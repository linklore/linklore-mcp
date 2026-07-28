"""English (en) messages for the 'dateutil' surface."""
MESSAGES: dict[str, str] = {

    "err_period_int_ambiguous": (
        "period integers are ambiguous about the unit — spell it out like "
        "'{value}d' (last {value} days) or '{value}h' (last {value} hours)"
    ),

    "err_period_range_format": "period date format not recognized — expected 'YYYY-MM-DD..YYYY-MM-DD': {value}",

    "err_period_format_unrecognized": "period format not recognized — expected 'Nh'(hours)|'Nd'(days)|'YYYY-MM-DD': {value}",
}
