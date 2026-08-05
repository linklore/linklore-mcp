"""Korean (ko) messages for the 'router_show' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "show — 통합 조회 (내 프로젝트 전용 — 오픈박스 조회는 openbox(action='show'))\n\n"
        "## 대상/범위 (query, type)\n"
        "  query=ID  → 상세 (lr-*/dc-*)\n"
        "  query=ID+단어 혼합 → ID 매치 최상단 + 키워드 결과 (ID 오타는 힌트만, 키워드 오염 없음)\n"
        "  query=텍스트 → 통합 검색 (lore+doc)\n"
        "  type=컬렉션 → 목록 (lore/doc)\n"
        "  section=헤딩 → 섹션 조각 하나만 읽기 (query=id 단독, 다른 필터 결합 불가)\n"
        "  (없음) → lore 목록 (자기 + auto_search 외부 openbox 머지)\n\n"
        "## 필터 (tag, status, file, period, source_id)\n"
        "  tag, status(open/done/dropped/rule)\n"
        "  file(경로 매칭, files[] 인덱스 기준) — 코드 편집 전 확인 권장. 직접 Edit/Write 시엔 PreToolUse 훅이 자동 서빙하지만,\n"
        "    위임 전이나 조사 단계엔 직접 호출 필요. files[] 미등록 lore는 놓침 — 더 넓게 잡으려면 query=텍스트 병행\n"
        "  source_id — 반입 원본 id 역조회 (openbox('pull')·local copy/move — '이 항목 이미 가져왔나' 확인)\n"
        "  범위: period='24h'(최근 24시간) · period='7d'(최근 7일) · period='2026-07-01'(그날부터·UTC) · period='2026-07-01..2026-07-08'(사이·UTC)\n\n"
        "## 결과형태 (sort, max, oneline, superseded)\n"
        "  정렬: sort(newest/oldest/alpha), max(N건), oneline(한줄)\n"
        "  상세 조회 시 max= 는 클러스터 표시 상한 (기본 10, 목록 모드에선 기존처럼 건수 상한)\n"
        "  기본 건수: 무필터 조감(lore+doc 요약)은 각 10건 · tag 등 필터가 있는 목록은 30건 (max= 로 오버라이드)\n"
        "  기타: superseded=True → 구버전 lore·doc 둘 다 포함\n\n"
        "## 모드 (action)\n"
        "  action='graph' → 코퍼스 감사 집계 (status/태그/body길이/링크그래프 분포, 전수 카운트)\n"
        "  action='tags'  → 태그 목록\n"
        "  (없음) → 위 대상/범위·필터·결과형태 조합대로 목록/상세/검색\n\n"
        "## 배관 (help)\n"
        "  help=True → 이 안내"
    ),


    "log_help": (
        "log — 이력 조회 (SQL: lore/doc supersede 체인 + 본문 편집 이력 + 통합 타임라인)\n\n"
        "id → lore 변경 이력 (supersede 체인 + 본문 편집 이력) 또는 doc 변경 이력 "
        "(supersede 체인 + 본문 편집 이력) — 본문 편집 이력은 append/overwrite/section 변경을 시간순 전부 나열\n"
        "(없음) → 통합 타임라인 (lore/doc 변경 순)\n\n"
        "필터: period='24h'(최근 24시간) · period='7d'(최근 7일) · period='2026-07-01'(그날부터·UTC) · period='2026-07-01..2026-07-08'(사이·UTC), "
        "sort(oldest), max(기본20)"
    ),

    "err_action_invalid": "오류: action='{action}' 미지원 — graph|tags 중 하나",


    "err_section_combo": (
        "오류: section= 은 query=(id) 필요 + 다른 필터 없이 단독 결합만 가능 — "
        "type/tag/status/file/period/sort/max/oneline/superseded/action/source_id 를 제거하세요"
    ),

    "err_sort_invalid": "오류: sort='{sort}' 미지원 — {valid} 중 하나",

    "err_period": "오류: {err}",


    "err_max": "오류: {err}",

    "empty_project": (
        "결과 없음 — 아직 이 프로젝트에 기억이 없습니다.\n"
        "add(type='lore'/'doc', ...) 로 첫 기록을 남기면 발자취가 시작됩니다."
    ),

    "overview": (
        "{lore_part}\n"
        "  ↳ 좁히기: show(tag='...') · show(status='done') · show(query='검색어')\n\n"
        "{doc_part}\n"
        "  ↳ 좁히기: show(type='doc', tag='...')"
    ),

    "graph_title": "# 코퍼스 통계 (감사)",
    "graph_lore_summary": "lore: {live} live / {total} 전체 (supersede 포함)",
    "graph_status_label": "  status: ",
    "graph_tags_label": "  top 태그: ",
    "graph_tag_item": "#{t} {c}",
    "graph_body_len_line": "  body 길이: 중앙값 {median}자 · 평균 {mean}자 · 1500자+ {over}건({pct}%)",
    "graph_linkgraph_line": "  링크그래프: {nodes}개 노드, {edges}개 엣지, 컴포넌트 {components}개 (최대 {top})",
    "graph_doc_summary": "doc: {total} live (supersede·휴지통 제외)",
    "graph_footer": "→ 상세: show(tag=, status=, sort=, max=) · 전수는 max 크게",

    "tags_none_no_store": "태그 없음 (아직 기억 없음)",
    "tags_none": "태그 없음",
    "tags_header": "# 태그 ({n}개)",
    "tags_count_lore": "lore {n}",
    "tags_count_doc": "doc {n}",
    "tags_line": "- #{tag} ({counts})",


    "tags_truncated_hint": "\n  … 전체 {total}개 중 {shown}개 — 더: max={total}",

    "lore_none": "등록된 lore가 없습니다.",
    "lore_filtered_none": "조건에 맞는 lore가 없습니다. 전체 {total}건.",
    "lore_oneline_header": "lore ({shown}/{total}건)",
    "lore_cluster_suffix_oneline": "+{n}클러스터",
    "lore_header": "# lore ({shown}/{total}건)",
    "lore_cluster_suffix_full": "  +{n} 클러스터 (show(query=)로 전체)",


    "lore_date_header": "\n### {date}",

    "lore_cluster_suffix_full_openbox": "  +{n} 클러스터 (openbox(action='show', query=...)로 전체)",

    "list_truncated_hint": "\n  … 전체 {total}건 중 {shown}건 — 더: max={total}",


    "list_truncated_hint_clustered": "\n  … 전체 {total}건(클러스터 접힘 {collapsed}줄) 중 {shown}건 — 더: max={collapsed}",

    "log_no_history": (
        "'{id}' 변경 이력 없음 — 이력 추적은 lore(supersede 체인+본문 편집 이력)·"
        "doc(supersede 체인+본문 편집 이력)만. 현재상태는 show 로 확인하세요."
    ),

    "mixed_id_hits_header": "# ID 매치 ({n}건)",


    "mixed_id_miss": "⚠️ {hint}",


    "doc_match_hint": "\n  doc {n}건 매칭 — show({cmd})",
}
