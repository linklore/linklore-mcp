"""Korean (ko) messages for the 'doc_rollup' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "doc_rollup — 연결 lore 수집 → AI 요약용 markdown\n\n"
        "  doc_rollup(id='dc-xxx')\n\n"
        "동작: MCP가 관련 lore(works 명시 + 태그 매칭) 모음.\n"
        "MCP는 직접 수정 안 함. AI가 읽고 요약 초안 제안 → 사용자 확인 →\n"
        "AI가 edit(id, items='...') 호출.\n\n"
        "⚠️ doc 자동 덮어쓰기 금지. 사용자 판단 필수."
    ),
    "err_no_id": (
        "오류: id 필수 — doc_rollup(id='dc-xxx') (rollup은 doc 1건 대상 집계라 "
        "목록 모드 없음 — 대상 후보는 show(type='doc') 또는 doc_flow()로 찾을 것)"
    ),
    "not_found": "오류: doc '{id}'를 찾을 수 없습니다.",
    "tags_label": "태그: {tags}",
    "items_header_progress": "## 현재 items ({done}/{n})",
    "items_header_plain": "## 현재 items ({n})",
    "items_none": "(없음)",
    "explicit_header": "## 명시 연결 lore ({n}건)",
    "explicit_none": "(없음 — lore.works에 이 doc 연결된 항목)",
    "tag_header_base": "## 태그 매칭 lore ({n}건",
    "tag_header_omitted": " / 전체 {total}건 — 최신순 상위 {limit}만, 외 {omitted}건 생략",
    "tag_header_footer": " · 기준: {tags})",
    "tag_none": "(없음 — 범용 태그(design/decision 등)는 노이즈라 매칭 제외. 특정 태그만 매칭)",
    "tag_omitted_notice": (
        "  ⚠️ {omitted}건 생략됨 (상위 {limit}만 표시) — 롤업 전 전체 확인: "
        "show(tag='{tag}')"
    ),

    "rollup_insufficient_stub": "(롤업 재료 부족 — 연결 lore {n}건. lore 가 더 쌓이면 items 초안 제안 가능)",
    "ai_guide_header": "## 📌 AI 처리 가이드",
    "ai_guide_1": "1. 위 lore 내용을 읽고 **items 재구성 초안** 작성",
    "ai_guide_2": "2. **사용자에게 제안**: 어떤 항목이 신규/수정/완료될지",
    "ai_guide_3": "3. 사용자 확인 후에만 `edit(id='{id}', items='...')` 호출",
    "ai_guide_warn": "⚠️ **doc 자동 덮어쓰기 금지**. doc은 프로젝트 기준점이므로 사용자 판단 필수.",
    "ai_guide_tip": "필요 시 `edit(id='{id}', tags='+새태그')` 등도 함께 제안 가능.",

    "more_lines_suffix": "  ... (+{n}줄)",
}
