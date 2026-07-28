"""Korean (ko) messages for the 'local' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "local(action, id, to='워크스페이스경로', from_dir='') — 같은 디스크의 다른 LinkLore "
        "프로젝트 직접 조작 (lore·doc 둘 다 대상).\n"
        "\n"
        "action='move'   다른 워크스페이스로 이관 (원본 삭제·id 보존, 생성일·files·tags·level·"
        "status·body·items 보존, 출처 기록)\n"
        "action='copy'   다른 워크스페이스로 사본 생성 (원본 보존, 새 id 발급 + 출처 기록 — "
        "같은 원본 재복사는 멱등 스킵)\n"
        "action='show'   다른 워크스페이스 내용 조회 (읽기전용 — query/tag/type/"
        "status 그대로 전달)\n"
        "from_dir= 는 세 액션 공통 — move/copy 는 원본 워크스페이스 지정(생략 시 cwd), "
        "show 는 조회 대상이라 필수.\n"
        "⚠️ 다건(2개 이상)은 기본이 미리보기만 — 안내된 local(confirm=<번호>) 로 실행 확정 (단건은 즉시 실행).\n"
        "cf. 서버 너머/팀 공유는 오픈박스(openbox 도구) — local() 은 서버를 안 건드림, 같은 "
        "디스크 안에서만 동작.\n"
        "⚠️ 같은 소유자 프로젝트끼리만 — 진짜 다른 사람/팀 소유면 파일 접근권이 있어도 "
        "local() 로 바로 쓰지 말고 openbox('push')(상대가 openbox('pull') 로 받는 리뷰 게이트)를 거칠 것.\n"
    ),

    "help": (
        "local — 같은 디스크의 다른 LinkLore 프로젝트 직접 조작 (move/copy/show)\n\n"
        "  local(action='move', id='lr-x'|'dc-x', to='/path')         이관 (단건 즉시)\n"
        "  local(action='move', id=[...], to='/path')                 이관 다건 → 미리보기+"
        "번호, local(confirm=<번호>) 로 확정\n"
        "  local(action='copy', id='lr-x', to='/path')                사본 생성 (원본 보존, 새 id)\n"
        "  local(action='show', from_dir='/other', query='...')       형제 워크스페이스 조회\n"
        "  local(action='move'|'copy', ..., from_dir='/src')          원본 워크스페이스 명시 — "
        "move/copy 공통 (기본 cwd)\n\n"
        "move: 보존 필드 = id·생성일·files·tags·level·status·body·items. 원본은 휴지통行"
        "(soft, restore(id) 로 복구 가능). 출처 기록(source_location='local'·원 프로젝트·원본 id).\n"
        "copy: move 와 동일 판정, 원본 삭제만 스킵. 새 id 발급 + 동일 출처 기록. 같은 원본 "
        "재복사는 source_id 대조로 멱등 스킵 — id 충돌 거부 없음.\n"
        "다건(len>1)은 미리보기+계획 등록만 — 실행은 안내된 local(confirm=<번호>) 단독 재호출"
        "(대량 실수 방지). 단건은 저위험이라 즉시 실행\n"
        "(단건 강제 미리보기는 지원 안 함 — 미리보기가 필요하면 다건으로 넘길 것).\n"
        "show: from_dir 필수. query/tag/type/status 를 그대로 대상 워크스페이스에 위임 — 검색 "
        "로직은 show() 와 동일.\n"
        "cross-workspace 링크(works/supersede/docLink)는 move/copy 둘 다 안 따라감 — 끊김 표시.\n"
        "대상 워크스페이스가 없으면(move/copy) 실행하지 않음 — 먼저 init(project_dir=...) 로 생성 "
        "(경계 생성은 init 전용, 자동 생성 없음).\n"
        "경계: 서버 너머/팀 공유는 오픈박스(openbox 도구) — local() 은 내 디스크 안에서만."
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
    "preview_confirm": "\n\n  1. 실행: local(confirm={slot})\n  2. 취소: 아무것도 안 함 (15분 후 소멸)",

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
    "moved_lore": '[{id}] "{title}" 이관됨 — id·생성일·files 보존, 출처 기록{warn}',
    "moved_doc": '[{id}] "{title}" 이관됨 — id·생성일·items 보존, 출처 기록{warn}',
    "copied_lore": '[{new_id}] "{title}" 복사됨 — 새 id (원본 {id}·생성일·files 보존), 출처 기록{warn}',
    "copied_doc": '[{new_id}] "{title}" 복사됨 — 새 id (원본 {id}·생성일·items 보존), 출처 기록{warn}',
    "preview_lore": '[{id}] "{title}" → 이관 예정 (생성일·files 보존){warn}',
    "preview_doc": '[{id}] "{title}" → 이관 예정 (생성일·items 보존){warn}',
    "preview_copy_lore": '[{id}] "{title}" → 복사 예정 (원본 보존, 새 id 발급·출처 기록){warn}',
    "preview_copy_doc": '[{id}] "{title}" → 복사 예정 (원본 보존, 새 id 발급·출처 기록){warn}',
}
