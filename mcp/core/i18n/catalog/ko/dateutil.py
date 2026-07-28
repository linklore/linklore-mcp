"""Korean (ko) messages for the 'dateutil' surface."""
MESSAGES: dict[str, str] = {

    "err_period_int_ambiguous": (
        "period 정수는 단위 모호 — '{value}d'(최근 {value}일) 또는 "
        "'{value}h'(최근 {value}시간)처럼 단위 명시"
    ),

    "err_period_range_format": "period 날짜 형식 인식 실패 — 'YYYY-MM-DD..YYYY-MM-DD' 형식 필요: {value}",

    "err_period_format_unrecognized": "period 형식 인식 실패 — 'Nh'(시간)|'Nd'(일)|'YYYY-MM-DD' 필요: {value}",
}
