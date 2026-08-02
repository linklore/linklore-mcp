"""Korean (ko) messages for the 'config' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "프로젝트 설정(오픈박스 source 옵션) + iam + 세션 pin.\n"
        "\n"
        "⚠️ handle/name/email 은 프로젝트가 아니라 이 머신 전체에 적용됩니다.\n"
        "\n"
        "공유는 별도 도구: openbox(오픈박스 공유·멤버).\n"
        "\n"
        "action 11갈래:\n"
        "- action='whoami' → 내 신원(handle/name/email) 조회\n"
        "- action='version' → 서버 코드 버전(git commit) 조회\n"
        "- action='sources' → 등록된 외부 source(오픈박스) 목록\n"
        "- action='option' → 외부 source 설정(auto_search=/show_prefix=) 변경\n"
        "- action='sync' → 외부 source 캐시 강제 갱신\n"
        "- action='forget' → 외부 source 등록 해제\n"
        "- action='pin' → 이 세션을 특정 프로젝트에 고정\n"
        "- action='unpin' → 세션 고정 해제\n"
        "- action='sessions' → 내 계정 세션 목록/강제로그아웃(revoke=)\n"
        "- action='projects' → 이 머신의 전체 LinkLore 프로젝트 목록\n"
        "- action='delete_project' → 서버상 개인공간 영구삭제 (2단계 confirm)\n"
        "\n"
        "help=true로 상세 안내."
    ),

    "help": (
        "config — 프로젝트 설정 + 외부 오픈박스 source 옵션 + user 정보\n"
        "\n"
        "발자취 모델 (git 개념): 본진=로컬(사적), 내 서버=push/pull(나만), 오픈박스=openbox 도구(공유·초대제).\n"
        "push/pull(본진↔내 서버)·openbox(오픈박스 공유·멤버)는 별도 도구.\n"
        "\n"
        "## user (글로벌 — 프로젝트가 아니라 이 머신 전체에 적용)\n"
        "  config(action='whoami')                  현재 iam + 이 프로젝트의 iam (조회 전용)\n"
        "  config(handle='alice')                    handle 변경 (action 없이 호출)\n"
        "  config(name='Alice', email='d@e.com')     name/email 변경\n"
        "  config(name='-')                          name 해제(clear) — email='-'/handle='-' 도 동일\n"
        "\n"
        "## 계정 세션\n"
        "  config(action='sessions')                내 계정 활성 세션 목록\n"
        "  config(action='sessions', revoke='<id>') 개별 세션 폐기\n"
        "  config(action='sessions', revoke='all')  현재 세션 제외 전부 폐기 (유령 세션 정리)\n"
        "\n"
        "## 외부 오픈박스 source 옵션\n"
        "  config(action='sources')         등록된 오픈박스 목록\n"
        "  config(action='option', name='team-prj', auto_search=false)  검색 포함 여부\n"
        "  config(action='sync')            오픈박스 변경 요약\n"
        "  config(action='forget', name='team-prj')  source 등록 완전 해제(registry+openbox 양쪽)\n"
        "  ⚠️ 오픈박스 가입/배선은 openbox(action='join'/'docking').\n"
        "\n"
        "## 내 서버(push/pull) / 오픈박스 공유·배선 (별도 도구)\n"
        "  push(id='lr-xxx')                본진 → 내 서버 (나만)\n"
        "  openbox(name='team-prj', action='docking', url='https://.../api/projects/<pid>')  기존 멤버십 배선\n"
        "  openbox(name='team-prj', action='push', id='lr-xxx')   본진 → 오픈박스 공유\n"
        "  openbox(name='team-prj', action='show')   오픈박스 훑기 (캐시 자동 갱신)\n"
        "  openbox(name='team-prj', action='pull', id='lr-xxx')   항목 → 본진 흡수\n"
        "\n"
        "## 세션 pin\n"
        "  project_dir 는 MCP 표면에서 제거됨(init 제외) — 여러 프로젝트를 오갈 땐 pin 사용.\n"
        "  config(action='pin', dir='/path')  이 세션의 기준 프로젝트 고정 (명시 project_dir 이 항상 우선)\n"
        "  config(action='pin')               현재 pin 조회\n"
        "  config(action='unpin')             pin 해제 — cwd/CLAUDE_PROJECT_DIR 로 복원\n"
        "  ⚠️ 프로세스 메모리 전용 — 영속 안 됨, 세션(서버 프로세스) 종료 시 자동 소멸.\n"
        "\n"
        "## 일반\n"
        "  config()                   현재 설정 + 외부 source 요약\n"
        "  config(action='projects')  전체 LinkLore 프로젝트 목록 (별칭: projects=true)\n"
        "  config(action='version')   현재 mcp 코드 버전(git commit) 확인\n"
        "  config(action='delete_project', project_id=, confirm='<확인 코드>')  개인공간(내 서버) 영구 삭제 — 1차 호출이 1회용 확인 코드를 발급, project_id 미지정 시 pin된/현재 프로젝트 대상, 오픈박스는 openbox(name=, action='delete')"
    ),

    "err_invalid_action": "오류: 알 수 없는 action '{action}'. 유효: {valid} (또는 비움=현재 설정 표시). help=True.",

    "version_line": "mcp version: {commit} ({branch}){dirty}",
    "version_dirty_flag": " *(dirty)",

    "unpin_done": "📌 pin 해제 — 이후 cwd/CLAUDE_PROJECT_DIR 기준으로 복원.",
    "pin_none": "pin 없음 — config(action='pin', dir='/path')",
    "pin_no_store_suffix": " (.linklore 없음 — 쓰기는 init() 먼저)",
    "pin_store_parent_suffix": " (상위 '{parent}'의 공유 저장소 사용 중 — 독립하려면 init())",
    "pin_status": "📌 pin: {name} ({path}){store_note}",
    "err_dir_not_found": "오류: 디렉토리 없음 — {dir}",
    "store_has": "저장소 있음",
    "store_parent": "상위 '{parent}'의 공유 저장소 사용 중 — 독립하려면 init()",
    "store_none": "저장소 없음 — 쓰기는 init() 먼저",
    "pin_set": "📌 pin: {name} ({path}) — {store_note}",

    "whoami_project_identity": "\n이 프로젝트: {display} (프로젝트 iam)",
    "whoami_account_acting": "\n계정으로 행동 중",
    "err_whoami_readonly": "오류: whoami는 조회 전용 — 변경은 config(handle=..., name=..., email=...)",

    "err_login_required": "오류: 로그인 필요 — uvx llre login",
    "err_revoke_failed": "오류: 세션 폐기 실패 ({code}) — {body}",
    "session_revoked": "세션 {id} 폐기됨",
    "sessions_revoked_all": "{n}개 폐기 — 현재 세션은 유지됨",
    "err_sessions_list_failed": "오류: 세션 목록 조회 실패 ({code}) — {resp}",
    "no_active_sessions": "활성 세션 없음",
    "sessions_header": "# 활성 세션 ({count})",
    "session_current_marker": " (현재)",
    "session_line": "- {id}{marker}  생성 {created}  최근사용 {last_used}  만료 {expires}",
    "sessions_footer": "폐기: config(action='sessions', revoke='<id>') (개별, 즉시) · revoke='all' (현재 세션 제외 전부, 확인 필요)",
    "sessions_revoke_all_desc": "세션 일괄 폐기 (현재 세션 제외)",
    "sessions_revoke_all_confirm": (
        "⚠️ 현재 세션을 제외한 내 계정의 모든 활성 세션을 폐기합니다 — 되돌릴 수 없습니다.\n"
        "  1. 실행: config(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),

    "no_sources": "등록된 외부 source 없음",
    "src_list_header": "# 외부 source ({count})",
    "err_source_not_registered": "오류: 소스 '{name}' 미등록 (config(action='sources') 로 확인)",
    "no_sources_hint": "등록된 외부 source 없음. openbox(action='join'/'docking')로 오픈박스 연결",

    "sync_counts": "  lore {lore} (새 {new_lore}) · doc {docs} (새 {new_docs})",
    "sync_new_lore_header": "  새 lore (상위 3):",
    "sync_new_doc_header": "  새 doc (상위 3):",
    "no_changes": "변경 없음.",

    "err_name_required": "오류: name 필수",
    "option_updated": "[{name}] 옵션 갱신 — auto_search={auto_search}, show_prefix={show_prefix}",

    "forget_done": "[{name}] source 등록 해제 — {where}",

    "settings_header": "# {name} 설정",
    "default_sources_summary": "\n외부 source ({count}): {names}",
    "default_sources_detail_hint": "  상세: config(action='sources')",
    "default_projects_hint": "전체 프로젝트 목록: config(projects=true)",

    "no_projects": "LinkLore 프로젝트 없음. init로 시작하세요.",
    "projects_header": "# LinkLore 프로젝트 ({count}개)",

    "delete_project_personal_label": "개인 공간",
    "err_delete_project_use_rm_openbox": "오류: 오픈박스 삭제는 openbox(name='{name}', action='delete') 사용 — config(action='delete_project')는 개인 공간 전용",
    "err_delete_project_no_target": "오류: 삭제 대상 없음 — project_id= 직접 지정하거나, 이 프로젝트를 config(action='pin')으로 먼저 지정한 뒤 재시도(pin된/현재 프로젝트의 개인 공간)",
    "err_delete_project_bad_ref": "오류: project_id='{ref}' — prj-xxxxxxxx (config(action='projects')에 표시) 또는 풀 UUID 로 지정하세요",
    "err_delete_project_ref_not_found": "오류: '{ref}' 에 해당하는 프로젝트 없음 — 주소록·내 멤버십에서 못 찾음. 확인: config(action='projects')",
    "delete_project_ambiguous_header": "오류: '{ref}' 가 여러 프로젝트와 일치 — 어느 것인가요? (자동 선택 안 함)",
    "delete_project_ambiguous_item": "  {n}. {label} ({prj}) → {cmd}",
    "candidates_more": "  … 외 {n}건",
    "delete_project_desc": "개인 공간 영구 삭제 — {label} ({id})",
    "delete_project_confirm_needed": (
        "⚠️ [{label}] ({id}) 서버에서 영구 삭제 — lore/doc/멤버/초대 전부 사라지고 복구 불가.\n"
        "  1. 실행: config(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),
    "err_delete_project_failed": "오류: 삭제 실패 ({code}) — {body}",
    "delete_project_done": "[{label}] ({id}) 서버에서 영구 삭제됨.",
}
