"""Korean (ko) messages for the 'project' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "brief — 프로젝트 대시보드\n\n"
        "세션 시작 시 호출. 기능 목록 + lore 통계 + stale 감지 + 최근 활동.\n"
        "dismiss: 넛지 끄기 (쉼표 구분 키)\n"
        "undismiss: 넛지 복원"
    ),


    "identity_name_part": " ({name})",
    "identity_connected": "iam: @{handle}{name_part} ✓ 계정 연결됨",


    "identity_project_acting": "iam: @{handle}{name_part} ✓ 프로젝트 iam으로 행동 중",
    "identity_local_only": "iam: @{handle}{name_part} · 로컬 전용 (계정 연결: login)",


    "location_counts": "doc {doc_count} lore {lore_count} (전체, supersede·dropped 포함)",
    "location_own_store": "여기: {anchor} · 자체 저장소 · {counts}",
    "location_parent_store": (
        "여기: {anchor} · 상위 워크스페이스 '{store}' 에 귀속 "
        "(이 폴더 자체 저장소 아님) · {counts}\n"
        "   이 폴더 독립 메모리: init()"
    ),
    "location_pin_suffix": "\n📌 pin: {name} ({path}) — 해제: config(action='unpin')",
    "location_identity_suffix": "\n🪪 프로젝트 iam: {display} — config(action='whoami')로 상세",


    "brief_empty": (
        "# {name}\n\n"
        "여기: {name} · 미등록 (.linklore 없음)\n\n"
        "시작하기:\n"
        "- 다른 곳에 이미 프로젝트가 있나요? `config(action='projects')`로 목록 확인 후 "
        "`config(action='pin', dir='/프로젝트/경로')`로 새로 만들지 않고 여기에 붙이기\n"
        "- 새로 시작: `init()`            이 폴더에 독립 발자취 메모리 시작\n"
        "- `add(type='lore'/'doc', ...)`  (init 후) 첫 기록 남기기 (lore-first)\n"
        "- `show(file='경로')` / `show(query=...)`  (등록 후) 관련 기억 검색"
    ),


    "doc_flow_header": "**doc 흐름 ({count}):**",
    "doc_flow_item": "- {title} → {steps}단계 [doc_flow(id='{id}')]",
    "doc_flow_more": "  외 {count}건 — doc_flow()",


    "cleanup_header": "**정리 후보:**",
    "cleanup_extra_suffix": " 외 {count}건",
    "cleanup_stale_item": "- #{tag} lore {count}건 누적 — 후보 doc: {titles}{extra} — 분배/업데이트 고려",
    "cleanup_pending_item": "- #{tag} lore {count}건 누적, 관련 doc 없음 — doc_rollup/수동 doc 정리 고려",


    "external_sources_header": "**외부 source ({count}):**",
    "auto_search_flag": "auto_search ",
    "external_source_local": "- [{name}] {auto}— 로컬 link (항상 최신)",
    "external_source_no_access": "- [{name}] {auto}— ⚠️ 접근 안 됨 (로그인 필요/만료 또는 비멤버) → login",
    "external_source_first_pull": "- [{name}] {auto}— 🔔 첫 pull 필요 (rev {rev}) → openbox(name='{name}', action='show')",
    "external_source_changed": "- [{name}] {auto}— 🔔 변경 있음 (rev {last} → {current}) → openbox(name='{name}', action='show')",
    "external_source_latest": "- [{name}] {auto}— 최신 (rev {rev})",
    "external_sources_footer": "  → openbox(name=, action='pull', id=) 카피",


    "stale_header": "코드 변경 후 doc 미갱신 ({count}건) — status로 확인",
    "stale_file_extra": " 외 {count}개",
    "stale_item": "  - {name}: {files}",


    "hotspot_tag": "  {warn}{title} [{id}]",
    "hotspot_line": "    {path} ·{age}{tag}",


    "codemap_stale_suffix": " · 지도 갱신 중",
    "codemap_header": "## 코드 지형 (자동파생{stale})",
    "codemap_head_bits_line": "  {bits}",
    "codemap_run_line": "  실행: {bits}",
    "codemap_structure_line": "  구조: {mods}",
    "codemap_landmarks_line": "  → {items}",
    "codemap_entities_more": " 외 {count}",
    "codemap_entities_line": "  명사: {entities}{more}",
    "codemap_hotspot_legend": " · ⚠=미결",
    "codemap_hotspot_header": "  핫스팟 (최근+결정{legend}):",


    "title_header": "# {name}",
    "legend_doc": "doc = 설계·기능·기술문서·체크리스트 → show(type='doc')",
    "legend_lore": "lore = 결정·삽질·교훈·규칙 → show()",
    "doc_summary": "doc: {total}건 (done {done}) — 목록 show(type='doc') · 필터 show(type='doc', tag='...')",
    "tag_hint_more": " 외 {count}개",
    "tag_hint_line": "  태그(빈도순): {tags}",


    "lore_summary": "lore: {count}개 (supersede·dropped 제외) — 목록 show() · 필터 show(tag='...')",
    "lore_summary_zero": "lore: 0개",
    "rule_doc_note": " · doc {count}",
    "rule_header": "**rule ({count}{doc_note}):**",
    "rule_item": "- {title} [{id}]",
    "rule_tail_more": "  외 {count}건 → show(status='rule')",
    "rule_tail_default": "  → show(status='rule')",
    "rule_tail_doc_suffix": " · doc은 show(type='doc', status='rule')",
    "unresolved_header": "**미결:**",
    "unresolved_tags_paren": " ({tags})",
    "unresolved_item": "- {title}{tags_suffix} [{id}]",
    "recent_activity_header": "**최근 활동:**",
    "recent_activity_item": "- [{kind}] {title} ({date}){author} [{id}]",
    "nudge_no_doc": "doc 없음 → 핵심 구조 문서는 add(type='doc')",
    "nudge_no_lore": "lore 없음 — 삽질 기록 시작 권장 (add)",
    "recommend_header": "추천:",
    "recommend_item": "  - [{nudge_key}] {msg}",
    "section_failed": "  (⚠ {name} 표시 실패: {error})",


    "section_name_doc_flow": "doc 흐름",
    "section_name_cleanup": "정리 후보",
    "section_name_external_sources": "외부 source",
    "section_name_stale": "stale 감지",
    "section_name_codemap": "코드 지형",
}
