# 스마트팩토리 MES: 문제를 사람보다 먼저 보는 법 — learn-mes-yhk

자동차 부품사 재직자가 ISA-95 층 지도, OEE 계산, 선행 신호 비교를 4블록(약 75분)으로 배우고 결과 대시보드를 공개하는 강의다. 수업은 Claude Code 스킬 `/learn-mes-yhk`가 진행한다 (Skills as Curriculum). 이 강의는 yhk가 course-forge로 직접 만들었다.

- **결과 대시보드**: https://yunhakim17.github.io/learn-mes-yhk/
- **교재 PDF**: [docs/Smart_Factory_MES_Textbook.pdf](docs/Smart_Factory_MES_Textbook.pdf) · **강의 덱 PDF**: [docs/Smart_Factory_MES_Deck.pdf](docs/Smart_Factory_MES_Deck.pdf)
- 처음이면 [GUIDE.md](GUIDE.md)부터. 기본 환경은 Claude 데스크톱 앱(Code 탭). VS Code는 GUIDE 부록 B

## 설치 — 한 줄

Claude Code 입력칸에 붙여 넣는다.

```
npx skills add yunhakim17/learn-mes-yhk --agent claude-code --global --yes 를 실행해 줘
```

새 세션에서 `/learn-mes-yhk`를 입력하면 수업이 시작된다. zip을 받았다면 GUIDE.md 2단계대로 설치한다.

## 블록

| Block | 주제 | 끝나면 생기는 것 |
|---|---|---|
| 0 | 준비 — 작업 폴더·facts.csv·Python | `~/mes-lab` · `env_check.txt` |
| 1 | MES 데이터 지도 — ISA-95 다섯 층과 MESA-11 | `out/ch1_map.md` · `out/ch1_map.json` |
| 2 | 데이터 연결 — OEE 계산과 차트 | `out/ch2_oee.json` · `out/ch2_oee.png` |
| 3 | 먼저 보는 신호 — 성과 비교 · 대시보드 · 공개 | `out/ch3_compare.json` · `index.html` · 공개 주소 |

## 수업 방식

| 구분 | 내용 |
|---|---|
| 목표 — AI Native | AI에게 맡기는 것이 기본인 방식으로 일한다 |
| 방법 — Skills as Curriculum | 스킬이 블록마다 설명 → 실습 → STOP → 확인·퀴즈를 진행한다 |
| 형식 — 자율학습 | 강사 없이 자기 속도로, 퀴즈로 스스로 점검한다 |

## 원본 강의와 데이터 출처

| 자료 | 출처 | 구분 |
|---|---|---|
| 교재 3장 · 강의 덱 | yhk가 만든 「스마트팩토리 MES」 교재·덱 (`docs/`) | 내 업무 주제 |
| `facts.csv` | 공개 보도·표준 단체·시장조사 보도자료에서 뽑은 숫자 24건, 출처 S1~S16 (`.claude/skills/learn-mes-yhk/assets/lab/sources.md`) | 실데이터 (가상 데이터 없음) |
| 미확보 | 부품사 실제 MES 로그, 도입 후 불량률·리드타임 수치 | 공개 자료 없음 |

## 개정 이력

| 날짜 | 바뀐 점 |
|---|---|
| 2026-10-31 | 첫 판 — 4블록 · 퀴즈 3문항 · 결과 대시보드 |

## 만든 방법

- `/course-forge`로 만들었다. 제작 기록(원본 요약·커리큘럼·검수 결과)은 `forge/`에 있다.
- 강의 저장소 템플릿: https://github.com/keerhee/kma-auto-genai-3-1
