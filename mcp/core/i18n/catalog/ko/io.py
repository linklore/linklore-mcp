"""Korean (ko) messages for the 'io' surface."""
MESSAGES: dict[str, str] = {
    "err_no_store": "아직 기억 없음 (.linklore/ 없음). init() 으로 시작하세요. (탐색: {start})",


    "err_store_missing_init": "이 폴더에 LinkLore 저장소가 없습니다 — init() 먼저. (탐색: {start})",


    "err_no_store_pinned": "오류: 실행 안 됨 — pin({target})에 저장소가 없습니다 (.linklore/ 없음). 의도한 대상이 아니면 config(action='unpin'), 여기서 새로 시작하려면 init(). (탐색: {start})",
    "warn_boundary": "⚠️ 이 폴더({anchor})엔 .linklore 없음 — 상위 '{store}'의 공유 저장소를 사용 중입니다. 독립 메모리를 원하면 init().",

    "warn_pin_write_divergence": "⚠️ 지금 pin된 상태입니다 — 작업 디렉토리({base})와 다릅니다. 이 쓰기는 pin({target})을 대상으로 합니다 — 해제: config(action='unpin')",


    "warn_pin_export_divergence": "⚠️ 지금 pin된 상태입니다 — 작업 디렉토리({base})와 다릅니다. 이 전송은 pin({target})의 데이터를 내보냅니다 — 해제: config(action='unpin')",


    "parent_independent": "ℹ️ 상위 '{parent}' 저장소와 별개의 독립 저장소로 시작합니다.",


    "parent_referenced": (
        "⚠️ 상위 '{parent}' 저장소에 이 폴더를 참조하는 항목이 {n}건 있습니다 — "
        "이 프로젝트에서는 이제 그 항목들이 조회되지 않습니다.\n"
        "   가져오려면: local_cross(action='move', id=[...], from_dir='{parent_dir}', to='{child_dir}')"
    ),
}
