"""Korean (ko) messages for the 'push_pull' surface."""
MESSAGES: dict[str, str] = {

    "err_unauthorized": "오류: 세션 만료(401) — 재인증 필요",
    "err_not_found_on_server": (
        "서버에 이 프로젝트가 없습니다 (지워졌거나 옮겨짐). "
        "로컬은 그대로입니다 — 올리려면 push()."
    ),
    "err_reauth_failed": "오류: 세션 만료(401) — 재인증 필요\n  다시 로그인: uvx llre login",
    "err_forbidden": (
        "오류: 내 서버 인증 거부(403) — 이 프로젝트의 iam이 그 서버의 소유자가 아닙니다.\n"
        "  확인: config(action='whoami') · 재로그인: uvx llre login"
    ),
    "err_snapshot_fetch_failed": "오류: backend snapshot fetch 실패 — {url}{cause}",
    "err_revoked": "오류: 서버 측 게시 철회됨 (410) — 복원할 데이터 없음",
    "err_no_identity": "오류: '{label}' 인증 정보 없음 — config(action='whoami')로 확인",
    "err_backend_unreachable": "backend 접근 실패 — {url}{cause}",


    "restore_header": "[{label}] pull {count}건 복원 (lore {lore} + doc {doc})",
    "restore_updated": "  갱신 {count}건 (서버본이 더 신선 — 로컬 교체)",
    "restore_skipped": "  skip {count}건 (로컬이 최신/동일)",
    "conflict_prefix": "  ⚠️ 충돌 {count}건 (마지막 push 이후 서버·로컬 양쪽 다 수정 — 로컬 유지): ",
    "conflict_more": " 외",
    "conflict_suffix": " · 로컬을 정본으로 확정하려면 push(id=...)",
    "not_found_header": "  서버에 없음 {count}건: {ids}",


    "push_desc": (
        "[my server] push(id) — 본진을 **내 서버**에 올림 (나만 봄). git push 처럼 로컬→서버.\n"
        "공유 아님 — 타인 공유(오픈박스)는 push 아니라 openbox(action='push')"
        " (push 는 설계상 타겟 인자가 없어 공유가 불가능).\n"
        "\n"
        "- push()            본진 전체 → 서버\n"
        "- push(id='lr-x'|'dc-x')   1건\n"
        "- push(id=['lr-x','dc-y'])  배치\n"
        "내리기(역연산): rm(sent='lr-x'|'dc-x') — 내 서버 사본만 내림, 본진 무변.\n"
        "(로컬 워크스페이스끼리 항목 이동은 push 아니라 local())\n"
    ),
    "push_help": (
        "[my server] push — 본진 → 내 서버 (나만 봄, git push 개념)\n"
        "\n"
        "  push()            본진 전체\n"
        "  push(id='lr-x'|'dc-x')   1건 / push(id=['lr-x','dc-y']) 배치\n"
        "  공유 아님 (오픈박스에 공유 = openbox(action='push')). 복원 = pull. 내 서버 내리기 = rm(sent='lr-x'|'dc-x').\n"
        "  (로컬 워크스페이스끼리 항목 이동은 push 아니라 local())"
    ),
    "auto_connect_new_push": "⚠️ 연결이 없어 자동 connect 했습니다 — 새 공간이 생성됨.\n",
    "auto_connect": "⚠️ 연결이 없어 자동 connect 했습니다.\n",
    "push_empty": "[{label}] 본진 비어있음 — 올릴 항목 없음",
    "push_up_to_date": "[{label}] 이미 최신 — push할 변경 없음",
    "err_reconnect_failed": "오류: 서버에 프로젝트가 없어 재연결을 시도했으나 실패했습니다.\n",
    "err_reconnect_retry_failed": "오류: 서버에 프로젝트가 없어 새로 연결했으나 재시도도 실패(404)했습니다.",
    "healed_new_space": "⚠️ 서버에 없어 새 공간에 올렸습니다.\n",
    "reauth_success": "⚠️ 세션이 만료되어 재인증했습니다.\n",


    "push_result_header": "[{label}] {verb} {count}건 (lore {lore} + doc {doc})",
    "push_not_found_header": "  본진에 없음 {count}건: {ids}",
    "push_errors_header": "  실패 {count}건:",
    "unpush_header": "[{label}] {verb} {count}건",
    "unpush_unknown_header": "  id prefix 불명(lr-/dc-) {count}건: {ids}",
    "unpush_errors_header": "  실패 {count}건:",
    "unpush_404_openbox_hint": (
        "  → '{id}'이(가) 오픈박스에만 있다면: openbox(action='rm', id='{id}')로 시도하세요"
    ),


    "pull_desc": (
        "[my server] pull(id) — 내 서버에서 본진 복원 (다른 기기서도). git pull 처럼 서버→로컬.\n"
        "오픈박스(공유)에서 가져오기는 pull 아니라 openbox(action='pull') — pull 은 내 서버 전용.\n"
        "로컬이 최신/동일이면 skip, 양쪽 다 수정된 진짜 충돌은 별도 표시(로컬 유지).\n"
        "\n"
        "- pull()            내 서버 전체 → 본진\n"
        "- pull(id='lr-x'|'dc-x')   선택 복원\n"
        "(로컬 워크스페이스끼리 항목 이동은 pull 아니라 local())\n"
    ),
    "pull_help": (
        "[my server] pull — 내 서버 → 본진 복원 (git pull 개념)\n"
        "\n"
        "  pull()            전체 / pull(id='lr-x'|'dc-x') 선택\n"
        "  충돌: 로컬이 최신/동일이면 skip (overwrite 안 함).\n"
        "  양쪽 다 수정된 진짜 충돌은 별도 ⚠️ 표시(로컬 유지) — 확정하려면 push(id=...).\n"
        "  오픈박스 발자취 가져오기 = openbox(action='pull').\n"
        "  (로컬 워크스페이스끼리 항목 이동은 pull 아니라 local())"
    ),
    "auto_connect_new_pull": (
        "⚠️ 연결이 없어 자동 connect 했습니다 — 새 공간이 생성됨"
        " (서버에 복원할 데이터가 없을 수 있음).\n"
    ),


    "backup_nudge": "(내 서버 개인 백업 — 오픈박스 공유는 openbox(action='push'))",
}
