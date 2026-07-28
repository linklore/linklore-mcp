"""Korean (ko) messages for the 'doc_flow' surface."""
MESSAGES: dict[str, str] = {

    "flow_tool_desc": "[read-only] doc_flow(id) — doc flowLink 체인을 순서대로 렌더링 (여정 뷰).",

    "flow_help": (
        "doc_flow — doc 여정 뷰 (flowLink 체인)\n\n"
        "  doc_flow()            — 전체 flow 시작점 목록\n"
        "  doc_flow(id='dc-xxx') — 시작점에서 flowLink 체인 펼침\n\n"
        "편집: edit(id='dc-xxx', links=['dc-yyy'], flow=True)\n"
        "flowLink는 단방향 — 분기가 있으면 첫 타겟만 표시.\n"
        "(끊어진 링크) 정리 = doctor(action='fix') — 타겟 없는 링크 자동 삭제."
    ),
    "no_flow_links": "flow 연결 없음\nedit(id='dc-xxx', links=['dc-yyy'], flow=True)로 흐름 생성",
    "no_clear_start": "명확한 시작점 없음 — flowLink 있는 doc {n}건",
    "starts_header": "# doc_flow — 시작점 {n}건",
    "start_line": "- **{title}** [{id}] → {n}단계 체인",
    "starts_footer": "`doc_flow(id='dc-xxx')`로 체인 펼치기",
    "flow_not_found": "오류: doc '{id}'를 찾을 수 없습니다.",
    "chain_header": "# doc_flow({id}) — {n}단계",
    "current_suffix": "  (현재 위치)",
    "branch_suffix": "  (+{n} 분기)",
    "branches_header": "## 분기 ({n}개 — 첫 번째만 따라감)",
    "branch_item": "- {title} [{id}]",
    "branch_item_broken": "- (끊어진 링크) [{id}]",


    "map_tool_desc": "[read-only] doc_map(oneline) — 전체 doc 링크 네트워크 조감.",

    "map_help": (
        "doc_map — doc 링크 네트워크 조감\n\n"
        "  doc_map(oneline=True)  — 덩어리별 대표 제목+건수 요약 (큰 프로젝트 조감용, 먼저 이걸로)\n"
        "  doc_map()              — 덩어리별 전체 doc + 링크 상세\n\n"
        "↔ docLink (관련) / → flowLink (흐름)\n"
        "끊어진 링크 정리 = doctor(action='fix') — 타겟 없는 링크 자동 삭제."
    ),
    "no_docs": "doc 없음",
    "map_header_body": " ({n}건: 연결 {conn}덩어리, 미연결 {iso}건",
    "map_header_dangling": ", 끊어진 링크 {n}건",
    "map_header_empty_note": "\n아직 연결 없음 (정상 — 쌓이면 link 로 묶기)",
    "more_suffix": " 외 {n}",
    "chunk_oneline_line": "## 덩어리 {i} ({n}건): {preview}{more}",
    "isolated_oneline_footer": "\n미연결 {n}건 — 상세: doc_map()",
    "chunk_header": "## 덩어리 {i} ({n}건)",
    "external_label": "(외부)",
    "isolated_header": "## 미연결 ({n}건)",
    "truncated_suffix": "  ... 외 {n}건",
    "dangling_header": "## 끊어진 링크 ({n}건)",
    "dangling_item": "- **{title}** [{id}] {field} → {target} (타겟 없음)",
}
