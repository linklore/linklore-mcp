"""Korean (ko) messages for the 'local' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "local_cross — 같은 디스크의 다른 LinkLore 프로젝트 직접 조작 (move/copy/show)\n\n"
        "  local_cross(action='move', id='lr-x'|'dc-x', to='/path')         이관 → 미리보기 + "
        "forced(...) 호출문, 그대로 복붙해 확정\n"
        "  local_cross(action='move', id=[...], to='/path')                 이관 다건 → 미리보기 + "
        "forced(...) 호출문(단건과 동일 경로)\n"
        "  local_cross(action='copy', id='lr-x', to='/path')                사본 생성 (원본 보존, 새 id, 단건 즉시)\n"
        "  local_cross(action='show', from_dir='/other', query='...')       형제 워크스페이스 조회\n"
        "  local_cross(action='move'|'copy', ..., from_dir='/src')          원본 워크스페이스 명시 — "
        "move/copy 공통 (기본 cwd)\n\n"
        "move: 보존 필드 = id·생성일·files·tags·level·status·body·items. 원본은 휴지통行"
        "(soft, restore(id) 로 복구 가능). 출처 기록(source_location='local'·원 프로젝트·원본 id).\n"
        "copy: move 와 동일 판정, 원본 삭제만 스킵. 새 id 발급 + 동일 출처 기록. 같은 원본 "
        "재복사는 source_id 대조로 멱등 스킵 — id 충돌 거부 없음.\n"
        "move는 원본을 지우는 비가역 동작이라 개수 무관 항상 미리보기만 반환 — 실행은 미리보기가 "
        "그대로 찍어주는 forced(action='local_cross', mode='move'|'copy', id=[...], to=..., "
        "from_dir=...) 를 복붙해 재호출(슬롯 저장 없음, v4 게이트). copy는 원본이 안 사라지는 "
        "가역 동작이라 무변 — 단건은 즉시 실행, 다건(len>1)만 동일한 미리보기+forced() 재호출.\n"
        "show: from_dir 필수. query/tag/type/status 를 그대로 대상 워크스페이스에 위임 — 검색 "
        "로직은 show() 와 동일.\n"
        "cross-workspace 링크(works/supersede/docLink)는 move/copy 둘 다 안 따라감 — 끊김 표시.\n"
        "대상 워크스페이스가 없으면(move/copy) 실행하지 않음 — 먼저 init(project_dir=...) 로 생성 "
        "(경계 생성은 init 전용, 자동 생성 없음).\n"
        "경계: 서버 너머/팀 공유는 오픈박스(openbox 도구) — local_cross() 은 내 디스크 안에서만."
    ),

    "err_action_invalid": (
        "오류: action='{action}' — 3갈래 중 하나 필수:\n"
        "  action='move'   이관 (원본 삭제)\n"
        "  action='copy'   사본 생성 (원본 보존)\n"
        "  action='show'   형제 워크스페이스 조회 (읽기전용, from_dir 필수)"
    ),
    "err_no_to": "오류: to= (대상 워크스페이스 경로) 를 지정하세요.",


    "err_target_no_store": (
        "오류: 대상 '{to}' 에 저장소 없음 — 자동 생성하지 않습니다. "
        "대상 폴더에서 먼저 init(project_dir='{to}') 로 만든 뒤 다시 실행하세요."
    ),
    "note_target_absent": "ℹ️ 대상에 저장소 없음 — 실행하려면 먼저 init(project_dir='{to}') 가 필요합니다.",
    "err_same_workspace": "오류: 원본과 대상이 같은 워크스페이스입니다.",
    "err_same_workspace_walkup": (
        "오류: '{to}' 는 자체 저장소가 없어 상위 '{store}' 로 해석됨 — 원본과 같은 "
        "워크스페이스입니다. 독립 프로젝트로 만들려면 먼저 init(project_dir='{to}')."
    ),
    "err_no_id": "오류: id 를 지정하세요.",
    "err_show_no_from_dir": "오류: action='show' 는 from_dir= (조회할 형제 워크스페이스 경로) 가 필수입니다.",


    "preview_header": "🔍 미리보기 — 실행 안 함 (원본 유지)\n",
    "transfer_desc": "{action} {n}건 → {to}",
    "forced_hint": (
        "확정하려면 다음을 그대로 호출하세요:\n"
        "  forced(action='local_cross', mode='{mode}', id={ids}, to='{to}', from_dir='{from_dir}')"
    ),

    "err_resolve": "[{id}] 오류: {rerr}",
    "err_kind": "[{id}] 오류: lore(lr-*)/doc(dc-*) 만 이관·복사 가능",

    "reason_not_found": "원본에 없음",
    "reason_dup": "대상에 이미 존재",
    "reason_self": "대상에 원본이 이미 있음(같은 id) — 반입 불필요",
    "reason_already": "이미 반입됨 — 대상 {existing} (source_id 멱등)",
    "err_move_cancel": "[{id}] 오류: {reason} — 이관 취소",
    "err_copy_cancel": "[{id}] 오류: {reason} — 복사 취소",
    "err_preview_skip": "[{id}] 오류: {reason} — 건너뜀",

    "skip_self": "[{id}] 스킵 — 대상에 원본이 이미 있음 (반입 불필요)",
    "skip_already": "[{id}] 스킵 — 이미 반입됨 (대상 {existing}, source_id 멱등)",
    "warn_dropped": "  ⚠ 링크 {dropped} 끊김(cross-ws)",
    "note_trash_ghost": "  ℹ️ 대상에 같은 id 의 휴지통 유령이 있어 자동 정리 후 이관됩니다",
    "moved_lore": '[{id}] "{title}" 이관됨 — id·생성일·files 보존, 출처 기록{warn}',
    "moved_doc": '[{id}] "{title}" 이관됨 — id·생성일·items 보존, 출처 기록{warn}',
    "copied_lore": '[{new_id}] "{title}" 복사됨 — 새 id (원본 {id}·생성일·files 보존), 출처 기록{warn}',
    "copied_doc": '[{new_id}] "{title}" 복사됨 — 새 id (원본 {id}·생성일·items 보존), 출처 기록{warn}',
    "preview_lore": '[{id}] "{title}" → 이관 예정 (생성일·files 보존){warn}',
    "preview_doc": '[{id}] "{title}" → 이관 예정 (생성일·items 보존){warn}',
    "preview_copy_lore": '[{id}] "{title}" → 복사 예정 (원본 보존, 새 id 발급·출처 기록){warn}',
    "preview_copy_doc": '[{id}] "{title}" → 복사 예정 (원본 보존, 새 id 발급·출처 기록){warn}',
}
