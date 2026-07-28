"""Korean (ko) messages for the 'openbox' surface."""
MESSAGES: dict[str, str] = {
    "identity_birth_warning": (
        "⚠️ 프로젝트 iam 탄생 — 이후 이 프로젝트의 서버 백업·공유는 이 iam 소유가 됩니다.\n"
        "  저장: remote/iam.json\n"
    ),


    "identity_cleared_warning": (
        "⚠️ 프로젝트 iam 정리됨 — 이 박스에서 발급된 iam이었습니다. 이후 이 프로젝트는 계정으로 행동합니다.\n"
    ),
    "err_openbox_not_registered": (
        "오류: 오픈박스 '{who}' 미등록.\n"
        "  생성: openbox(name='{name_label}', action='new', display_name='나')\n"
        "  가입: openbox(action='join', code='<초대코드>', display_name='나')\n"
        "  기존 멤버십 배선: openbox(name='{name_label}', action='docking')"
    ),
    "err_member_id_required": "오류: member= 필수 (닉네임 또는 이메일) — 멤버 확인: openbox(name='{ob}', action='list')",
    "member_not_found": "오류: '{ref}' 멤버를 찾을 수 없음 — 멤버 확인: openbox(name='{ob}', action='list')",
    "member_hint_close": "\n  혹시: {items}",
    "member_ambiguous_header": "오류: '{ref}' 닉네임이 여러 멤버와 일치 — 어느 멤버인가요? (자동 선택 안 함)",
    "member_ambiguous_item": "  {n}. {display} ({role}) {detail} → {cmd}",
    "candidates_more": "  … 외 {n}건",
    "name_auto_placeholder": "(자동)",
    "name_placeholder": "이름",
    "openbox_name_placeholder": "<오픈박스명>",


    "list_boxes_empty": (
        "등록된 오픈박스 없음 — 생성: openbox(name='<이름>', action='new', display_name='나') · "
        "가입: openbox(action='join', code='<초대코드>', display_name='나')"
    ),
    "list_boxes_header": "등록된 오픈박스 {count}개:",
    "list_boxes_hint": "액션 지정: openbox(name='<박스>', action='docking'|'show'|'list'|...) · 전체 사용법: help=True",


    "init_help": (
        "openbox(name='<이름>', action='new', display_name='나')\n"
        "  새 오픈박스 생성 — 본인이 owner.\n"
        "  - name: 박스 이름 (서버 project name 그대로 등록 — 로컬 별칭 없음)\n"
        "  - display_name: 본인 멤버명 (다른 멤버에게 보임)\n"
        "  접근 = 멤버십 (초대제) — 공개/비공개 플래그 없음.\n"
        "  결과: backend project_id + owner 등록 → remote/openbox/openbox.json"
    ),
    "err_name_required": "오류: name 필수",
    "err_display_name_required": "오류: display_name 필수",
    "init_err_backend_failed": "오류: backend init 실패 ({code}) — {resp}",
    "init_success": (
        "[{name}] 오픈박스 생성 — owner={display_name}\n"
        "  project_id: {pid}\n"
        "  접근: 멤버십 (초대제)\n"
        "다음: openbox(name='{name}', action='invite') 로 멤버 초대"
    ),


    "edit_err_no_fields": (
        "오류: action='edit' 은 description=/title=/display_name= 중 최소 하나 필요 — "
        "지원 필드: description(박스 설명, owner/member) · title(박스명, owner 전용) · "
        "display_name(내 닉네임, 누구나)\n"
        "  예: openbox(name='{name}', action='edit', description='...')"
    ),
    "edit_err_failed": "오류: 수정 실패 ({code}) — {resp}",
    "edit_done": "[{name}] description 변경 완료 — \"{description}\"",
    "edit_title_done": "[{name}] 박스명 변경 완료 — \"{title}\"",
    "edit_title_err_forbidden": "오류: 박스명(title) 변경은 owner만 가능 — docking/이 서버가 매칭하는 정체성이라 소유자 단독 게이트",
    "edit_display_name_done": "[{name}] 내 닉네임 변경 완료 — \"{display_name}\"",
    "edit_display_name_err_conflict": "오류: 닉네임 '{display_name}' 은(는) [{name}]에서 이미 사용 중 — 다른 닉네임으로 재시도",


    "invite_help": (
        "openbox(name='<박스>', action='invite', role='member', kind='member', expires_h=24)\n"
        "  초대 코드 발급. owner 만 가능.\n"
        "  - role='owner' 도 가능 (transfer 우선 권장)\n"
        "  - kind='project' — 프로젝트 멤버 초대 (상대 repo가 join)\n"
        "  - member='<닉네임>' — 재발급 초대(기존 프로젝트 iam 대상, 세션 회전)\n"
        "  - 기본 24h, 1회 사용"
    ),
    "invite_err_bad_role": "오류: role = viewer / member / owner 중 하나 (받음: '{role}')",
    "invite_err_bad_kind": "오류: kind = member / project 중 하나 (받음: '{kind}')",
    "invite_err_failed": "오류: invite 실패 ({code}) — {resp}",
    "invite_join_hint_reissue": "재발급 초대 — 프로젝트에서 openbox(action='join', code='{code}') 로 설치",
    "invite_join_hint_project": "상대 프로젝트에서: openbox(action='join', code='{code}', display_name='<프로젝트명>')",
    "invite_join_hint_member": "공유: 멤버에게 invite_code 전달 → openbox(action='join', code='{code}', display_name='...')",
    "invite_issued_header": "[{name}] invite 발급{suffix}\n",
    "invite_project_suffix": " (프로젝트 멤버)",
    "invite_owner_role_warning": (
        "⚠️ owner 권한 초대 — 이 코드가 소비되면 owner 권한이 즉시 부여됩니다(transfer 우선 권장).\n"
    ),


    "openbox_join_help": (
        "openbox(action='join', code='<초대코드>', display_name='나')\n"
        "  초대 코드로 오픈박스 가입.\n"
        "  - iam(env>프로젝트 iam>계정)으로 인증 — 박스별 토큰 없음\n"
        "  - kind='project' 초대 소비 시 이 프로젝트에 iam 탄생 가능(loud 경고)\n"
        "  - 박스 이름은 backend project name 그대로 등록 (로컬 별칭 없음)"
    ),
    "err_invite_code_required": "오류: code 필수 (초대 코드)",
    "err_invite_login_required": (
        "오류: 이 초대는 로그인이 필요합니다 — 브라우저 로그인을 시도했지만 완료되지 않았습니다.\n"
        "  다시 시도하거나: uvx llre login"
    ),
    "err_auth_url_hint": "\n  브라우저가 안 열리면 직접 열기: {url}",
    "join_err_409": "오류: join 실패 (409) — {resp}",
    "join_err_generic": "오류: join 실패 ({code}) — {resp}",
    "openbox_join_success": (
        "[{project_name}] 오픈박스 가입 — {display_name} ({role})\n"
        "  project_id: {pid}\n"
        "다음: openbox(name='{project_name}', action='show') 로 박스 훑기\n"
        "  흡수: openbox(name='{project_name}', action='pull', id='...')"
    ),


    "list_help": (
        "openbox(name='<박스>', action='list') — 멤버 목록: 닉네임 + (사람이면) 이메일 + 역할 + last_push_at.\n"
        "  멤버 지칭은 닉네임/이메일 그대로 — openbox(action='role'/'transfer'/'rm') 의 member= 에 사용."
    ),
    "list_err_failed": "오류: list 실패 ({code}) — {resp}",
    "list_header": "[{name}]  ({count} 멤버)",
    "list_project_tag": " [프로젝트]",


    "rm_member_help": (
        "openbox(name='<박스>', action='rm', member='<닉네임 또는 이메일>')\n"
        "  owner 가 멤버 추방. token revoke. 2단계 확인\n"
        "  (1차 응답이 주는 번호를 openbox(confirm=<번호>) 단독으로 재호출하면 실행).\n"
        "  추방된 멤버의 lore 데이터는 박스에 그대로 남음 (a 옵션).\n"
        "  member= 는 리스트도 허용(벌크) — 건별 결과 따로 보고, 부분 실패해도 전체 롤백 아님."
    ),
    "rm_member_desc": "멤버 추방 — {name}: {members}",
    "rm_member_confirm": (
        "⚠️ [{name}] 멤버 추방: {members} — token revoke(lore 데이터는 잔존).\n"
        "  1. 실행: openbox(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),
    "remove_err_failed": "오류: 멤버 제거 실패 ({code}) — {resp}",
    "remove_done": "[{name}] 멤버 {member_id} 추방 — token revoke. lore 데이터는 잔존.",


    "role_help": (
        "openbox(name='<박스>', action='role', member='<닉네임 또는 이메일>', role='viewer')\n"
        "  owner 가 멤버 역할 변경 — role='viewer'(읽기 전용) | 'member'(읽기·쓰기).\n"
        "  owner 지정 불가(이전은 transfer). 자기/owner 대상 불가."
    ),
    "role_err_bad_value": "오류: role = 'viewer'(읽기 전용) 또는 'member'(읽기·쓰기)",
    "role_err_failed": "오류: role 변경 실패 ({code}) — {resp}",
    "role_label_viewer": "뷰어(읽기 전용)",
    "role_label_member": "멤버(읽기·쓰기)",
    "role_changed": "[{name}] 멤버 {member_id} → {label}",


    "docking_help": (
        "openbox(name='team-prj', action='docking')\n"
        "  이미 멤버인 오픈박스를 **이름으로** 이 프로젝트에 배선 — 박스는 docking 된 프로젝트에서만 보임.\n"
        "  - 계정 토큰으로 내 멤버십 목록을 조회해 이름 매칭 → 그 이름 그대로 배선(로컬 별칭 없음)\n"
        "  - 동명 박스가 2개 이상이면 후보(이름·prj-id·멤버수)를 보여주고 멈춤 — project_id='prj-xxxxxxxx' 로 확정\n"
        "  - 인증 = 계정 iam (login). 토큰 저장 안 함. url= 은 은퇴됨.\n"
        "  - project-kind 는 docking 불가 (프로젝트 iam 은 join 으로 탄생한 프로젝트에 바인딩).\n"
        "  - 첫 가입(초대코드)은 openbox(action='join', code=). 배선 해제: openbox(name='<이름>', action='undocking')."
    ),
    "docking_err_url_retired": (
        "오류: url= 은 은퇴했습니다 — docking 은 이제 박스 **이름**으로 합니다:\n"
        "  openbox(name='{name}', action='docking')\n"
        "  동명 박스가 여럿이면 후보와 함께 project_id='prj-xxxxxxxx' 확정 명령을 안내합니다."
    ),
    "docking_nudge_pid_looks_name": (
        "'{value}' — project_id= 자리에 이름 형태가 왔습니다 (prj-xxxxxxxx 또는 풀 UUID 가 아님). 이거 맞나요?\n"
        "  1. 이 이름으로 배선: {cmd}\n"
        "  2. prj-id 로 지정하려면 먼저 확인: config(action='projects') 또는 config(action='sources')"
    ),
    "docking_nudge_name_looks_prj": (
        "'{name}' — name= 자리에 prj-id 형태가 왔습니다. 이거 맞나요? (자동 실행 안 함)\n"
        "  1. 이 id 로 배선: {cmd}\n"
        "  2. 이 문자열이 진짜 박스 이름이면: {results}"
    ),
    "docking_nudge_name_results": "내 멤버십에 같은 이름 {count}건 — openbox(action='docking', name=...) 그대로 재호출해도 이름으로 처리되지 않으니 위 1번을 쓰세요",
    "docking_nudge_name_no_results": "내 멤버십에 이 이름의 박스 없음",
    "docking_err_ref_not_found": "오류: '{ref}' 에 해당하는 프로젝트 없음 — 주소록·내 멤버십에서 못 찾음. 확인: config(action='projects')",
    "docking_ref_ambiguous_header": "오류: '{ref}' 가 여러 프로젝트와 일치 — 어느 것인가요? (자동 선택 안 함)",
    "docking_candidate_ref_item": "  {n}. {label} ({prj}) → {cmd}",
    "docking_err_name_not_found": "오류: 내 멤버십에 '{name}' 이름의 박스 없음 — 초대코드가 있으면 openbox(action='join', code='...')",
    "docking_hint_close_names": "\n  혹시: {items}",
    "docking_err_name_not_box": "오류: '{name}' 은(는) 오픈박스가 아닙니다 (개인 공간) — 개인 백업은 push()/pull() (docking 불필요)",
    "docking_ambiguous_header": "'{name}' 이름의 박스가 {count}개 — 어느 박스인가요? (자동 배선 안 함)",
    "docking_ambiguous_item": "  {n}. {name} ({prj}) 멤버 {count}명 → {cmd}",
    "docking_err_project_kind": (
        "오류: project-kind iam은 docking 불가 — 이 프로젝트는 프로젝트 iam"
        "(remote/iam.json)으로 행동 중이고, iam 은 join 으로 탄생한 박스에 바인딩됩니다.\n"
        "  이 박스가 필요하면: owner 에게 kind='project' 초대를 요청 → "
        "openbox(action='join', code='...', display_name='...')"
    ),
    "docking_err_no_url": "오류: url 필수 (오픈박스 주소 https://.../api/projects/<project_id>)",
    "docking_err_bad_url": "오류: url 은 백엔드 오픈박스 주소여야 합니다 (예: https://api.linklore.io/api/projects/<pid>)",
    "docking_err_login_required": "오류: 로그인 필요 — `uvx llre login` 후 재시도 (docking 은 계정 iam으로 인증)",
    "docking_err_connect_failed": "오류: 오픈박스 접속 실패 ({body}) — 주소/네트워크 확인",
    "docking_err_not_member": (
        "오류: 이 오픈박스 멤버가 아님 (또는 토큰 만료).\n"
        "  초대코드가 있으면 openbox(action='join', code='...').\n"
        "  로그인 만료면 `uvx llre login`."
    ),
    "docking_err_not_found": "오류: 오픈박스를 찾을 수 없음 — URL 의 project_id 확인",
    "docking_err_unexpected": "오류: 예상치 못한 응답 ({status}) — {body}",
    "err_generic": "오류: {error}",


    "register_err_url_not_ascii": (
        "오류: url 에 비ASCII 문자가 있음 — 박스 주소를 그대로 복사해 다시 시도\n"
        "  (백엔드 주소는 ASCII 전용, 예: https://api.linklore.io/api/projects/<pid>)"
    ),
    "register_err_alias_taken": (
        "오류: 이름 '{name}' 은(는) 이미 다른 박스({pid})에 배선되어 있음 —\n"
        "  다른 이름을 쓰거나 먼저 배선 해제: openbox(name='{name}', action='undocking')"
    ),
    "docking_success": (
        "[{name}] docking — {prj} (멤버 {count}명)\n"
        "  인증: 계정 iam (토큰 저장 안 함, 멤버십 확인됨)\n"
        "  훑기: openbox(name='{name}', action='show', query='...') · 흡수: openbox(name='{name}', action='pull', id='...')"
    ),


    "docking_rewired": (
        "⚠️ 이 박스는 이미 '{old}' 이름으로 배선돼 있었습니다 — 이제 '{new}'로 갱신됩니다.\n"
    ),


    "undocking_help": (
        "openbox(name='<이름>', action='undocking')\n"
        "  이 프로젝트의 주소록 배선만 제거 — 서버 멤버십은 그대로 (탈퇴는 openbox(name='<이름>', action='leave')).\n"
        "  docking/join 이 남긴 로컬 등록(registry.json·openbox.json)을 함께 정리."
    ),
    "undocking_done": (
        "[{name}] undocking 완료 — 이 프로젝트의 배선 제거 (서버 멤버십 무변).\n"
        "  탈퇴가 목적이면: openbox(name='{name}', action='leave')"
    ),


    "transfer_help": (
        "openbox(name='<박스>', action='transfer', member='<새 owner 닉네임 또는 이메일>')\n"
        "  owner 권한 이전. 본인은 member 로 강등. 2단계 확인\n"
        "  (1차 응답이 주는 번호를 openbox(confirm=<번호>) 단독으로 재호출하면 실행)."
    ),
    "transfer_desc": "owner 이전 — {name} → {member}",
    "transfer_confirm": (
        "⚠️ [{name}] owner를 {member_id}로 이전 — 본인은 member로 강등되고 되돌리려면\n"
        "  새 owner가 다시 이전해야 합니다.\n"
        "  1. 실행: openbox(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),
    "transfer_err_failed": "오류: transfer 실패 ({code}) — {resp}",
    "transfer_done": "[{name}] owner → member ({member_id})\n  본인은 이제 member.",


    "leave_help": (
        "openbox(name='<박스>', action='leave')\n"
        "  본인이 오픈박스에서 탈퇴 — 멤버십 삭제 + 로컬 등록 정리(join 의 역연산).\n"
        "  owner 는 탈퇴 불가 — 먼저 openbox(name='<박스>', action='transfer', member='<id>') 로 소유권 이전.\n"
        "  배선만 풀려면(멤버십 유지): openbox(name='<박스>', action='undocking')."
    ),
    "leave_desc": "탈퇴 — {name}",
    "leave_confirm": (
        "⚠️ '{name}' 오픈박스에서 나가시겠어요? 재초대 전엔 되돌릴 수 없습니다.\n"
        "  1. 실행: openbox(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),
    "leave_confirm_owner_hint": (
        "⚠️ '{name}' 오픈박스에서 나가시겠어요? 재초대 전엔 되돌릴 수 없습니다.\n"
        "  ℹ️ 로컬 기록상 당신이 이 박스의 owner로 보입니다 — 맞다면 서버가 거부합니다(owner 탈퇴 불가,\n"
        "     이미 이전했다면 로컬 기록이 오래된 것일 수 있으니 무시하세요).\n"
        "  1. 그래도 시도: openbox(confirm={slot})\n"
        "  2. 대안(owner라면 이게 정답): openbox(name='{name}', action='transfer', member='<새 owner 닉네임>')"
    ),
    "leave_err_owner_409": (
        "오류: '{name}' owner 는 탈퇴할 수 없습니다 — 먼저 소유권을 이전하세요:\n"
        "  openbox(name='{name}', action='transfer', member='<새 owner 닉네임>')"
    ),
    "leave_err_not_member": "오류: '{name}' 멤버가 아닙니다 — openbox(name='{name}', action='list') 로 확인",
    "leave_err_failed": "오류: leave 실패 ({code}) — {resp}",
    "leave_done": "[{name}] 탈퇴 완료 — 로컬 등록 정리됨.",


    "err_name_required_target": "오류: name= 필수 — 대상 오픈박스 이름 (예: openbox(name='team-prj', action='{action}', ...))",
    "push_err_no_id": "오류: id= 필수 — 공유할 발자취 (예: id='lr-x' 또는 id=['lr-a', 'dc-b'])",
    "push_verb": "push(공유)",
    "push_preview_header": "[{name}] push 미리보기 — {count}건 (아직 전송 안 됨)",
    "push_preview_missing": "  ⚠️ 본진에 없음: {ids}",
    "push_desc": "push {count}건 — {name}",
    "push_preview_confirm": "  1. 실행: openbox(confirm={slot})\n  2. 취소: 아무것도 안 함 (15분 후 소멸)",
    "pull_err_no_id": "오류: id= 필수 — 가져올 발자취 id. 훑기·캐시 갱신만은 openbox(name='{name}', action='show')",
    "pull_header": "[{name}] pull {count}건 — 본진에 새 id 로 흡수 (출처 메타 유지)",
    "pull_more": "  ... 외 {count}건",
    "pull_errors_header": "  실패 {count}건:",
    "rm_ids_err_no_id": "오류: id= 필수 — 오픈박스에서 삭제할 발자취 id (내가 이 박스에 공유했던 것)",
    "rm_ids_verb": "오픈박스에서 삭제",
    "show_refresh_failed": "⚠️ 캐시 갱신 실패 — 마지막 캐시로 표시 ({cause})",

    "show_with_docs": "{lore_part}\n\n{doc_part}",


    "rm_err_no_args": "오류: id= 또는 member= 필수 — id= 는 공유한 것 회수, member= 는 멤버 제거 (정확히 하나)",
    "rm_err_both_args": "오류: id= 와 member= 를 동시에 줄 수 없음 — id= 는 공유한 것 회수, member= 는 멤버 제거 (정확히 하나)",


    "tool_desc": (
        "openbox(name, action) — 소유자 벽: 다른 소유자와의 교류(공유·가져오기·멤버십)는 전부 이 문패 하나로. "
        "오픈박스 = 초대제 공유 박스. 내 서버 백업은 push()/pull() (타깃 인자 없음 — 벽 안 넘음).\n"
        "\n"
        "운반:\n"
        "- openbox(name='team-prj', action='push', id='lr-x')     발자취를 박스에 공유 — 사본 전송, 본진 무변. 다건(id 2+)은 미리보기 후 confirm=True 재호출\n"
        "- openbox(name='team-prj', action='pull', id='lr-x')     박스의 발자취를 본진에 흡수 — 새 id + 출처 메타\n"
        "- openbox(name='team-prj', action='rm', id='lr-x')       내가 공유한 발자취를 박스에서 삭제 (본진 무변)\n"
        "조회:\n"
        "- openbox(name='team-prj', action='show', query='인증')   박스 훑기 — 호출 시 캐시 자동 갱신 (필터: query·tag·max·oneline)\n"
        "거버넌스:\n"
        "- openbox(name='team-prj', action='new', display_name='나')         박스 생성 (나=owner)\n"
        "- openbox(name='team-prj', action='edit', description='...')        박스 설명 수정 (owner/member) · title=박스명(owner 전용) · display_name=내 닉네임(누구나)\n"
        "- openbox(name='team-prj', action='invite', role='member')          초대 코드 (owner). kind='project'=프로젝트 멤버, member='<닉네임>'=재발급\n"
        "- openbox(action='join', code='X', display_name='나')  초대 코드로 가입 (박스 이름은 서버 project name 그대로)\n"
        "- openbox(name='team-prj', action='docking')                        멤버십을 이름으로 이 프로젝트에 배선 — 동명 2+는 후보+project_id='prj-...' 확정. project-kind는 docking 불가\n"
        "- openbox(name='team-prj', action='undocking')                      이 프로젝트의 배선만 제거 — 서버 멤버십 무변 (탈퇴는 leave)\n"
        "- 'list' 멤버 목록 · 'role' member=+role= · 'transfer' member= (2회 확인) · 'leave' (2회 확인) · 'rm' member='<닉네임/이메일>' 로 멤버 추방(owner) · 'delete' 통째 삭제 (owner, 2회 확인)\n"
        "(멤버 지칭 member= 는 닉네임 또는 이메일 — id 없음. 액션 문법: 지속 연결 절차형=-ing(docking/undocking), 즉발형=동사원형. rm(id=)=공유 회수, rm(member=)=멤버 추방 — 정확히 하나)\n"
    ),
    "help": (
        "openbox(name, action) — 소유자 벽 (오픈박스 = 초대제 공유 박스)\n"
        "운반·조회:\n"
        "  push      openbox(name='team-prj', action='push', id='lr-x')             박스에 공유 (사본, 본진 무변; 다건은 미리보기→confirm=True)\n"
        "  pull      openbox(name='team-prj', action='pull', id='lr-x')             본진에 흡수 (새 id + 출처 메타)\n"
        "  rm        openbox(name='team-prj', action='rm', id='lr-x')               공유한 것 삭제 — 또는 action='rm', member='<닉네임/이메일>' 로 멤버 추방(owner). id=/member= 중 정확히 하나\n"
        "  show      openbox(name='team-prj', action='show', query='인증')           훑기 (캐시 자동 갱신; 필터 query·tag·max·oneline)\n"
        "거버넌스:\n"
        "  new       openbox(name='team-prj', action='new', display_name='나')       박스 생성 (나=owner)\n"
        "  edit      openbox(name='team-prj', action='edit', description='...')      설명 수정 (owner/member) · title=박스명(owner 전용) · display_name=내 닉네임(누구나)\n"
        "  invite    openbox(name='team-prj', action='invite', role='member')        초대 코드 (kind='project'=프로젝트 멤버, member=재발급)\n"
        "  join      openbox(action='join', code='X', display_name='나')  가입 (박스 이름은 서버 project name 그대로)\n"
        "  docking   openbox(name='team-prj', action='docking')                      기존 멤버십을 이름으로 배선 (동명 2+는 project_id='prj-...' 확정, project-kind 불가)\n"
        "  undocking openbox(name='team-prj', action='undocking')                    배선만 제거 (서버 멤버십 무변 — 탈퇴는 leave)\n"
        "  list      openbox(name='team-prj', action='list')                         멤버 목록 (닉네임·이메일·역할)\n"
        "  role      openbox(name='team-prj', action='role', member='<닉네임>', role='viewer')  역할 변경\n"
        "  transfer  openbox(name='team-prj', action='transfer', member='<닉네임>')   owner 이전 (2회 확인)\n"
        "  leave     openbox(name='team-prj', action='leave')                        본인 탈퇴 (owner 는 409 — transfer 먼저)\n"
        "  delete    openbox(name='team-prj', action='delete')                       박스 통째 삭제 (owner, 2회 확인)\n"
        "내 서버(백업)는 push()/pull() — 벽 안 넘음. 내 서버에서 내림은 rm(sent=)."
    ),
    "err_invalid_action": "오류: action = {valid} 중 하나. help=True 로 사용법.",
    "err_param_not_allowed": (
        "오류: {params} — '{action}' 액션 파라미터가 아님 (silent 무시 안 함).\n"
        "  '{action}' 허용: {allowed}. help=True 로 사용법."
    ),
    "err_name_looks_like_action": (
        "오류: '{name}' 이 name=(박스 이름) 자리에 들어왔습니다 — 액션은 두 번째 인자:\n"
        "  openbox(name='<박스이름>', action='{name}', ...)\n"
        "  이름이 필요 없는 액션(join)은 openbox(action='{name}', ...)."
    ),
}
