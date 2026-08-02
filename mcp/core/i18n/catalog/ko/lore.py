"""Korean (ko) messages for the 'lore' surface."""
MESSAGES: dict[str, str] = {

    "doc_hint_header": "\n관련 doc 후보 (제안 · 연결 안 됨 — 엮으려면 link()):",


    "sem_label": " (의미 유사 {cosine})",


    "weak_candidates": "  약한 후보 {n}건 — 겹침은 cleanup()으로 확인",


    "connected_line": "연결: {labels}",

    "auto_tags_notice": (
        "\n  태그 자동: #{tags} — "
        "수정: edit(id='{id}', tags=[...], action='overwrite') · 해제: tags='-'"
    ),

    "err_status": "오류: {err}",


    "rule_tag_removed": (
        "ℹ️ #rule 태그는 폐지됨 — 규칙 지정은 status='rule' 이 정본. "
        "태그에서 제외했습니다."
    ),


    "status_invalid_default": (
        "⚠️ status '{input}' 무효 — open 으로 저장됨. "
        "수정: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "status_invalid_skip": (
        "⚠️ status '{input}' 무효 — 스킵, 기존값('{current}') 유지. "
        "재시도: edit(id='{id}', status=open|done|dropped|rule)"
    ),

    "err_no_relates": "오류: relates(대상 lore ID)를 지정하세요.",

    "err_not_found": "오류: lore '{id}'를 찾을 수 없습니다.",

    "no_changes": "변경 사항 없음. 수정할 필드를 지정하세요.",

    "overwrite_desc": "body 전체 교체 — {id}",
    "overwrite_confirm": (
        "⚠️ [{id}] body 전체 교체 준비 — 기존 {old_len}자 소멸.\n"
        "  현재 첫 줄: {first_line}\n"
        "  1. 실행: edit(confirm={slot})\n"
        "  2. 덧붙이기(기본, overwrite 없이 재호출)"
    ),

    "modify_replace_echo": (
        "\n  body 전체 교체 — 옛 {old_len}자 → 새 {new_len}자 "
        "(옛 본문 lore_history 보존, 복구: log(id='{id}'))\n  ↳ {echo}"
    ),

    "modify_append_echo": "\n  body(append) — 기존 {old_len}자 뒤에 +{appended_len}자\n  ↳ {echo}",

    "tags_cleared": "tags 해제 — 기존 {n}개 제거",
    "tags_replaced": "tags 교체 — {old_n}개 → {new_n}개",
    "tags_added": "tags +{n}개 (총 {total}개)",

    "files_cleared": "files 해제 — 기존 {n}개 제거",
    "files_replaced": "files 교체 — {old_n}개 → {new_n}개",
    "files_added": "files +{n}개 (총 {total}개)",

    "err_no_title_or_msg": "오류: title 또는 msg를 지정하세요.",

    "supersede_result": (
        "[{new_id}] {title}\n"
        "  ↳ supersede: {old_id} → {new_id} "
        "(새 lore 박힘, 옛 lore는 head=False로 보존)\n"
        "  ⚠️ append 아님 — 옛 본문은 brief/show 기본 결과에 안 보임. "
        "같은 ID에 본문만 추가하려면 edit(msg=...) 사용."
    ),

    "no_lore": "등록된 lore가 없습니다.",
    "no_filtered_lore": "조건에 맞는 lore가 없습니다 ({filters}). 전체 {total}건.",

    "oneline_header": "lore ({matched}/{total}건)",
    "cluster_suffix": "+{n}클러스터",
    "detail_header": "# lore ({matched}/{total}건)",
    "cluster_detail_suffix": "  +{n} 클러스터 (show(query=)로 전체)",

    "delete_permanent": "[{id}]{title_str} 영구 삭제됨 (복구 불가)",
    "delete_soft": (
        "[{id}]{title_str} 휴지통으로 이동 — "
        "복구: restore('{id}'), 영구삭제: rm('{id}', force=True)"
    ),

    "predecessor_revived": "전임자 [{id}]가 복권됨(대체본 삭제 — dropped로 검색에 표시)",

    "restore_already_active": "[{id}] 이미 활성 상태 (휴지통 아님).",
    "restored": "[{id}] 휴지통에서 복구됨",
}
