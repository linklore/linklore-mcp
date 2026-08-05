"""Korean (ko) messages for the 'link' surface."""
MESSAGES: dict[str, str] = {

    "warn_superseded": "⚠ {eid} 은 superseded(대체됨) — 최신 head 에 거는 게 맞는지 확인 (show(query=))",
    "warn_dropped": "⚠ {eid} 은 dropped(폐기) 항목 — 폐기본에 연결 중",


    "err_entity_not_found": "오류: {label} 없음 — {id}",
    "err_entity_not_found_simple": "오류: {label} 없음",
    "already_linked": "이미 연결됨",
    "not_linked_simple": "연결 없음 (이미 끊겨 있음)",


    "linked_symmetric": "{a_title} ↔ {b_title}\n연결됨 ({label}Link 양방향)",
    "unlinked_symmetric": "{a_title} ↮ {b_title}\n연결 해제됨 ({label}Link 양방향)",


    "already_linked_flow": "이미 연결됨: {a} → {b}",
    "linked_flow": "{a_title} → {b_title}\n흐름 연결됨 (flowLink)",
    "not_linked_flow": "연결 없음: {a} → {b} (이미 끊겨 있음)",
    "unlinked_flow": "{a_title} ↛ {b_title}\n흐름 연결 해제됨 (flowLink)",


    "already_linked_cross": "이미 연결됨: {a_id} ↔ {b_id}",
    "linked_cross": "{a_title} ↔ {b_title}\n연결됨 ({label})",
    "not_linked_cross": "연결 없음: {a_id} — {b_id} (이미 끊겨 있음)",
    "unlinked_cross": "{a_title} ↮ {b_title}\n연결 해제됨 ({label})",


    "err_supersede_type_mismatch": "오류: supersede 는 같은 타입끼리만 — lore↔lore 또는 doc↔doc",
    "err_supersede_self": "오류: 자기 자신으로 supersede 불가",
    "err_supersede_target_missing": "오류: 대체 대상 '{b}' 가 존재하지 않습니다 (phantom supersede 방지).",
    "err_supersede_cycle": "오류: {a} → {b} 는 supersede 순환을 만듭니다 — {b} 가 이미 (연쇄적으로) {a} 로 되돌아갑니다. 둘 다 그대로입니다.",
    "supersede_done": (
        "[{a}] 폐기(dropped) + 대체 → [{b}]\n"
        "  대체본 있는 dropped = 자동 검색제외 (head=False). show(superseded=True)·show(query=) 로 보임.\n"
        "  cf. 대체본 없는 폐기는 status='dropped' 만 (검색에 남음)."
    ),


    "err_action_file_incompatible": "오류: action='{action}' 는 파일경로와 결합 불가 — 파일은 related(기본)만 지원",
    "err_unrecognized": "오류: '{raw}' 인식 불가 — id(lr-*/dc-*)·기존 제목·실존 파일 중 하나여야 합니다.",
    "err_flow_file_incompatible": "오류: flow=True 는 파일경로와 결합 불가 — 파일은 flow 없이(기본)만 지원",
    "err_item_not_found": "오류: '{other}'를 찾을 수 없습니다.",
    "not_linked_file": "연결 없음: {other} — {file} (이미 끊겨 있음)",
    "unlinked_file": "{title} ↮ {file}\n연결 해제됨 (파일)",


    "err_multi_value": "오류: a=/b=는 단일 id/파일/제목만 지원합니다 — 여러 쌍을 연결하려면 link()를 반복 호출하세요.",

    "link_help": (
        "link — 두 항목 연결 (ID prefix 자동 판별)\n"
        "\n"
        "## ID 형식\n"
        "  prefix 매칭 OK (예: 'lr-1a2b3c4'로 dc-1a2b3c4d 자동 매칭). 다중 매치 시 풀 ID 필요.\n"
        "  id 꼴이 아니면 자동분류(add/edit 의 links= 와 동일 분류기 재사용):\n"
        "  link('lr-X', '기존 lore 제목')      → 제목 정확일치 시 그 id 로 연결\n"
        "  link('lr-X', 'src/a.py')            → 실존 파일이면 X.files 에 코드연결(link 테이블 아님)\n"
        "    (파일경로는 action='related'(기본)에서만 동작 — flow/supersede 는 구조적 관계라\n"
        "     파일과 결합 불가, 둘 다 거부됨)\n"
        "\n"
        "## action='related' (기본) — 상호 연결\n"
        "  link('dc-A', 'dc-B')              → 양쪽 docLink (상호 관련)\n"
        "  link('lr-X', 'lr-Y')              → 양쪽 loreLink (클러스터링)\n"
        "  link('dc-A', 'lr-X')              → lore X.works에 A 추가\n"
        "  link('lr-X', 'dc-A')              → 위와 동일 (순서 무관)\n"
        "\n"
        "## action='flow' — 문서 순서 (a→b 방향, doc↔doc 전용)\n"
        "  link('dc-A', 'dc-B', action='flow')   → A.flowLink에 B (a 다음 b 로 읽는 여정)\n"
        "\n"
        "## action='supersede' — a가 b로 대체 (a=old 폐기, b=target 생존)\n"
        "  link('lr-old', 'lr-new', action='supersede')  → lr-old head=False/dropped, lr-new 로 대체\n"
        "  link('dc-old', 'dc-new', action='supersede')  → 위와 동일 (doc)\n"
        "  제약: 같은 타입끼리만(lore↔lore/doc↔doc) · b 는 실존 항목이어야 함\n"
        "\n"
        "## 제안 판정 4종 — 관련 후보/중복 경보에 대한 응답 (맞음 2 + 아님 2)\n"
        "  관련 맞음 → link(a, b)                       기존 연결 (엮이면 재제안 자동 소멸)\n"
        "  중복 맞음 → link(a, b, action='supersede')   기존 대체 (옛 항목 봉인)\n"
        "  관련 없음 → link(a, b, action='unrelated')   판정 저장 — 관련 후보+중복 경보 억제\n"
        "  중복 아님 → link(a, b, action='distinct')    판정 저장 — 중복 경보만 억제 (관련 후보 잔존: 별개지만 관련)\n"
        "  방향 무관(a/b 순서 자유) · 타입 제약 없음(lr↔lr/dc↔dc/dc↔lr) · 재호출 멱등\n"
        "  재판정(되돌리기) = unlink(a, b, action=동일값)\n"
        "\n"
        "제한: dc↔lr + flow/supersede 미지원 (supersede는 동종끼리(lr↔lr/dc↔dc) · flow는 doc↔doc만)\n"
        "\n"
        "해제(역연산) = unlink(a, b) — 동일 인자 (파일 연결 해제 포함)"
    ),
    "err_ab_required": "오류: a, b 두 ID 필수",
    "err_self_link": "오류: 자기 자신과는 연결 불가",
    "err_bad_action": "오류: action='{action}' 미지원 — related|flow|supersede|unrelated|distinct 중 하나",


    "verdict_unrelated_done": (
        "{a} ✕ {b} 판정 저장: 관련 없음(unrelated)\n"
        "  이 쌍은 관련 후보·중복 경보에 다시 안 뜹니다. 되돌리기 = unlink(a='{a}', b='{b}', action='unrelated')"
    ),
    "verdict_distinct_done": (
        "{a} ≠ {b} 판정 저장: 중복 아님(별개 확정, distinct)\n"
        "  중복 경보만 꺼집니다 — 관련 후보로는 계속 등장(별개지만 관련). 되돌리기 = unlink(a='{a}', b='{b}', action='distinct')"
    ),
    "verdict_already": "이미 판정됨: {a} — {b} ({action}) — 재호출은 멱등(변화 없음)",
    "verdict_removed": "판정 해제됨: {a} — {b} ({action}) — 후보/경보 복귀",
    "verdict_not_found": "판정 없음: {a} — {b} ({action}) (이미 해제 상태)",
    "err_unrecognized_id": "오류: 인식할 수 없는 ID — a={a} ({a_col}), b={b} ({b_col})",
    "err_flow_link_only": "오류: flow는 doc↔doc(dc-* 양쪽)만 지원",
    "err_flow_cycle": "오류: {a} → {b} 는 순환을 만듭니다 — doc 여정은 선형 체인만 지원(루프 불가). 체인은 그대로입니다.",

    "unlink_help": (
        "unlink — 연결 해제 (link와 대칭)\n"
        "\n"
        "  unlink('dc-A', 'dc-B')                    → 양쪽 docLink에서 제거\n"
        "  unlink('dc-A', 'lr-X')                    → X.works에서 A 제거\n"
        "  unlink('dc-A', 'dc-B', action='flow')     → A.flowLink에서 B 제거\n"
        "  unlink('lr-X', 'src/a.py')                → X.files 에서 그 파일 제거\n"
        "  unlink('lr-X', 'lr-Y', action='unrelated') → '관련 없음' 판정 해제 (후보/경보 복귀)\n"
        "  unlink('lr-X', 'lr-Y', action='distinct')  → '중복 아님' 판정 해제 (중복 경보 복귀)\n"
        "  (action='flow' + 파일경로 조합은 거부 — 파일은 action='' 에서만 지원, link() 과 대칭)"
    ),
    "err_bad_action_unlink": "오류: action='{action}' 미지원 — flow|unrelated|distinct 중 하나 (또는 미지정)",
    "err_flow_unlink_only": "오류: flow는 doc↔doc만",


    "err_sentinel": "오류",
}
