"""Korean (ko) messages for the 'doctor' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "doctor() — 프로젝트 데이터 정합성 점검(oldId/newId·files[]경로·링크대상 실존).\n"
        "\n"
        "doctor()             read-only 진단 (기본)\n"
        "doctor(action='fix') 발견된 문제 자동 복구\n"
    ),

    "help": (
        "doctor — 프로젝트 데이터 정합성 점검 + 자동 복구\n"
        "\n"
        "  doctor()             read-only 진단 — oldId/newId 슈퍼시드 체인(lore/doc 공용),\n"
        "                       lore/doc files[] 경로 실존, lore_links/doc_links/lore_works\n"
        "                       참조 대상 실존\n"
        "  doctor(action='fix') 발견된 문제 자동 복구(oldId/newId 재연결·dangling 클리어·\n"
        "                       반쪽 봉인 완성, 고아 관계행 삭제) 후 재검증 요약\n"
        "\n"
        "⚠️ files[] 경로 누락(stale)과 supersede_fork(분기)는 진단만 — 파일은 되살릴 수 없고\n"
        "  분기는 어느 쪽이 정본인지 기계가 판단할 수 없어 자동 fix 대상 아님.\n"
        "  stale 수동 정리: 재연결 edit(id, links=['새/경로']) · 죽은 참조 제거 unlink(id, '옛/경로')"
    ),
    "err_action_invalid": "오류: action='{action}' 미지원 — '' 또는 'fix'",
    "ok_no_issues": "정상 — 문제 없음",
    "check_header": "# 정합성 점검 — error {error} · warn {warn} · info {info}",
    "auto_fix_hint": "자동 복구 가능한 항목(oldId/newId·링크대상 실존)은 doctor(action='fix')",
    "stale_hint": "stale(파일 없음)은 수동 정리 — 재연결: edit(id, links=['새/경로']) · 죽은 참조 제거: unlink(id, '옛/경로')",
    "fix_header": "# doctor(action='fix') 결과",
    "fixed_header": "고친 항목 ({count}):",
    "nothing_fixed": "고칠 항목 없음.",
    "remaining_issues": "\n남은 문제 (error {remaining}건) — doctor() 로 상세 확인",
    "no_remaining": "\n재검증: 남은 error 없음.",
}
