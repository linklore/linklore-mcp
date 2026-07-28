"""Korean (ko) messages for the 'inbox' surface."""
MESSAGES: dict[str, str] = {

    "err_source_unregistered": "source '{name}' 미등록",

    "err_item_not_found": "'{item_id}' source '{name}'에 없음",


    "provenance_report_failed": " (provenance 보고 실패: {err})",

    "skipped_self": "본진에 원본 있음({id}) — 흡수 불필요 (이미 내 항목)",

    "deduped": "이미 import됨 — {name}/{id} → {new_id}",

    "imported": "[{new_id}] {kind_label} import 완료 — {name}/{id}",

    "local_source_noop": "remote/{pid}/ 로컬 source — 원격 동기화 불필요 (lore {lore_count} / doc {doc_count})",

    "err_session_expired": "세션 만료(401) — 재로그인: uvx llre login",

    "revoked": "remote/{pid}/ revoked — 게시 철회됨, 비움",
}
