"""Korean (ko) messages for the 'schema' surface."""
MESSAGES: dict[str, str] = {
    "gen_too_new": (
        "이 저장소(.linklore)는 더 새로운 버전의 LinkLore가 만든 세대입니다 "
        "(저장소={db_gen}, 이 도구={code_gen}) — LinkLore 도구를 최신 버전으로 업데이트하세요."
    ),
    "gen_too_old": (
        "이 저장소(.linklore)는 구세대 스키마입니다 (저장소={db_gen}, 이 도구={code_gen}) "
        "— 업그레이드가 필요합니다. 자동 업그레이드 도구는 아직 없습니다 — "
        "report(msg='스키마 업그레이드 필요: 저장소={db_gen} 도구={code_gen}') 로 알려주세요 (report 는 이 게이트와 무관하게 항상 동작, 로그인 불요)."
    ),
}
