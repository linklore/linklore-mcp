"""Markdown section parsing and replacement."""
from __future__ import annotations

import re

from core.i18n import msg as _msg

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_FENCE_PREFIXES = ("```", "~~~")


def _iter_sections(body: str) -> list[dict]:
    headings: list[dict] = []
    offset = 0
    in_fence = False
    for line in body.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        stripped = content.strip()
        if stripped.startswith(_FENCE_PREFIXES):
            in_fence = not in_fence
        elif not in_fence:
            m = _HEADING_RE.match(content)
            if m:
                level = len(m.group(1))
                text = m.group(2).strip()
                text = re.sub(r"\s+#+\s*$", "", text).strip()
                headings.append({"level": level, "text": text, "start": offset})
        offset += len(line)

    sections: list[dict] = []
    for i, h in enumerate(headings):
        end = len(body)
        for nxt in headings[i + 1:]:
            if nxt["level"] <= h["level"]:
                end = nxt["start"]
                break
        sections.append({"level": h["level"], "text": h["text"], "start": h["start"], "end": end})
    return sections


def _norm_query(s: str) -> str:
    return s.lstrip("#").strip().casefold()


def _find_section(sections: list[dict], query: str, *, read: bool = False) -> tuple[dict | None, str]:
    q = _norm_query(query)

    def _fmt(items: list[dict]) -> str:
        return ", ".join(f"'{'#' * s['level']} {s['text']}'" for s in items)

    exact = [s for s in sections if _norm_query(s["text"]) == q]
    if len(exact) == 1:
        return exact[0], ""
    if len(exact) > 1:
        return None, _msg("sections.ambiguous", candidates=_fmt(exact))

    sub = [s for s in sections if q and q in _norm_query(s["text"])]
    if len(sub) == 1:
        return sub[0], ""
    if len(sub) > 1:
        return None, _msg("sections.ambiguous", candidates=_fmt(sub))


    if not sections:
        return None, _msg("sections.not_found_no_headings_read" if read
                          else "sections.not_found_no_headings")
    return None, _msg("sections.not_found_read" if read else "sections.not_found",
                      sections=_fmt(sections))


def replace_section(body: str, query: str, new_content: str) -> tuple[str | None, str]:
    sections = _iter_sections(body)
    matched, err = _find_section(sections, query)
    if err:
        return None, err

    start, end = matched["start"], matched["end"]
    nl_idx = body.find("\n", start)
    heading_end = nl_idx if nl_idx != -1 else len(body)
    heading_line = body[start:heading_end]

    new_section_body = new_content.strip()
    first_line = new_section_body.split("\n", 1)[0]
    if _HEADING_RE.match(first_line):

        section_text = new_section_body + "\n"
    else:

        section_text = heading_line + "\n"
        if new_section_body:
            section_text += "\n" + new_section_body + "\n"

    before = body[:start]
    after = body[end:]
    if after:
        result = before + section_text + "\n" + after
    else:
        result = before + section_text
    return result, ""
