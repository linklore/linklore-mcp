"""Korean (ko) messages for the 'router_rm' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "rm — 본진 삭제 통일. 대상은 인자로 구분(action= 은 명시적 대안, 미지정 시 인자 존재로 자동판별). "
        "show/rm은 내 프로젝트 안에서만 논다 — 오픈박스(공유) 쪽 정리는 openbox 도구.\n\n"
        "## 항목 삭제 (lore/doc) — id 는 단건 또는 list (일괄)\n"
        "- **휴지통 (복구가능, 기본)**         → `rm(id)`  → restore(id) 로 복구\n"
        "- **영구 삭제 (복구 불가, 확인 필요)** → `rm(id, force=True)` → 안내된 `rm(confirm=N)` 재호출\n"
        "- **일괄 삭제**                       → `rm(id=['lr-x','dc-y'], force=True)`\n"
        "- **폐기 표시 (검색 시 보임)**        → `edit(id, status='dropped')`\n"
        "- **supersede (옛 보존 + 새 head)**  → `add(type='lore'|'doc', relates=old_id, ...)`\n\n"
        "## 보낸 발자취 내림 — 내 서버 전용 (push 역연산, 본진 안 건드림)\n"
        "- `rm(sent='lr-x'|'dc-x')`  내 서버에서 내림 (또는 action='sent' 명시)\n\n"
        "## 오픈박스 쪽은 여기 아님 (openbox 문패로 이동)\n"
        "- 공유 발자취 회수: openbox(action='rm', id=...) · 멤버 추방: openbox(action='rm', member=...) · "
        "통삭제: openbox(action='delete')\n"
    ),

    "restore_tool_desc": "restore(id) — 휴지통 lore·doc 복구. id 없으면 휴지통 목록.",

    "help": (
        "rm — 본진 삭제 통일 (대상은 인자로, action= 은 명시적 대안)\n"
        "show/rm은 내 프로젝트 안에서만 논다 — 오픈박스(공유) 쪽 정리는 openbox 도구.\n\n"
        "## 항목 (lore/doc) — action='' (기본)\n"
        "  휴지통 (복구가능, 기본)        → rm(id)  → restore(id) 복구\n"
        "  영구 삭제 (복구 불가, 확인 필요) → rm(id, force=True) → 안내된 rm(confirm=N) 재호출\n"
        "  폐기 표시 (검색 보임)          → edit(id, status='dropped')\n\n"
        "## 보낸 발자취 내림 — 내 서버 전용 (본진 안 건드림) — action='sent'\n"
        "  rm(sent='lr-x'|'dc-x')\n\n"
        "## 오픈박스 쪽 (여기 아님 — openbox 문패로 이동)\n"
        "  공유 발자취 회수 (보낸 본인만)   openbox(action='rm', id=...)\n"
        "  멤버 추방 (owner)               openbox(action='rm', member=...)\n"
        "  오픈박스 통삭제 (owner)          openbox(action='delete')\n\n"
        "action='sent' 는 sent= 존재만으로도 자동판별되는 기존 방식의 명시적\n"
        "대안(발견성) — 값 자체는 여전히 필요, action= 만 주면 안 됨.\n"
    ),

    "restore_help": (
        "restore — 휴지통(soft-deleted) 복구\n\n"
        "  restore()      → 휴지통 목록 (lore + doc)\n"
        "  restore(id)    → 해당 lore/doc 복구 (검색/관련후보 재등장)\n\n"
        "rm(id) = 휴지통 이동(기본), rm(id, force=True) = 영구삭제(확인 필요)."
    ),

    "err_action_invalid": "오류: action='{action}' 미지원 — 'sent' 만 (또는 미지정). 오픈박스 쪽 정리는 openbox 도구",
    "err_sent_required": "오류: action='sent' 는 sent=(id) 필수",

    "moved_rm_ids": (
        "이동됨: 오픈박스에서 공유 발자취 삭제는 rm이 아니라 openbox 도구입니다.\n"
        "  사용: openbox(name='{name}', action='rm', id={ids})\n"
        "  (rm(sent=) 은 내 서버 내림 전용 — show/rm은 내 프로젝트 안에서만 논다)"
    ),
    "moved_rm_member": (
        "이동됨: 오픈박스 멤버 추방은 rm이 아니라 openbox 도구입니다.\n"
        "  사용: openbox(name='{name}', action='rm', member='{member}')\n"
        "  (show/rm은 내 프로젝트 안에서만 논다)"
    ),
    "moved_delete": (
        "이동됨: 오픈박스 통삭제는 rm이 아니라 openbox 도구입니다. 아무것도 실행되지 않았습니다.\n"
        "  사용: openbox(name='{name}', action='delete')\n"
        "  (show/rm은 내 프로젝트 안에서만 논다)"
    ),
    "err_id_required": "오류: id를 지정하세요.",
    "err_not_rm_target": "오류: '{id}'는 rm 대상이 아닙니다. lore(lr-*), doc(dc-*)만 삭제 가능합니다.",

    "err_doc_not_found": "오류: doc '{id}'를 찾을 수 없습니다.",
    "doc_permanent_deleted": "[{id}]{ts} 영구 삭제됨 (복구 불가)",
    "doc_trashed": "[{id}]{ts} 휴지통으로 이동 — 복구: restore('{id}'), 영구삭제: rm('{id}', force=True)",

    "predecessor_revived": "전임자 [{id}]가 복권됨(대체본 삭제 — dropped로 검색에 표시)",


    "force_delete_desc": "영구 삭제 — [{id}] {title}",


    "force_delete_confirm": (
        "⚠️ [{id}] \"{title}\" 영구 삭제 준비 — 복구 불가. "
        "1. 실행: rm(confirm={slot}) · 2. 대신 휴지통으로: rm(id='{id}')  (15분 후 소멸)"
    ),

    "restore_listing_empty": "휴지통 비어있음.",
    "restore_listing_header": "# 휴지통 ({n}건) — restore(id) 로 복구",
    "restore_listing_line": "- [{id}] {title}  ({when})",
    "restore_not_trash": "[{id}] 이미 활성 상태 (휴지통 아님).",
    "restore_restored": "[{id}] 휴지통에서 복구됨",

    "err_sent_no_server": (
        "오류: 내 서버 없음 (push 한 적 없음).\n"
        "  먼저 push 로 서버에 올리세요 (자동으로 개인 서버 설정됨)."
    ),


    "err_openbox_unregistered_list": "오류: 오픈박스 '{space}' 미등록 — openbox(action='list') 로 확인",
    "space_delete_desc": "오픈박스 통삭제 — {space}",
    "space_delete_confirm": (
        "⚠️ 오픈박스 '{space}' 삭제 — 복구 불가.\n"
        "  · 그 공유공간의 모든 공유 발자취 + 멤버 접근이 영구 삭제됩니다.\n"
        "  · 각자 본진(로컬) 원본은 안전 — 공유 사본만 사라집니다.\n"
        "  1. 실행: openbox(confirm={slot})\n"
        "  2. 취소: 아무것도 안 함 (15분 후 소멸)"
    ),
    "err_openbox_delete_no_auth": "오류: 오픈박스 삭제 실패 — '{space}' 인증 정보 없음",
    "err_openbox_delete_failed": "오류: 오픈박스 삭제 실패 — {detail}",
    "space_deleted": "[{space}] 오픈박스 삭제됨 — 서버 내용물 cascade + 로컬 정리 (복구 불가)",

    "err_name_not_found": "오류: '{name}'를 찾을 수 없습니다. ID를 사용하세요.",
}
