# 정답 스크립트 — facts.csv 가 있는 폴더에서 실행한다.
# 블록 1~3 산출물(out/*.json, out/ch2_oee.png)과 결과 대시보드(index.html), expected.json 을 만든다.
import csv, json, os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 설치된 한글 글꼴 중 첫 번째를 쓴다 (윈도우·맥·리눅스)
_have = {f.name for f in font_manager.fontManager.ttflist}
plt.rcParams["font.family"] = next((n for n in ["Malgun Gothic", "AppleGothic", "NanumGothic", "Noto Sans CJK KR",
                                                "Noto Sans CJK JP"] if n in _have), "DejaVu Sans")
plt.rcParams["axes.unicode_minus"] = False
os.makedirs("out", exist_ok=True)

with open("facts.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
facts = {r["id"]: r for r in rows}

def nums(s):
    """'+44.3 / +22.8 / -32.5' → [44.3, 22.8, -32.5]"""
    return [float(x) for x in re.findall(r"[-+]?\d+(?:\.\d+)?", s)]

# ---- Block 0: facts.csv 점검 ----
status = [r["교차확인"] for r in rows]
env = {"facts_rows": len(rows), "cross_checked": status.count("확인"),
       "single_source": status.count("단일출처"), "not_found": status.count("미확보")}

# ---- Block 1: ISA-95 층 지도 ----
ch1 = {"layers": int(facts["F01"]["값"]), "mes_level": int(facts["F02"]["값"]),
       "mesa_functions": int(facts["F03"]["값"])}
layers = [("Level 4", "경영·물류", "ERP", "수주량, 납기일, 자재 재고"),
          ("Level 3", "최종 제품을 만드는 작업 흐름", "MES", "작업 지시, 생산 실적, LOT 번호, 검사 결과"),
          ("Level 2", "공정 모니터링·제어", "PLC, DCS, SCADA", "설비 가동/비가동, 알람"),
          ("Level 1", "감지와 조작", "센서, 지능형 디바이스", "온도, 압력, 진동, 토크"),
          ("Level 0", "실제 물리 공정", "프레스, 용접기, 사출기", "(물리적 움직임 자체)")]
md = ["| 층 | 하는 일 | 대표 시스템 | 부품 공장 데이터 예 |", "|---|---|---|---|"]
for lv, role, sys_, data in layers:
    cells = [lv, role, sys_, data]
    if sys_ == "MES":
        cells = [f"**{c}**" for c in cells]
    md.append("| " + " | ".join(cells) + " |")
md.append("")
md.append(f"ISA-95 계층 수 {ch1['layers']}단계, MES 위치 Level {ch1['mes_level']} [S1][S2] · "
          f"MESA-11 핵심 기능 {ch1['mesa_functions']}개 [S2][S11]")
open("out/ch1_map.md", "w", encoding="utf-8").write("\n".join(md) + "\n")
json.dump(ch1, open("out/ch1_map.json", "w", encoding="utf-8"))

# ---- Block 2: OEE ----
a, p, q = nums(facts["F09"]["값"])
oee = round(a * p * q / 10000, 1)
oee99 = round(a * p * 99 / 10000, 1)          # 품질만 99%로 바꾼 경우
wc = float(facts["F08"]["값"])
ch2 = {"oee_world_class": oee, "oee_quality99": oee99}
json.dump(ch2, open("out/ch2_oee.json", "w", encoding="utf-8"))

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
vals = [a, p, q, oee]
bars = ax.bar(["가용률", "성능", "품질", "OEE"], vals, color=["#EAF1FB"] * 3 + ["#1B2C5E"], edgecolor="#1B2C5E")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v:g}%", ha="center", fontsize=12, weight="bold", color="#1B2C5E")
ax.axhline(wc, color="#C77700", ls="--", lw=2)
ax.text(-0.45, 106, f"- - 월드클래스 기준 {wc:g}%", color="#C77700", fontsize=11, weight="bold")
ax.set_ylim(0, 112)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, "출처: Tractian [S7], TeepTrak [S8] · facts.csv F08·F09", fontsize=9, color="#6B7280")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig("out/ch2_oee.png")
plt.close(fig)

# ---- Block 3: 두 조사의 최대 개선 지표 ----
def top(fid):
    labels = re.search(r"\(([^)]*)\)", facts[fid]["주장"]).group(1).split("·")
    vals = nums(facts[fid]["값"])
    k = max(range(len(vals)), key=lambda i: abs(vals[i]))   # 원가는 감소가 개선 → 절댓값
    return labels[k], abs(vals[k]), dict(zip(labels, vals))
g_name, g_val, g_all = top("F18")
n_name, n_val, n_all = top("F20")
ch3 = {"gyeongnam_top": g_name, "gyeongnam_top_value": g_val, "national_top": n_name, "national_top_value": n_val}
json.dump(ch3, open("out/ch3_compare.json", "w", encoding="utf-8"), ensure_ascii=False)

# ---- 결과 대시보드 ----
def row(name, d):
    return "<tr><th>" + name + "</th>" + "".join(
        f"<td>{d[k]:+.1f}%</td>" if k in d else "<td>—</td>" for k in ("품질", "생산성", "원가", "납기")) + "</tr>"
html = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>스마트팩토리 MES 실습 결과</title>
<style>
:root{{--navy:#1B2C5E;--amber:#C77700;--muted:#6B7280;--line:#D6D6DB;--tint:#EAF1FB}}
*{{box-sizing:border-box}} body{{margin:0;font-family:"Malgun Gothic","Apple SD Gothic Neo",sans-serif;color:#3B4252;background:#fff}}
header{{background:var(--navy);color:#fff;padding:28px 16px}} header h1{{margin:0 0 6px;font-size:1.6rem}} header p{{margin:0;color:#CADCFC}}
main{{max-width:960px;margin:0 auto;padding:16px}} h2{{color:var(--navy);font-size:1.2rem;border-bottom:2px solid var(--amber);padding-bottom:4px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.card{{background:var(--tint);padding:14px;border-radius:6px}} .card b{{display:block;font-size:1.7rem;color:var(--navy)}} .card span{{color:var(--muted);font-size:.9rem}}
img{{max-width:100%;height:auto}} table{{width:100%;border-collapse:collapse;font-size:.95rem}}
th,td{{border:1px solid var(--line);padding:6px;text-align:center}} thead th{{background:var(--navy);color:#fff}}
.note{{color:var(--muted);font-size:.9rem}} a{{color:var(--navy)}}
</style></head><body>
<header><h1>스마트팩토리 MES — 실습 결과</h1>
<p>MES는 Level {ch1['mes_level']}에서 납기와 품질 신호를 잇고, OEE {oee}%로 세 데이터를 묶고, 품질 신호를 먼저 본다.</p></header>
<main>
<h2>1장 MES 데이터 지도</h2>
<div class="cards">
<div class="card"><b>{ch1['layers']}층</b><span>ISA-95 계층 수 [S1][S2]</span></div>
<div class="card"><b>Level {ch1['mes_level']}</b><span>MES의 위치 [S1][S2]</span></div>
<div class="card"><b>{ch1['mesa_functions']}개</b><span>MESA-11 핵심 기능 [S2][S11]</span></div>
</div>
<h2>2장 데이터 연결 — OEE</h2>
<div class="cards">
<div class="card"><b>{oee}%</b><span>가용률 {a:g} × 성능 {p:g} × 품질 {q:g} [S7][S8]</span></div>
<div class="card"><b>{oee99}%</b><span>품질만 99%일 때 — 85%에 못 미침 [S7]</span></div>
</div>
<p><img src="out/ch2_oee.png" alt="월드클래스 OEE 구성 막대 차트"></p>
<h2>3장 먼저 보는 신호 — 도입 성과</h2>
<table><thead><tr><th>조사</th><th>품질</th><th>생산성</th><th>원가</th><th>납기</th></tr></thead><tbody>
{row("경남 439곳 (2022~2023 도입) [S13]", g_all)}
{row("전국 참여 기업 (2014~2018) [S15]", n_all)}
</tbody></table>
<p>두 조사 모두 개선 폭이 가장 큰 지표는 <b>{g_name}</b>({g_val:g}% · {n_val:g}%)이다. 대상·시기가 달라 숫자끼리 비교하지 않고 방향만 읽는다.</p>
<h2>교재와 출처</h2>
<p><a href="docs/Smart_Factory_MES_Textbook.pdf">교재 PDF</a> · <a href="docs/Smart_Factory_MES_Deck.pdf">강의 덱 PDF</a></p>
<p class="note">숫자는 모두 공개 자료에서 뽑은 facts.csv 값이다(가상 데이터 없음). 출처 번호 [S1]~[S16]의 목록은 교재 부록에 있다.
부품사 실제 MES 로그와 도입 후 불량률·리드타임 수치는 공개 자료를 찾지 못했다(미확보).</p>
</main></body></html>
"""
open("index.html", "w", encoding="utf-8").write(html)

# ---- expected.json ----
def v(val, d, block):
    return {"value": val, "decimals": d, "block": block}
expected = {"values": {
    "facts_rows": v(env["facts_rows"], 0, 0), "cross_checked": v(env["cross_checked"], 0, 0),
    "single_source": v(env["single_source"], 0, 0), "not_found": v(env["not_found"], 0, 0),
    "layers": v(ch1["layers"], 0, 1), "mes_level": v(ch1["mes_level"], 0, 1), "mesa_functions": v(ch1["mesa_functions"], 0, 1),
    "oee_world_class": v(oee, 1, 2), "oee_quality99": v(oee99, 1, 2),
    "gyeongnam_top": v(g_name, None, 3), "gyeongnam_top_value": v(g_val, 1, 3),
    "national_top": v(n_name, None, 3), "national_top_value": v(n_val, 1, 3)}}
json.dump(expected, open("expected.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: x["value"] for k, x in expected["values"].items()}, ensure_ascii=False))
