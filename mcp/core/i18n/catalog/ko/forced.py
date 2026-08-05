"""Korean (ko) messages for the 'forced' surface."""
MESSAGES: dict[str, str] = {
    "help": (
        "forced — rm()/local_cross()/config()/openbox() 가 낸 파괴적 동작 경고를 "
        "실행하는 유일한 통로. 경고문에 적힌 값을 그대로 옮겨 쓸 것 — 스스로 판단해서 "
        "부르지 말 것.\n\n"
        "action='rm'           id=<지울 항목(들)>\n"
        "  → rm(force=True) 경고에 실린 id 를 그대로.\n\n"
        "action='local_cross'  mode='move'|'copy', id=<항목(들)>, to=<대상 경로>, from_dir=<원본 경로>\n"
        "  → local_cross() 다건 경고에 실린 값을 그대로. mode= 는 local_cross() 자신의 "
        "action= 을 개명한 것(forced 자신의 action= 과 이름 충돌 방지).\n\n"
        "action='config'       delete_project=<prj_id>  또는  sessions_revoke_all=True\n"
        "  → config() 경고에 실린 값을 그대로. 둘 중 정확히 하나만.\n\n"
        "action='openbox'      delete=<pid> | leave=<pid> | transfer=<member id>(+pid=) | "
        "rm_member=<member id(들)>(+pid=) | push=<item id(들)>(+pid=, name=선택)\n"
        "  → openbox() 경고에 실린 값을 그대로. 다섯 중 정확히 하나만 — transfer=/"
        "rm_member=/push= 는 대상 박스를 지칭하는 pid= 도 함께 필요(delete=/leave= 는 "
        "그 값 자체가 pid라 불필요).\n\n"
        "9개 조합:\n"
        "  rm            id=\n"
        "  local_cross   mode= id= to= from_dir=\n"
        "  config        delete_project=\n"
        "  config        sessions_revoke_all=True\n"
        "  openbox       delete=\n"
        "  openbox       leave=\n"
        "  openbox       transfer= pid=\n"
        "  openbox       rm_member= pid=\n"
        "  openbox       push= pid= (name=선택)"
    ),
    "err_action_invalid": "오류: action='{action}' 미지원 — {valid} 중 하나",
    "err_fields_missing": "오류: 어떤 동작인지 특정 안 됨 — {action}의 유효 필드: {fields}",
    "err_pid_required": "오류: action='openbox', {field}= 에는 pid=(대상 박스) 도 필요합니다",
    "err_box_not_found": "오류: pid='{pid}' 에 해당하는 박스를 주소록에서 찾을 수 없음 — 경고가 뜬 사이 등록이 해제됐을 수 있습니다",
}
