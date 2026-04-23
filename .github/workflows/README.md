# 잡코리아(JobKorea) 채용공고 검색 기능 QA 포트폴리오

> 잡코리아 채용공고 검색 기능을 대상으로 수동 TC 설계·실행, JIRA 버그 등록,
> SauceDemo UI 자동화 및 Restful-Booker API 자동화를 구현하고
> GitHub Actions CI/CD 파이프라인을 구성한 QA 포트폴리오입니다.

---

## 📋 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 테스트 대상 | 잡코리아(JobKorea) 채용공고 검색 기능 |
| 자동화 환경 | SauceDemo (UI) · Restful-Booker (API) |
| 수동 TC | 25개 (P1/P2/P3/SEC 트랙 분리) |
| 자동화 TC | 12개 Pass (UI 7개 + API 5개) |
| 발견 버그 | 5건 (Major 1건 · Minor 4건) |
| CI/CD | GitHub Actions (매 push마다 자동 실행) |

---

## 🛠 기술 스택

| 구분 | 도구 |
|---|---|
| UI 자동화 | Playwright + pytest |
| API 자동화 | requests + pytest |
| CI/CD | GitHub Actions |
| 이슈 관리 | JIRA |
| TC 문서 | Excel (v4.0) |
| 언어 | Python 3.11 |

---

## 📁 프로젝트 구조

```
jobkorea-qa-portfolio/
│
├── .github/
│   └── workflows/
│       └── qa-automation.yml     # CI/CD 파이프라인
│
├── tests/
│   ├── conftest.py               # 공통 설정
│   ├── ui/                       # Playwright UI 자동화
│   │   ├── test_TC001_product_list.py
│   │   ├── test_TC002_filter.py
│   │   ├── test_TC004_empty_input.py
│   │   ├── test_TC009_filter_reset.py
│   │   └── test_TC013_sort.py
│   └── api/                      # requests API 자동화
│       └── test_booking.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🔗 수동 TC → 자동화 매핑

| 잡코리아 수동 TC | SauceDemo UI 매핑 | Restful-Booker API 매핑 |
|---|---|---|
| TC-001 키워드 검색 결과 표시 | 상품 목록 정상 표시 | GET /booking 목록 조회 |
| TC-002 필터 적용 | 가격 오름차순 정렬 필터 | GET /booking?firstname= |
| TC-004 빈 입력 처리 | 빈 로그인 오류 메시지 | POST 필수값 누락 오류 |
| TC-006 공백 입력 처리 | 공백 로그인 오류 메시지 | - |
| TC-009 필터 초기화 | 정렬 필터 기본값 복귀 | - |
| TC-013 정렬 기능 | 이름·가격 정렬 순서 확인 | - |
| TC-005 결과 기본 정보 | - | GET /booking/{id} 단건 조회 |
| TC-018 마지막 페이지 | - | DELETE 후 404 확인 |

---

## 🐛 발견된 버그 (JIRA)

| JIRA 티켓 | 내용 | 우선순위 | 심각도 |
|---|---|---|---|
| SCRUM-5 | 빈 검색어 입력 시 안내 메시지 미표시 | P1 | Minor |
| SCRUM-6 | 공백 스페이스 입력 시 안내 메시지 미표시 | P2 | Minor |
| SCRUM-7 | 필터 3개 이상 적용 시 고용형태 카드 미출력 | P2 | **Major** |
| SCRUM-8 | 필터 조합 결과 0건 시 필터 해제 유도 UI 미제공 | P2 | Minor |
| SCRUM-9 | 마지막 페이지 "다음" 버튼 비활성화 안 됨 | P2 | Minor |

---

## ✅ 테스트 결과

### UI 자동화 (SauceDemo) — 7개 Pass

| 테스트 | 매핑 TC | 결과 |
|---|---|---|
| test_produt_list_displayed | TC-001 | ✅ Pass |
| test_sort_filter_low_to_high | TC-002 | ✅ Pass |
| test_empty_username_shows_error | TC-004 | ✅ Pass |
| test_space_only_input | TC-006 | ✅ Pass |
| test_filter_reset_to_default | TC-009 | ✅ Pass |
| test_sort_name_a_to_z | TC-013 | ✅ Pass |
| test_sort_price_high_to_low | TC-013 | ✅ Pass |

### API 자동화 (Restful-Booker) — 5개 Pass

| 테스트 | 매핑 TC | 결과 |
|---|---|---|
| test_get_booking_list | TC-001 | ✅ Pass |
| test_filter_booking_by_name | TC-002 | ✅ Pass |
| test_get_single_booking | TC-005 | ✅ Pass |
| test_empty_required_field | TC-004 | ✅ Pass |
| test_delete_booking | TC-018 | ✅ Pass |

**총 12개 Pass / 0개 Fail**

---

## ⚙️ 실행 방법

```powershell
# 가상환경 활성화
.\venv\Scripts\Activate.ps1

# 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install chromium

# 전체 실행
pytest tests/ -v

# UI만 실행
pytest tests/ui/ -v

# API만 실행
pytest tests/api/ -v
```

---

## 🔄 CI/CD 파이프라인

`main` 브랜치에 `push`할 때마다 GitHub Actions가 자동 실행됩니다.

```
git push → GitHub Actions 자동 실행
         → UI 자동화 (Playwright) 실행
         → API 자동화 (requests) 실행
         → 결과 Actions 탭에서 확인
```

### 로컬 / CI 환경 자동 구분

```python
IS_CI = os.environ.get("CI", "false").lower() == "true"
browser = p.chromium.launch(headless=IS_CI)
# 로컬: headless=False (브라우저 창 표시)
# CI:   headless=True  (창 없이 실행)
```

---

## 📊 수동 TC 구성

| 트랙 | TC 수 | Pass | Fail | 실행 기준 |
|---|---|---|---|---|
| P1 핵심 기능 | 5개 | 4개 | 1개 | 매 빌드마다 |
| P2 일반 기능 | 13개 | 9개 | 4개 | 주요 릴리스마다 |
| P3 엣지케이스 | 2개 | 2개 | 0개 | 전체 점검 시 |
| SEC 보안 트랙 | 5개 | 5개 | 0개 | 릴리스 전 필수 |
| **합계** | **25개** | **20개** | **5개** | - |

> 보안 TC(SEC)는 법적 리스크 검토 후 실제 사이트 대신
> www.saucedemo.com 테스트 환경에서 진행하였습니다.