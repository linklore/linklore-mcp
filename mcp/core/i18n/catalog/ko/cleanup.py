"""Korean (ko) messages for the 'cleanup' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "cleanup — 강한 중복 lore/doc 후보 표시\n"
        "\n"
        "  cleanup()                  default — type='lore', open 만 (결정 끝난 건 제외)\n"
        "  cleanup(type='doc')        doc 중복 후보 (아래 한계 참고)\n"
        "  cleanup(status='')         전체 status 포함 (done/dropped 등도)\n"
        "  cleanup(status='done')     특정 status 끼리만\n"
        "  cleanup(threshold=0.80)    더 너그럽게\n"
        "\n"
        "동작: head 항목(lore 또는 doc) 임베딩 cosine 매트릭스 → threshold 이상 pair.\n"
        "기본 open — 결정 끝난(done/dropped) 항목은 판단 완료라 제외.\n"
        "표시: 새 ↔ 옛 (중복 후보). 제안 명령 = link(a=옛, b=새, action='supersede').\n"
        "⚠️ type='doc' 한계: doc 임베딩은 title+body(앞 500자)+items+tags 사용 —\n"
        "   500자 넘는 본문의 뒷부분만 다른 중복은 못 잡는다.\n"
        "⚠️ 자동 삭제 X — 사용자 결정 필수."
    ),

    "pair_new": "  새: {id} {title}",
    "pair_old": "  옛: {id} {title}",
    "pair_confirm": "  → 대체 확정: link(a='{older_id}', b='{newer_id}', action='supersede')",

    "not_enough_lore": "비교할 lore가 부족합니다 (대상 2건 미만).",
    "not_enough_doc": "비교할 doc가 부족합니다 (대상 2건 미만).",
    "err_no_embed_model": "오류: 임베딩 모델 미설치 (fastembed)",
    "not_enough_indexed_lore": "임베딩 캐시에 등록된 head lore가 부족합니다.",
    "not_enough_indexed_doc": "임베딩 캐시에 등록된 head doc가 부족합니다.",
    "no_dup_lore": "강한 중복 lore 없음 (cos ≥ {threshold}, head {count}건 검사)",
    "no_dup_doc": "강한 중복 doc 없음 (cos ≥ {threshold}, head {count}건 검사)",
    "dup_candidates_header": "# 중복 후보 (cos ≥ {threshold}, {pairs}건 / head {count}건 검사)",
    "warn_manual_lore": "⚠️ 자동 close X — 의미 다른 비슷한 lore도 있으니 본문 확인 후 결정.",
    "warn_manual_doc": "⚠️ 자동 close X — 의미 다른 비슷한 doc도 있으니 본문 확인 후 결정.",
    "doc_embed_limit_note": "⚠️ doc 임베딩은 title+body(앞 500자)+items+tags 기반 — 500자 넘는 본문 뒷부분만 다른 중복은 못 잡음.",
}
