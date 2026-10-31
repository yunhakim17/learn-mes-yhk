# curriculum — learn-mes-yhk

- learn 이름: `learn-mes-yhk` — 주제(스마트팩토리 MES) + 만든 사람 이니셜(yhk). 사용자가 지정.
- 대상 · 시간 · 결과물: 자동차 부품사 재직자 · 약 75분 · GitHub Pages 대시보드 1장 + 교재·덱 PDF

## 블록

| Block | 제목 | 개념 (EXPLAIN) | 실습 (붙여 넣을 일) | 산출물 | 원본 강의 단계 | 시간 |
|---|---|---|---|---|---|---|
| 0 | 준비 | 작업 폴더·교재 PDF·facts.csv가 무엇인지 | 폴더 만들기 · facts.csv 복사 · Python 확인 | env_check.txt | 교재 표지·목차 | 10분 |
| 1 | MES 데이터 지도 | ISA-95 다섯 층, MES = Level 3, MESA-11 기능 11개 · 케이스: 삼성SDS 모터 라인 | facts.csv F01~F03으로 층별 데이터 지도 표 만들기 | out/ch1_map.md | 교재 1장 | 20분 |
| 2 | 데이터 연결 | OEE = 가용률×성능×품질, 월드클래스 85% · LOT 추적·SPC·OPC UA · 케이스: OEE 85% 거꾸로 읽기 | F08·F09로 OEE 계산 + 품질 99% 가정 재계산 + 차트 | out/ch2_oee.json · out/ch2_oee.png | 교재 2장 | 20분 |
| 3 | 먼저 보는 신호 | 후행 지표 vs 선행 지표 · 세 문제의 선행 신호 · 케이스: 태정기공 | F18·F20 성과 비교표 → 결과 대시보드 index.html → GitHub Pages 공개·공유 메시지 | out/ch3_compare.json · index.html · 공개 주소 | 교재 3장 | 25분 |

합계: 75분 (brief 약 75분)

## 퀴즈 주제 (판단형) — 교재 '생각해 볼 질문'이 재료

| Block | 물을 판단 |
|---|---|
| 0 | 퀴즈 없음 (course-forge 규칙: Block 0은 준비 블록) |
| 1 | 설비 알람이 다음 날 아침 ERP 납기 화면에 뜨는 공장 — 어느 층 사이 연결을 먼저 고칠까 (1장 질문 1) |
| 2 | 가용률 90 · 성능 95 · 품질 99인 라인의 OEE는 85%를 넘나, 무엇부터 볼까 (2장 질문 3 + 주의 1) |
| 3 | 경남 품질 +44.3% vs 전국 +42.5% — "경남이 더 잘했다"고 보고해도 되나 (3장 3.3 읽는 법) |

## 실습 MVP 계획

- 데이터: `assets/lab/facts.csv` (my-course/facts.csv 복사, 출처 S1~S16은 sources.md)
- 정답: `assets/answers/solve.py` → `expected.json`
- 확인할 핵심 수치: ISA-95 층 5 · MES Level 3 · MESA 기능 11 · OEE 85.4% · 품질 99%일 때 84.6% · 경남 최대 개선 지표 품질(44.3) · 전국 최대 개선 지표 품질(42.5)
- 대시보드: 세 블록 결과 + 교재·덱 PDF 링크 (docs/)

## 원본과 다르게 정한 곳

- **블록 4개** (사용자 지정). course-forge 기본인 "끝의 배포·공유 두 블록"은 따로 두지 않고 Block 3 실습 끝에 공개·공유를 넣는다.
- **Block 0 퀴즈 없음** — 사용자는 "블록마다 퀴즈"라고 했지만 course-forge 규칙상 준비 블록은 퀴즈가 없다. 퀴즈는 교재 3장에 대응하는 Block 1~3에 1문항씩.
- 교재에는 실습 단계가 없다 → 실습은 facts.csv 숫자로 교재의 표·계산을 다시 만들어 보는 것으로 한다. 교재에 없는 개념·숫자는 넣지 않는다.

## 위험과 가정

- 공개 저장소에는 교재·덱 PDF만 올린다. pptx·docx·캡처(PNG 미리보기)는 .gitignore.
- 부품사 실제 MES 로그는 〔미확보〕 → 가상 데이터도 만들지 않는다.
- GitHub 계정: 이 컴퓨터에 로그인된 `yunhakim17` → 예상 주소 https://yunhakim17.github.io/learn-mes-yhk/ (승인 ③에서 확정)
