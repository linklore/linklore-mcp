"""Korean (ko) messages for the 'app' surface."""
MESSAGES: dict[str, str] = {


    "instructions": (
        "에이전트를 위한 AI-native 구조화 메모리 — lore(결정·함정·저널)와 doc(스펙·계획)을 "
        "직접 읽고 쓰며, 코드 파일과 연결됩니다. "
        "사람이 아니라 에이전트를 위해 만들어졌습니다 — 모든 도구는 사람이 읽기 좋으라고가 "
        "아니라, AI가 실제로 잘 쓸 수 있도록 설계되었습니다. "
        "매 세션 시작 시 brief()를 먼저 호출해 "
        "미결 항목과 최근 활동을 확인하세요. 아직 설정 전이면 init()을 호출하세요. "
        "전체 가이드: show(tag='guide')."
    ),

    "err_generic": "오류: {name} 실패 — {err_type}: {err_msg}{hint}",


    "hint_str_attr": "\n💡 인자가 string인데 list/dict 처리 시도. list 형식 확인 (예: tags=['a','b'])",
    "hint_list_attr": "\n💡 인자가 list인데 string 처리 시도. 도구 docstring 확인 (help=True)",
    "hint_arg_shape": "\n💡 인자 형식 또는 누락. 도구 docstring 확인 (help=True)",
    "hint_keychain": "\n💡 uvx llre login 재실행 또는 Keychain 접근 허용",

    "err_empty_response": (
        "⚠️ 내부 오류: {name}이 빈 응답을 반환했습니다 "
        "(도구 버그 — report(msg='{name} 빈 응답: <재현 인자>') 로 신고해 주세요)"
    ),
}
