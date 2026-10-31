# Block 0: 준비 — 작업 폴더·facts.csv·Python

> **Phase A 시작 시 그대로 출력한다:**
> ```
> 📖 공식 문서: https://docs.anthropic.com/en/docs/claude-code/overview
> ```

## EXPLAIN

### 1. 이 수업에서 쓰는 것

| 용어 | 뜻 |
|---|---|
| **작업 폴더** `~/mes-lab` | 실습 결과(`out/`)와 대시보드(`index.html`)가 쌓이는 곳. Block 3에서 이 폴더가 그대로 공개된다 |
| **facts.csv** | 교재에 쓴 숫자 24건을 모은 표. 칸: id · 장 · 주장 · 값 · 단위 · 기준연도 · 출처 · 교차확인 · 비고 |
| **출처 번호 [S1]~[S16]** | facts.csv의 숫자가 어디서 왔는지 가리키는 번호. 목록은 `sources.md` |
| **교차확인 / 단일출처 / 미확보** | 두 곳 이상에서 확인한 숫자 / 한 곳에만 있는 숫자 / 공개 자료를 찾지 못한 것 |

### 2. 왜 숫자를 표 하나에 모으나

| 기준 | 숫자를 문서마다 따로 적기 | facts.csv 한 곳에서 가져오기 |
|---|---|---|
| 같은 숫자가 문서마다 다를 때 | 어느 쪽이 맞는지 모른다 | 표가 기준이다 |
| 출처 확인 | 문서를 다시 뒤진다 | 같은 줄에 출처 번호가 있다 |
| 이 수업의 실습 | 손으로 옮기다 틀린다 | Claude가 표에서 읽어 계산하고, 우리는 결과만 확인한다 |

### 3. 케이스 — 공개 자료가 없는 숫자

교재를 만들 때 "자동차 부품사가 MES 도입 후 불량률·리드타임을 얼마나 줄였나"는 공개 사례에서 정량 수치를 찾지 못했다(facts.csv F15 · 미확보). 이 수업은 그런 숫자를 지어내지 않는다. 표에 '미확보'로 남기고, 실습은 공개된 숫자로만 한다.

## EXECUTE

아래 프롬프트를 붙여 넣으라고 안내한다. `{SKILL_DIR}`은 Phase A 출력 직전에 이 SKILL.md가 있는 폴더의 실제 경로로 바꿔 보여 준다.

```
MES 수업 실습 준비를 해 줘.
1. 내 홈 폴더에 mes-lab 폴더와 그 안에 out 폴더를 만들어 줘.
2. {SKILL_DIR}/assets/lab/ 의 facts.csv 와 sources.md 를 mes-lab 으로 복사해 줘. 원본은 고치지 마.
3. {SKILL_DIR}/assets/docs/ 의 PDF 두 개를 mes-lab/docs 로 복사해 줘.
4. Python이 있는지 확인하고, 없으면 설치 방법을 알려 줘(설치는 내 허락을 받고 해).
5. facts.csv 의 행 수, '교차확인'·'단일출처'·'미확보' 개수를 세어
   mes-lab/env_check.txt 에 Python 버전과 함께 적어 줘.
6. 비밀번호나 계정 정보는 묻지 마.
```

끝나면 데스크톱 앱에서 **새 세션 → Local → 폴더 선택 → `mes-lab`** 으로 새 세션을 열고, 그 세션에서 `/learn-mes-yhk`를 다시 불러 Block 1로 간다.

### 확인할 것 (Phase B)

- `~/mes-lab/facts.csv`, `~/mes-lab/sources.md`, `~/mes-lab/docs/*.pdf` 2개, `~/mes-lab/out/` 이 있다.
- `env_check.txt`에 Python 버전과 facts.csv 행 수 24 · 교차확인 13 · 단일출처 8 · 미확보 3가 적혀 있다.

막히면 "env_check.txt 의 숫자가 facts.csv 를 다시 세어 본 값과 같은지 확인하고, 다르면 원인을 찾아 줘"라는 후속 프롬프트를 준다. 정답은 "정답 보기" 요청이 있을 때만 연다.

## QUIZ

Block 0은 퀴즈가 없다. 확인이 끝나면 AskUserQuestion으로 Block 1 진행 여부를 묻는다.
