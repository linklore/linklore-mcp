"""Korean (ko) messages for the 'guard' surface."""
MESSAGES: dict[str, str] = {

    "stale_doc_hint": "[stale] doc 업데이트 추천: {names}{extra}",
    "stale_doc_tip": "  → show(type='doc')로 확인 후 edit로 반영",

    "stale_extra": " 외 {n}건",

    "stale_lore_header": "[lore] 관련 함정/룰 {n}건:",
    "stale_lore_more": "  (+{n}건 더)",

    "file_surface_header": "⚠️ 이 파일 관련 결정/함정 {n}건 (LinkLore — 변경 전 확인):",
    "file_surface_more": "  (+{n}건 더 — show(file=) 로 전체)",
}
