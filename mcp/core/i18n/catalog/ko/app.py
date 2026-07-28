"""Korean (ko) messages for the 'app' surface."""
MESSAGES: dict[str, str] = {

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
