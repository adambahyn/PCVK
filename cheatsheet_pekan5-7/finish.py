import json, os, re, subprocess, statistics, sys
import pymupdf as fitz

D = "C:/Users/adamb/AppData/Local/hermes/cache/scratch/pcvk/"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
FS = float(sys.argv[1]) if len(sys.argv) > 1 else 11.5
CAP = 825.0

atoms = json.load(open(D + "atoms.json", encoding="utf-8"))
HR = json.load(open(D + "h11r.json", encoding="utf-8"))
HR = {int(k): v for k, v in HR.items()}
med = statistics.median(HR.values())
BASE = 11.0
S = FS / BASE
H = [HR.get(i, med) * S for i in range(len(atoms))]

CSS = f"""@page{{size:33.2mm 297mm;margin:0;}}
*{{box-sizing:border-box;}}
html,body{{margin:0;padding:0;width:33.2mm;}}
body{{font-family:"DejaVu Sans","Segoe UI",Arial,sans-serif;font-size:{FS}pt;line-height:1.03;color:#000;padding:1.2mm 1mm;}}
h2{{font-size:{FS*1.14}pt;margin:.9mm 0 .3mm;padding:.3mm .7mm;background:#000;color:#fff;text-transform:uppercase;}}
h3{{font-size:{FS*1.04}pt;margin:.7mm 0 .25mm;font-weight:bold;background:#d9d9d9;padding:.15mm .45mm;}}
p,ul,ol{{margin:.3mm 0;}}ul,ol{{padding-left:2.6mm;}}li{{margin:.06mm 0;}}
table.inn{{border-collapse:collapse;width:100%;margin:.35mm 0;font-size:{FS*0.95}pt;}}
.inn th,.inn td{{border:.4pt solid #666;padding:.18mm .4mm;vertical-align:top;}}
.inn th{{background:#e2e2e2;}}
.box{{border:.6pt solid #000;padding:.7mm;margin:.55mm 0;background:#f5f5f5;}}
.fx{{text-align:center;margin:.4mm 0;font-size:{FS*1.02}pt;font-family:"Cambria Math","DejaVu Serif",Georgia,serif;}}
.note{{background:#ebebeb;border-left:1.3pt solid #000;padding:.4mm .7mm;margin:.45mm 0;}}
code,kbd{{font-family:Consolas,monospace;font-size:{FS*0.93}pt;}}code{{background:#f0f0f0;}}
.hl{{background:#ffe066;}}
pre{{margin:.35mm 0;font-size:{FS*0.9}pt;line-height:1.03;white-space:pre-wrap;overflow-wrap:anywhere;}}
p,li,td,th,div,pre{{overflow-wrap:break-word;}}
"""

MARK = lambda i: f'<span style="font-size:1pt;color:#ffffff">KK{i}KK</span>'


def col_html(idxs):
    return ("<!DOCTYPE html><html lang='id'><head><meta charset='utf-8'><style>" + CSS
            + "</style></head><body>"
            + ''.join(atoms[i] + MARK(i) for i in idxs) + "</body></html>")


def col_height(idxs, tag):
    """render one column, return (max_y, measured per-atom heights)"""
    open(D + f"cols/x_{tag}.html", "w", encoding="utf-8").write(col_html(idxs))
    pdf = D + f"cols/x_{tag}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", D + f"cols/x_{tag}.html"],
                   capture_output=True)
    d = fitz.open(pdf)
    if d.page_count == 0:
        return 0, {}
    pg = d[0]
    ws = pg.get_text("words")
    marks = sorted(((int(m.group(1)), w[3]) for w in ws
                    for m in [re.fullmatch(r'KK(\d+)KK', w[4])] if m), key=lambda x: x[1])
    per = {}
    prev = 0.0
    for i, y in marks:
        per[i] = y - prev
        prev = y
    blocks = pg.get_text("blocks")
    ymax = max((b[3] for b in blocks), default=0)
    return ymax, per


# initial LPT pack
def lpt():
    n = 12
    a = [[] for _ in range(n)]
    load = [0.0] * n
    for i in sorted(range(len(atoms)), key=lambda i: -H[i]):
        j = min(range(n), key=lambda k: load[k])
        a[j].append(i)
        load[j] += H[i]
    for x in a:
        x.sort()
    return a


assign = lpt()
measured = list(H)
for it in range(7):
    ys = []
    for k in range(12):
        y, per = col_height(assign[k], f"i{it}c{k}")
        ys.append(y)
        for i, v in per.items():
            measured[i] = v * (H[i] / max(measured[i], 1e-6)) if measured[i] > 0 else v
    over = [k for k in range(12) if ys[k] > CAP - 2]
    print("iter", it, "ymax", [round(v) for v in ys], "over", over)
    if not over:
        break
    # move last atom of an overflowing column to the shortest column
    for k in over:
        if len(assign[k]) <= 1:
            continue
        move = assign[k].pop()
        tgt = min(range(12), key=lambda j: ys[j] if j != k else 1e9)
        assign[tgt].append(move)
        assign[tgt].sort()
        ys[tgt] += measured[move]
    # if any column is far shorter, pull the largest movable atom across
    if it == 6:
        lo_k = min(range(12), key=lambda k: ys[k])
        hi_k = max(range(12), key=lambda k: ys[k])
        if ys[hi_k] - ys[lo_k] > 90 and len(assign[hi_k]) > 2:
            cand = sorted(assign[hi_k], key=lambda i: -measured[i])[:3]
            for mv in cand:
                if measured[mv] < ys[hi_k] - ys[lo_k] and len(assign[hi_k]) > 2:
                    assign[hi_k].remove(mv)
                    assign[lo_k].append(mv)
                    assign[lo_k].sort()
                    break

json.dump({str(k): assign[k] for k in range(12)}, open(D + "assign_final.json", "w"))
print("final ymax", [round(v) for v in ys])
