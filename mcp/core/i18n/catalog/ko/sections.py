"""Korean (ko) messages for the 'sections' surface."""
MESSAGES: dict[str, str] = {

    "ambiguous": "모호 — 후보: [{candidates}]. 더 구체적으로.",


    "not_found": "섹션 없음 — 사용 가능한 섹션: [{sections}]. 새 섹션 추가는 edit(id, action='append').",


    "not_found_no_headings": (
        "섹션 없음 — 이 문서엔 섹션 헤딩이 없습니다. 새 섹션 추가는 edit(id, action='append')."
    ),


    "not_found_read": (
        "섹션 없음 — 사용 가능한 섹션: [{sections}]. 전문을 보려면 show(query='<id>')."
    ),
    "not_found_no_headings_read": (
        "섹션 없음 — 이 항목엔 섹션 헤딩이 없습니다. 전문을 보려면 show(query='<id>')."
    ),
}
