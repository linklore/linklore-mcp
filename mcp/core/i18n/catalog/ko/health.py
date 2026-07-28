"""Korean (ko) messages for the 'health' surface."""
MESSAGES: dict[str, str] = {
    "dangling_cleared": (
        "{label} [{item_id}] {field} dangling 클리어 "
        "(항목은 dropped 유지 — 복원 원하면 restore)"
    ),
    "old_new_sealed": "{label} [{target_id}] → [{item_id}] oldId/newId 봉인 완성",
    "resealed": "{label} [{item_id}] head=False/status=dropped 재봉인",
    "orphan_seal_revived": "{label} [{item_id}] head=True 복권 (고아 봉인 해소, status=dropped 유지)",
    "orphan_link_deleted": "{collection} [{item_id}]→[{target_id}] 고아 링크 {count}건 삭제",
    "orphan_ref_deleted": "lore_works [{item_id}]→[{target_id}] 고아 참조 삭제",
    "dangling_supersede": "{label} [{item_id}] {field}={target_id} — 대상 없음(dangling, corruption)",
    "half_sealed": "{label} [{item_id}] newId 없음(반쪽 쓰기) — [{ref_id}]가 oldId로 가리킴",
    "supersede_fork": "{label} [{item_id}] newId={new_id}이지만 [{ref_id}]도 oldId로 가리킴(분기)",
    "superseded_but_head": "{label} [{item_id}] newId={new_id} 설정됐지만 head=True(반쪽 봉인)",
    "orphaned_seal": "{label} [{item_id}] head=False 인데 newId 없음 — 고아 봉인(대체본 삭제로 참조 소실)",
    "supersede_convergence": "수렴 그룹 {n}개 — 정상 (여러 항목이 같은 new_id로 수렴)",
    "trash_reference": "휴지통 참조 {n}건 — restore 시 복원, 영구삭제 시 정리됨",
    "stale_file": "{label} [{item_id}] — {path} 파일 없음 (삭제/이동됨)",
    "broken_link_src": "{collection} [{src}]→[{dst}] ({kind}) — src {entity_word} [{src}] 없음",
    "broken_link_dst": "{collection} [{src}]→[{dst}] ({kind}) — dst {entity_word} [{dst}] 없음",
    "broken_ref_lore": "lore_works [{lore_id}]→[{doc_id}] — lore [{lore_id}] 없음",
    "broken_ref_doc": "lore_works [{lore_id}]→[{doc_id}] — doc [{doc_id}] 없음",
}
