"""Korean (ko) messages for the 'hints' surface."""
MESSAGES: dict[str, str] = {


    "sem_label": " (의미 유사 {cosine})",


    "weak_candidates": "  약한 후보 {n}건 — 겹침은 cleanup()으로 확인",


    "dup_action_unrelated": "   • 무관(관련 없음) → link(a='{new_id}', b='{top_id}', action='unrelated')",
    "dup_action_distinct": "   • 중복 아님(별개 확정) → link(a='{new_id}', b='{top_id}', action='distinct')",
    "conflict_action_unrelated": "   • 무관             → link(a='{new_id}', b='{top_id}', action='unrelated')",


    "dup_header": "\n🚨 매우 비슷한 lore (중복 가능):",
    "dup_judge_header": "   판단 (열지 말고 위 미리보기로 — 같은 결정?):",
    "dup_action_supersede": "   • 방금 게 나음  → link(a='{top_id}', b='{new_id}', action='supersede')",
    "dup_action_keep": "   • 기존 유지     → rm(id='{new_id}', force=True)",
    "dup_action_no_id": "   → 본문 확인 후: link(action='supersede') 또는 rm(force=True) 또는 유지",


    "conflict_header": "\n⚠️ 상충 후보 (주제 같음 — 결론 반대인지 확인):",
    "evidence_suffix": " (근거: {evidence})",
    "conflict_judge_header": "   판단 (극성=결론 방향 — 위 미리보기로):",
    "conflict_action_opposite": "   • 반대 결정(상충)   → 현행 확정 후 link(action='supersede')로 옛 결정 봉인",
    "conflict_action_reinforce": "   • 보강·이어짐(보완) → edit(id='{new_id}', links=['{top_cid}']) 로 엮기",

    "related_header_full": "\n관련 후보 (제안 · 연결 안 됨 — 엮으려면 links=/link()):",
    "related_header_short": "관련 후보 (제안 · 연결 안 됨):",
}
