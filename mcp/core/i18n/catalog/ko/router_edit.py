"""Korean (ko) messages for the 'router_edit' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "edit — 엔티티 수정 (ID prefix 자동)\n\n"
        "## 인자 형식 (중요)\n"
        "  id — 풀 ID 사용 권장 (예: lr-1a2b3c4d). show()는 부분 매칭 OK, edit은 풀 ID 필요.\n"
        "  tags/files/links — list 권장, str 쉼표 구분은 CLI 자연 입력용(`llre edit tags=a,b`) (예: ['a','b'] 또는 'a,b')\n"
        "  items — 체크리스트 조작(리스트·items=N(int) 토글)은 doc 전용 · batch(JSON 배열)는 lore·doc 둘 다 (아래 참조)\n\n"
        "## 본문 수정 (action) — append(기본) / section / overwrite / supersede 4갈래\n"
        "  action='append', msg='추가 내용'         → body 끝에 append (기본, 비파괴). action 생략하고 msg만 줘도 동일\n"
        "  action='section', section='## 헤딩', msg='새 섹션 내용'  → 그 섹션만 통째 교체(하위 섹션 포함), 나머지 body 보존\n"
        "    ↳ msg 는 헤딩 포함/생략 무관 — 헤딩으로 시작하면 그대로(중복 X, 리네임 가능), 아니면 원 헤딩 보존\n"
        "    ↳ section= 은 msg 필수 · action='overwrite'/items 와 동시 사용 불가(단독 모드) · batch 미지원\n"
        "    ↳ 헤딩은 부분일치도 OK, 모호하면 후보 목록·없으면 사용가능 섹션 목록을 그대로 반환\n"
        "    ↳ 같은 콜의 links= 도 함께 연결됨(id 안 바뀌므로 그 자리에서)\n"
        "  action='overwrite', msg='새 본문'        → body 전체 교체(수정). 옛 body→log(id)로 복구\n"
        "    ↳ 같은 콜의 tags=/items=(doc)/파일(links= 중 파일경로)도 함께 전체교체 · links= 의\n"
        "      id 연결(lr-y/dc-y 등)은 항상 추가만 — overwrite 영향 없음(link()이 멱등이라 다른\n"
        "      기존 연결이 지워질 걱정 없이 안전, 2026-07-09 doc-doc 삭제 실버그 fix)\n"
        "  action='supersede', msg='새 결론'        → 새 id 생성(옛 것에서 title/tags/status 상속)·옛 것 head=False\n"
        "    ↳ section= 과 동시 사용 불가 · title/tags/status 미지정 시 옛 항목 상속\n"
        "    ↳ 같은 콜의 links=(id·파일경로 모두) 도 새 id 에 연결됨(2-pass 불필요)\n\n"
        "## 수정 결정 트리\n"
        "  추가 (비파괴, 기본)       → edit(id, msg='...')  또는 edit(id, action='append', msg='...')\n"
        "  부분 수정 (기존 섹션만 교체) → edit(id, action='section', section='헤딩', msg='...')\n"
        "  교체 (수정)               → edit(id, action='overwrite', msg='...')\n"
        "  후속 발행 (=supersede, 새 id 생성) → edit(id=old_id, action='supersede', msg='새 결론')\n"
        "    (또는 add(type='lore'|'doc', relates=old_id, ...) — 동일 경로)\n"
        "  폐기 (대체본 없음, 검색 남음) → edit(id, status='dropped')\n"
        "  폐기+대체 (=supersede by 기존, 검색제외) → link(a=X, b='lr-Y'|'dc-Y', action='supersede')\n"
        "    대체본 있으면 자동 head=False (검색/brief 제외). 모순 결정 정리·버전 교체에 1콜.\n"
        "    (a=폐기될 옛 항목, b=생존할 기존 항목 — b 는 새로 안 만듦)\n"
        "  완전 삭제 (history X)     → rm(id)\n\n"
        "## 단건 수정\n"
        "  lr-* → lore: title/msg/status/tags/links\n"
        "  dc-* → doc: title/msg/items/tags/links(+flow)/status  (flow 는 doc 전용, lore 는 없음)\n"
        "  links= 통합 — edit(id, links=['src/x.py','lr-y','제목']) 파일·id·제목 자동분류\n"
        "  links=['dc-y'], flow=True → 문서 여정 체인 (doc 전용)\n"
        "  연결 해제(파일 1개·id 1개)는 unlink(a, 대상) — links='-' 일괄해제는 제거됨\n"
        "    (unlink() 반복과 동일 연산이라 실증수요 없어 보류)\n"
        "## status (lore/doc 공통) — 딱지 (검색에 계속 뜸)\n"
        "  open | done | dropped | rule(바뀌지 않는 기준) (또는 'clear' = open 복귀). "
        "그 외 값은 — status 단독 변경이면 거부, 다른 변경(msg 등) 동반이면 그 변경만 반영되고 status 는 스킵(기존값 유지)+경고.\n"
        "  ★ 정리 형태 구분 (헷갈리기 쉬움):\n"
        "     done                     = 끝난 유효 지식      → 검색에 뜸 (완료 표시)\n"
        "     dropped (대체본 없음)      = 폐기+이유 남김      → 검색에 뜸 (폐기 표시)\n"
        "     dropped + link(action='supersede') = 폐기+대체본 있음(=supersede) → 검색 숨김 (자동 head=False)\n"
        "     rm                       = 완전 삭제(이력 X)   → 휴지통/영구\n"
        "  ↑ supersede 는 별도 개념 아님 — '대체본 링크 있는 dropped'. 링크 유무가 검색노출을 가름.\n"
        "## 컬렉션 필드 (items(doc 전용)/tags/links) — msg와 동일 규칙\n"
        "    기본 = append(비파괴, 기존 보존) | action='overwrite' = 전체 교체\n"
        "    tags/items 는 '-' = clear 도 지원 · links 는 '-' 없음, 개별 해제는 unlink(a, 대상)\n"
        "    items 제거(파괴적, doc 전용): action='remove' 필수 — edit(id, action='remove', items=[N])  # 1-based, 여러개 items=[N,M]\n"
        "    items 추가: 리스트로 — edit(id, items=['새 항목'])  ('+텍스트' 문자열 접두는 은퇴됨)\n"
        "    items = 진행 추적 체크리스트(단일 개념) — done 없는 dict 항목은 legacy 읽기 전용(신규 생성 비권장)\n"
        "## items= 에 int/int리스트를 주면 — 단일 항목 토글 (action=/overwrite 스위치 안 씀)\n"
        "    edit(id='dc-x', items=3)        → 3번 항목 체크 토글 (1-based)\n"
        "    edit(id='dc-x', items=[2,3])    → 2·3번 동시 토글 (str/dict 형이면 지금처럼 추가/교체)\n"
        "    ⚠️ items='-N'/'✓N'/'vN'/'+텍스트' 문자열 접두 문법은 은퇴됨 — "
        "제거는 action='remove', items=[N] · 토글은 items=[N](int) · 추가는 items=['텍스트']\n\n"
        "## 배치 수정\n"
        "  edit(items='[{{\"id\":\"lr-...\",\"status\":\"done\"}},...]')\n"
        "  items가 JSON 배열 + 첫 항목 ID로 타입 자동 판별 (dc-* → doc batch, lr-* → lore batch)\n"
        "  항목별 overwrite 지원 — 전체교체(수정), 옛 body→log(id)로 복구\n"
        "    (항목별 \"overwrite\":true 또는 \"action\":\"overwrite\" — 단건 edit()과 동일 별칭, 둘 다 됨)"
    ),

    "err_no_id_or_items": "오류: id 또는 items(JSON 배열)을 지정하세요.",
    "err_action_invalid": "오류: action='{action}' 미지원 — append|section|overwrite|supersede|remove 중 하나",
    "err_section_required": "오류: action='section' 은 section=(헤딩) 필수",


    "err_remove_items_required": (
        "오류: action='remove' 는 items(제거할 1-based 번호) 필수 — "
        "edit(id='{id}', action='remove', items=[N])"
    ),


    "err_remove_section_conflict": "오류: action='remove' 는 section= 과 동시 사용 불가",
    "err_supersede_section_conflict": "오류: action='supersede' 는 section= 과 동시 사용 불가",
    "err_mode_conflict_items": "오류: 모드 충돌 — section 은 단독 사용",
    "err_section_msg_required": "오류: section= 은 msg=(그 섹션의 새 내용) 필수",
    "err_not_edit_target": "오류: '{id}'는 edit 대상이 아닙니다. lore(lr-*), doc(dc-*)만 수정 가능.",
    "err_no_linklore": "오류: .linklore 없음",
    "err_links_dash_removed": (
        "오류: links='-' 는 제거됨 — 개별 연결 해제는 unlink(a, 대상) 사용.\n"
        "  (일괄 연결해제 = unlink() 반복과 동일 연산이라 실증수요 없어 보류)"
    ),
    "err_lore_doc_only_args": (
        "lore엔 {joined} 없음 — {joined}는 doc 전용입니다. "
        "lore 본문 추가는 edit(id='{id}', msg='...')"
    ),
    "err_empty_list_tags": (
        "빈 리스트는 모호합니다 — 전부 해제: edit(id='{id}', tags='-') · "
        "교체: edit(id='{id}', tags=[...], action='overwrite') · "
        "추가: edit(id='{id}', tags=[...])"
    ),
    "err_empty_list_links": (
        "빈 리스트는 모호합니다 — 개별 해제: unlink(a='{id}', b=대상) · "
        "교체: edit(id='{id}', links=[...], action='overwrite') · "
        "추가: edit(id='{id}', links=[...])"
    ),

    "lore_no_change_with_preview": (
        "{preview}\n\n수정 내용 지정:\nedit(id='{id}', msg='+추가')  # append\n"
        "edit(id='{id}', status='done')  # 또는 'dropped'"
    ),
    "lore_no_change_no_preview": "수정 내용 지정:\nedit(id='{id}', msg='+추가')",
    "doc_no_change_preview": (
        "{preview}\n\n수정 예시:\nedit(id='{id}', items=[1,3])  # 토글\nedit(id='{id}', status='done')"
    ),
    "lore_links_only": "[{id}]",
    "doc_links_only": "[{id}]",

    "auto_files_note": (
        "\n📎 파일 자동연결 (uncommitted diff, 방금 추가된 내용 기준): {files}"
        "\n   무관한 파일은 unlink(a='{id}', b='파일명') 로 개별 해제"
    ),

    "link_ok": "  ↔ {target}",
    "link_fail": "  ⚠️ link({target}) 실패: {err}",
    "link_summary_header": "\n🔗 연결됨 (links=):\n",


    "flow_link_ok": "  → {target} (흐름 연결됨)",
    "flow_link_summary_header": "\n→ 흐름 연결됨 (flow_links=):\n",

    "err_item_not_found": "오류: '{item_id}'를 찾을 수 없습니다.",
    "err_wrap": "오류: {err}",
    "err_section_match_fail": "섹션 매칭 실패",
    "section_replaced": (
        "✂ 섹션 '{heading}' 교체 — 섹션 {old_len}자→{new_len}자 "
        "(본문 총 {body_len}자) · 옛 본문은 log(id='{item_id}') 로 복구"
    ),

    "err_batch_invalid_json": "오류: items가 유효한 JSON 배열이 아닙니다.",
    "err_batch_empty": "오류: items가 비어있거나 배열이 아닙니다.",
    "batch_section_unsupported": "{eid}: section= 은 batch 미지원 — 단건 edit(id=, section=, msg=)로",
    "batch_all_section_errors": "0/{total}건 ({errcount}건 오류)\n",
    "batch_section_excluded_suffix": "\n(section= {errcount}건 제외)\n",
    "batch_unknown_id_prefix": "오류: 알 수 없는 ID prefix — '{id}'. 배치 edit은 첫 항목의 id(lr-*/dc-*)로 lore/doc을 판별합니다.",
    "batch_mixed_kind": (
        "오류: 배치에 lore(lr-)와 doc(dc-) id가 섞여 있습니다 — 첫 항목이 {first_kind}로 판별돼 "
        "다른 kind의 id는 'not found'로 오표면화됩니다(실제로는 존재할 수 있음). "
        "타입별로 나눠 호출하세요: edit(items=[lore끼리]) / edit(items=[doc끼리])."
    ),

    "preview_header": "[{id}] {title}",
    "preview_body_line": "  {line}",
    "preview_meta_tags": "tags={tags}",
    "preview_meta_line": "  ({meta})",

    "err_name_not_found": "오류: '{name}'를 찾을 수 없습니다. ID(lr-*/dc-*)를 사용하세요.",

    "err_auto_search_not_alone": "오류: auto_search= 는 단독으로만 — 제거: {params}",
    "auto_search_set": "[{id}] \"{title}\" — {state}",
    "auto_search_state_on": "자동 검색/브리프에 다시 포함됨",
    "auto_search_state_off": "자동 검색/브리프에서 제외됨(show(query=)로 id 직접조회는 그대로 가능)",
}
