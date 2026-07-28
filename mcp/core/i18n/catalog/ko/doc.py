"""Korean (ko) messages for the 'doc' surface."""
MESSAGES: dict[str, str] = {

    "show_help": (
        "doc 조회 — show(type='doc') 로 통합됨 (lore=show 와 대칭)\n\n"
        "## 조회 (show)\n"
        "  show(type='doc')                — 전체 목록\n"
        "  show(type='doc', query='인증')   — 검색\n"
        "  show(type='doc', tag='tech')    — 태그 필터\n"
        "  show(type='doc', status='done') — 상태 필터\n"
        "  show(query='dc-xxx')            — 상세 보기 (id 는 type 불필요)\n\n"
        "## 생성/수정 (add/edit)\n"
        "  add(type='doc', title='인증', items=['OAuth','JWT'])\n"
        "  add(type='doc', relates='dc-old', title='새 버전', msg='...')  → supersede (옛 head=False)\n"
        "  edit(id='dc-xxx', items=['새 항목'])\n"
        "  edit(id='dc-xxx', items=[1,3])  → 완료 토글 (1-based)\n"
        "  edit(id='dc-xxx', action='remove', items=[2])  → 항목 제거 (파괴적, 1-based)\n"
        "  edit(id='dc-xxx', status='done')\n"
        "  link(a=X, b='dc-Y', action='supersede')  → 기존 dc-Y 로 묶어 대체(reconcile)\n\n"
        "  status: open(기본, 살아있음) | done(완료) | dropped(폐기) | rule(바뀌지 않는 기준)\n"
        "  show(type='doc', superseded=True) → supersede 된 옛 버전도 포함\n"
        "  show(type='doc', source_id='ext-id') → 반입 원본 id 역조회 (openbox('pull')·local copy/move)"
    ),
    "err_no_project": (
        "doc 없음 — 아직 이 프로젝트에 기억이 없습니다.\n"
        "add(type='doc', ...) 로 첫 문서를 만들면 발자취가 시작됩니다."
    ),
    "err_not_found": "오류: doc '{query}'를 찾을 수 없습니다.",

    "err_not_dc_lr_id": "'{raw}' dc-/lr- id 형식이 아님 (title→id 변환은 상위 classify_links 담당)",

    "err_items_schema_item": "  {i}번째 항목: 키 {keys} — 'text' 또는 'key' 없음",
    "err_items_schema_header": "items dict 항목엔 앵커 키('text' 또는 'key')가 필요합니다:\n",
    "err_items_schema_footer": (
        "\n\n올바른 예시:\n"
        "  체크리스트: {{\"text\": \"할 일\"}}\n"
        "  카탈로그: {{\"key\": \"이름\", \"value\": \"값\"}}"
    ),
    "err_no_match": "'{label}' 매칭 doc 없음",
    "err_sort_invalid": "오류: sort='{sort}' 미지원 — {valid} 중 하나",
    "err_empty": "doc 없음 — add(type='doc', title='...')로 생성",
    "limit_suffix": "\n  … 외 {n}건 (전체 {total}건) — 더: max={total}",
    "matched_header": "{n}건 매칭:",

    "files_label": "파일: {files}",
    "related_label": "관련: {target}",
    "flow_label": "흐름: {target}",
    "link_more": "  … 외 {n}건",
    "backref_label": "참조됨: {refs}",
    "backref_more": " 외 {n}건",

    "items_count_suffix": " {n}항목",

    "oneline_header": "doc ({m}/{t}건)",

    "uncategorized": "미분류",
    "grouped_header": "# doc ({n}건)",
    "grouped_done_footer": "완료 {done}/{n}",
}
