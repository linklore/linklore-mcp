"""Korean (ko) messages for the 'nudges' surface."""
MESSAGES: dict[str, str] = {


    "nudge_after_init_no_tags": "\n\n💡 기존 lore {count}건 (supersede 제외) 인식됨",
    "nudge_after_init_with_tags": (
        "\n\n💡 기존 lore {count}건 (supersede 제외) 인식 · 상위 태그: {tags}"
        "\n   → brief()로 전체 현황 확인"
    ),


    "related_doc_hint": "💡 관련 doc: {names}",
}
