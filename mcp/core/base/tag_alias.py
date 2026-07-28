"""Multilingual tag alias mapping applied at query time."""
_ALIAS_TABLE = {

    "기능": "product", "제품": "product", "feature": "product", "feat": "product",

    "버그": "bug", "결함": "bug", "fix": "bug",

    "작업": "task", "할일": "task", "todo": "task",

    "기술": "tech", "인프라": "tech",


    "삽질": "lesson", "교훈": "lesson", "함정": "lesson",

    "결정": "decision", "선택": "decision",

    "패턴": "pattern", "컨벤션": "pattern",

    "체크리스트": "checklist",
}


def resolve_tag(tag: str) -> str:
    lowered = tag.strip().lower()
    return _ALIAS_TABLE.get(lowered, lowered)


RETIRED_RULE_TAG = "rule"


def strip_retired_rule_tag(tags: list) -> tuple[list, bool]:
    if not tags:
        return tags, False
    found = any(isinstance(t, str) and t.strip().lower() == RETIRED_RULE_TAG for t in tags)
    if not found:
        return tags, False
    return [t for t in tags if not (isinstance(t, str) and t.strip().lower() == RETIRED_RULE_TAG)], True
