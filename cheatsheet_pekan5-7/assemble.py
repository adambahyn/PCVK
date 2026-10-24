import json, os, re, subprocess
import pymupdf as fitz

D = "C:/Users/adamb/AppData/Local/hermes/cache/scratch/pcvk/"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
FS = float(os.environ.get("FS", "10.3"))

atoms = json.load(open(D + "atoms.json", encoding="utf-8"))
assign = json.load(open(D + "assign_final.json", encoding="utf-8"))
assign = {int(k): v for k, v in assign.items()}

CSS = f"""@page{{size:33.5mm 297mm;margin:0;}}
*{{box-sizing:border-box;}}
html,body{{margin:0;padding:0;width:33.5mm;}}
body{{font-family:"DejaVu Sans","Segoe UI",Arial,sans-serif;font-size:{FS}pt;line-height:1.03;color:#000;padding:1.2mm 1.1mm;}}
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

os.makedirs(D + "final", exist_ok=True)
pdfs = []
for k in range(12):
    body = ''.join(atoms[i] for i in sorted(assign[k]))
    html = ("<!DOCTYPE html><html lang='id'><head><meta charset='utf-8'><style>" + CSS
            + "</style></head><body>" + body + "</body></html>")
    hp = D + f"final/c{k}.html"
    open(hp, "w", encoding="utf-8").write(html)
    pp = D + f"final/c{k}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pp}", hp], capture_output=True)
    pdfs.append(pp)

# page geometry: A4 595x842pt, 6 columns of 33.5mm, vertically centred
COLW = 33.5 * 72 / 25.4          # 94.96 pt
GUT = (595.0 - 6 * COLW) / 7.0   # gutter
out = fitz.open()
for pi in (0, 1):
    page = out.new_page(width=595, height=842)
    for k in range(6):
        src = fitz.open(pdfs[pi * 6 + k])
        x = GUT + k * (COLW + GUT)
        target = fitz.Rect(x, 3, x + COLW, 839)
        page.show_pdf_page(target, src, 0)
        src.close()
out.save(D + "cheatsheet_PCVK_pekan5-7.pdf")
print("pages", out.page_count, "colw", round(COLW, 1), "gut", round(GUT, 2),
      "size", round(os.path.getsize(D + "cheatsheet_PCVK_pekan5-7.pdf") / 1024), "KB")
