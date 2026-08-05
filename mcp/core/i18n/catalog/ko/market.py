"""Korean (ko) messages for the 'market' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "market — 공개 큐레이션 카탈로그(계정·인증 불필요).\n\n"
        "## 검색/브라우징 (기본, action 생략)\n"
        "  market()                              → 큐레이션 순, 상위 결과\n"
        "  market(query='mcp auth')              → 자유텍스트 검색(제목/태그)\n"
        "  market(filter='build')                → 카테고리 필터\n"
        "  market(order='hot')                   → pull 많은 순(데이터 부족하면 큐레이션 순으로 "
        "폴백 — 조용히 안 속이고 정직하게 알림)\n"
        "  market(order='new')                   → 최신 발행순\n"
        "  market(id='lr-xxxxxxxx')              → 단건 상세(query= 없이)\n\n"
        "## pull\n"
        "  market(action='pull', id='lr-xxxxxxxx')  → 이 프로젝트로 반입(ingest.ingest_item, "
        "openbox pull 과 같은 프리미티브)\n"
        "    - 이미 pull됨(같은 source id)       → 멱등, 아무 것도 안 바뀜\n"
        "    - 큐레이터가 새 내용으로 재발행함     → 로컬 사본이 최신으로 교체됨(그 사본에 한 로컬 "
        "수정은 사라짐 — loud 경고)\n"
        "    - 더 이상 제공 안 함(removed/retired) → 이미 있는 사본은 무영향, 명확히 안내, "
        "didyoumean 없음(실존 id일 뿐 오타가 아니므로)\n"
        "    - 없는 id                           → 근접 카탈로그 id 로 didyoumean\n\n"
        "전부 무료 — v1엔 결제 단계 없음."
    ),
    "err_invalid_action": "오류: market() action은 '' (검색/브라우징) 또는 'pull' 이어야 합니다.",
    "err_no_id": "오류: action='pull' 은 id=(카탈로그 항목 id, lr-*/dc-*) 필수.",
    "err_network": "오류: market 요청 실패 ({code}) — {resp}",
    "err_not_found": "market: '{id}' 없음.",
    "didyoumean_item": "market(action='pull', id='{id}')  # {title}",
    "didyoumean_suffix": " 혹시: {items}",
    "removed_tombstone": "[{id}] 더 이상 제공되지 않음(회수일 {date}) — 기존 사본은 영향 없음.",

    "search_header_query": "market — \"{query}\" ({count})",
    "search_header_hot": "market — hot ({count})",
    "search_header_new": "market — new ({count})",
    "search_header_curated": "market — curated ({count})",
    "search_header_category_suffix": " · category={category}",
    "hot_insufficient_banner": "(아직 pull 데이터가 부족해 큐레이션 순으로 표시)",
    "empty_result": "market 카탈로그에서 결과 없음. 검색어를 넓히거나 filter= 를 빼보세요.",
    "result_tags_suffix": " #{tags}",
    "result_line": "- **{title}** — {category}{tags_suffix} [{id}]",
    "result_summary_line": "  {summary}",

    "detail_header": "# {title} [{id}]",
    "detail_category_line": "**category:** {category}",
    "detail_curator_line": "**curator:** {curator}",
    "detail_tags_line": "**tags:** {tags}",
    "detail_published_line": "**published:** {date}",
    "detail_pulls_line": "**pulls:** {count}",
    "detail_sections_header": "\n## sections ({count})",
    "detail_sections_item": "- {heading}",
    "detail_pull_cta": "\npull: market(action='pull', id='{id}')",

    "pull_success": "[{id}] installed — 1 absorbed ({kind})",
    "pull_success_workspace_own": "workspace: {anchor}",
    "pull_success_workspace_parent": "workspace: {anchor} (상위 {store} 에 저장됨)",
    "pull_success_next": "next: brief()",
    "pull_deduped": "[{id}] 이미 설치됨 — 할 일 없음.",
    "pull_updated": "[{id}] 갱신됨 — 로컬 사본이 최신 버전으로 교체됨.",
    "pull_updated_warning": "⚠ 로컬 사본 교체됨 — 이 사본에 했던 로컬 수정은 사라졌습니다.",
}
