"""Single definition of file-to-item matching."""
FILEMATCH_SOURCE = '''\
def match_file(query: str, candidate: str) -> bool:
    """Whether query and candidate paths are related (permissive union match).

    Matches: exact match, directory prefix ("web/" vs "web/app.js"),
    basename suffix ("app.js" vs "web/app.js"), bidirectional substring —
    all case-insensitive. Empty string never matches.
    """
    if not query or not candidate:
        return False
    q = query.lower()
    c = candidate.lower()
    return q in c or c in q
'''

exec(compile(FILEMATCH_SOURCE, "<filematch:match_file>", "exec"), globals())


SCOPECLASSIFY_SOURCE = '''\
def is_scope_tag(candidate: str, project_root) -> bool:
    """Whether a registered path is a scope tag (directory/jurisdiction) —
    used to exclude scope tags from stale-doc nudges.

    file tag (strong coupling) = doc goes stale when the file changes /
    scope tag (jurisdiction declaration) = surfacing only.
    Resolution order (disk-first — avoids misclassifying extensionless
    real files like Makefile):
    1. empty string -> False
    2. trailing slash -> True
    3. exists on disk as a directory -> True
    4. exists on disk as a file -> False
    5. not on disk -> True if basename has no extension (dead directory
       path), False otherwise
    """
    from pathlib import Path
    if not candidate or not candidate.strip():
        return False
    c = candidate.strip()
    if c.endswith("/"):
        return True
    p = Path(project_root) / c
    if p.is_dir():
        return True
    if p.is_file():
        return False
    return "." not in c.rsplit("/", 1)[-1]
'''

exec(compile(SCOPECLASSIFY_SOURCE, "<filematch:is_scope_tag>", "exec"), globals())
