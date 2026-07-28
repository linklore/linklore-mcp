"""Korean (ko) messages for the 'router_add' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "add(type='lore'|'doc', title, msg=) — lore=발자취/결정, doc=기획서.\n"
        "연결 인자 2종: links=통합(코드파일·dc/lr id·제목 자동분류, flow=True 면 문서 체인) · push_to=박스로 전송(링크 아님).\n"
        "items=['a','b']→체크리스트(0/N, doc 전용) · items=[{{...}}]→batch 생성(lore·doc 둘 다 — 다건은 이걸로, N번 단건호출보다 넛지 조용함). "
        "상세 help=True"
    ),

    "help": (
        "add — 엔티티 생성 (type으로 라우팅)\n\n"
        "## 인자 형식\n"
        "  list 권장 — tags=['a','b'], items=['할일1','할일2']\n"
        "  string 쉼표 — tags='a,b' (CLI 자연 입력용, `llre add tags=a,b`)\n\n"
        "## 연결 인자 — 2종 (links 통합, 목적이 다름)\n"
        "  links=['src/x.py','lr-y','결정 제목']  연결 통합 — 파일경로·id·제목 자동분류\n"
        "                          (파일=코드 연결, dc/lr id·정확한 제목=지식 그래프 자동 라우팅. link() 불필요)\n"
        "  links=['dc-a','dc-b'], flow=True       문서 여정 체인 (doc 전용, 순서=리스트 순서)\n"
        "  push_to=['team-prj']    ★링크 아님★ — 만든 직후 그 오픈박스로 전송(send)\n\n"
        "## items — 진행 추적 체크리스트(단일 개념). 입력 형태가 결과 UI 를 정함\n"
        "  items=['a','b','c']           → 체크리스트 (0/N, edit(id, items=N)으로 토글, doc 전용)\n"
        "  items=[{{'title':'...'}},...]   → 카탈로그(dict 카드) = batch 생성 (lore·doc 둘 다 가능)\n"
        "  💡 lore 여러 건 만들 땐 이 배치형으로 — add() 단건 N번보다 조용함"
        "(항목당 관련후보 top-1 한 줄만, 단건은 매번 전체 넛지)\n"
        "  ⚠️ done 키 없는 dict 항목은 legacy 읽기 전용 — 신규 생성엔 비권장"
        "(체크리스트는 list[str] 또는 done 포함 dict로)\n\n"
        "## 예시\n"
        "  add(type='lore', title='...', msg='...', tags=['lesson'], links=['src/a.py'])\n"
        "  add(type='doc',  title='...', items=['a','b','c'], links=['lr-x'])\n"
        "  add(type='doc',  title='...', links=['dc-a','dc-b'], flow=True)  # 문서 여정 체인\n\n"
        "## type — lore | doc 2종뿐 (그 외 값은 거부)\n"
        "  lore: msg, tags, status, relates(supersede), items(dict list만=batch)\n"
        "  doc:  items, links(+flow), tags, status, relates(supersede)\n\n"
        "## supersede (옛 보존 + 새 head) — relates (lore/doc 공통)\n"
        "  add(type='lore', relates='lr-old', title='새 결정', msg='...')\n"
        "  add(type='doc',  relates='dc-old', title='새 버전', msg='...')\n"
        "  → 옛 항목 head=False(검색 제외), 새 항목이 head. tags/files 상속.\n"
        "  같은 콜의 items=(doc)/links=(id·파일경로 모두)/flow= 도 새 id 에 그대로 적용됨(2-pass 불필요).\n"
        "  cf. 모순을 *기존* 항목 Y 로 묶기만 = link(a=X, b='lr-Y'|'dc-Y', action='supersede')\n\n"
        "## status (lore/doc 공통) — 생명주기 딱지 (검색에 계속 뜸)\n"
        "  open(기본) 살아있음 · done 완료 · dropped 폐기 · rule 바뀌지 않는 기준(계속 유효)\n"
        "  ⚠️ done/dropped/rule 은 '딱지'라 검색에 계속 뜸. 그 외 값은 거부.\n"
        "  cf. 폐기하며 '대체본'을 함께 가리키면 자동 검색제외 (=supersede, 별도 개념 아님):\n"
        "     link(a=X, b='lr-Y', action='supersede')  — 대체본 링크가 검색노출을 가름\n"
        "     done=끝난 유효 지식(검색됨) · dropped=폐기+이유(검색됨) · dropped+대체본=옛버전(숨김)\n\n"
        "## 일괄 생성 (batch)\n"
        "  add(type='lore', items=[{{...}},{{...}}])  — items가 list[dict]면 batch\n"
        "  add(type='doc',  items=[{{...}},{{...}}])"
    ),

    "err_title_required": "오류: title 필수 — add(type='...', title='...', ...)",
    "err_lore_items_forbidden": (
        "오류: lore 는 체크리스트가 없습니다 — 체크리스트(items=['a','b'])는 doc 전용.\n"
        "  체크리스트가 필요하면: add(type='doc', title='...', items=['a','b'])\n"
        "  lore 본문은 msg=: add(type='lore', title='...', msg='내용')\n"
        "  batch 생성(items=[{{'title':...}},...] dict)은 lore·doc 둘 다 가능"
    ),
    "err_batch_title_conflict": (
        "오류: items=[{{...}}] (배치 생성)와 title=/msg= 를 함께 줄 수 없습니다 — 의도가 갈립니다.\n"
        "  · 여러 건 배치 생성: add(type='...', items=[{{'title':...}}, ...])  (title/msg 는 빼고)\n"
        "  · 한 건 생성 + 체크리스트: add(type='...', title='...', msg='...', items=['a','b'])  (문자열 리스트로)"
    ),
    "err_batch_links_conflict": (
        "오류: items=[{{...}}] (배치 생성)와 최상위 links=/push_to= 를 함께 줄 수 없습니다 — "
        "어느 항목에 적용할지 불명확합니다.\n"
        "  · 항목별 links: 각 item dict 안에 links= 를 넣으세요 — items=[{{'title':..., 'links':[...]}}, ...]\n"
        "  · 생성 후 전송: add(items=[...]) 로 먼저 만들고, 각 id 마다 openbox(name='...', action='push', id='<새id>') 호출"
    ),
    "err_flow_doc_only": "오류: flow는 doc 전용 — 문서 여정 체인 (lore 는 flow 없음).",
    "err_flow_files_forbidden": "오류: flow 체인 대상은 doc id/제목만 — 파일 경로 불가: {files}",
    "err_unknown_type": "오류: 알 수 없는 type '{t}'. doc | lore",

    "files_more_suffix": " 외 {n}",

    "auto_files_note": (
        "\n📎 파일 자동연결 (uncommitted diff): {files}"
        "\n   무관한 파일은 unlink(a='{id}', b='파일명') 로 개별 해제"
    ),
    "explicit_files_note": "\n📎 파일 연결: {files}",

    "link_ok": "  ↔ {target}",
    "link_fail": "  ⚠️ link({target}) 실패: {err}",
    "link_summary_header": "\n🔗 연결됨 (links=):\n",

    "push_to_fail": "\n  ⚠️ push_to 처리 실패: {err}",
    "push_to_unregistered": "  ⚠️ source '{name}' 미등록",
    "push_to_line": "  → {result}",

    "batch_streak_hint": (
        "\n💡 같은 type 단건 add() {n}회 연속 — 다건 생성은 items=[{{...}}] 배치가 넛지 조용합니다 "
        "(남은 건부터 배치 전환 가능). 이 안내는 세션당 1회."
    ),
}
