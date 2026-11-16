# -*- coding: utf-8 -*-
import re
F='file:///tmp/cce/fonts/'
logo=open('/tmp/cce/fix9/logo.svg').read()
def lg(w,h): return re.sub(r'width="\d+" height="\d+"','width="%d" height="%d"'%(w,h),logo)
CSS='''
@font-face{font-family:I;src:url({F}inter.woff2)}@font-face{font-family:PS;font-weight:700;src:url({F}ps700.woff2)}@font-face{font-family:PS;font-weight:600;src:url({F}ps600.woff2)}
@font-face{font-family:S;font-weight:700;src:url({F}serif7.woff2)}@font-face{font-family:S;font-weight:600;src:url({F}serif6.woff2)}@font-face{font-family:M;font-weight:600;src:url({F}mono6.woff2)}@font-face{font-family:M;font-weight:500;src:url({F}mono5.woff2)}
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}html,body{margin:0}
body{font-family:I,Arial,sans-serif;color:#14213D;font-size:12pt;line-height:1.45}
.pg{width:210mm;height:297mm;padding:18mm 17mm 20mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.pg:last-child{page-break-after:auto}
.hd{display:flex;justify-content:space-between;align-items:center;font:600 8.5pt M;letter-spacing:.14em;text-transform:uppercase;color:#6B7894;border-bottom:1px solid #DCE2EE;padding-bottom:3mm;margin-bottom:6mm}
.hd b{color:#0B1B3F}
.ft{position:absolute;left:17mm;right:17mm;bottom:9mm;display:flex;justify-content:space-between;font:500 8.5pt M;color:#6B7894}
.kick{font:600 9.5pt M;letter-spacing:.2em;text-transform:uppercase;color:#B5651D;margin:0 0 2mm}
h1{font:700 25pt/1.12 PS;margin:0 0 4mm;color:#0B1B3F;letter-spacing:-.01em}
h2{font:700 14.5pt/1.2 PS;margin:4.5mm 0 2mm;color:#0B1B3F}
h3{font:700 12.6pt/1.25 PS;margin:4mm 0 1.5mm;color:#0B1B3F}
p{margin:0 0 3mm}ul,ol{margin:0 0 3mm;padding-left:6mm}li{margin-bottom:1.4mm}
.lead{font-size:13.6pt;color:#33415C}
.box{border-radius:3mm;padding:3mm 4.5mm;margin:2.5mm 0 3mm}
.term{background:#EEF4FF;border-left:2mm solid #2A6FC4}
.norma{background:#FFF8E6;border-left:2mm solid #E0A800;font-size:11pt}
.norma .src{font:600 8.8pt M;letter-spacing:.06em;text-transform:uppercase;color:#8A5A00;display:block;margin-bottom:1.5mm}
.norma q{quotes:"«" "»";font-style:italic}
.simple{background:#EAF7EF;border-left:2mm solid #12A05A}
.exam{background:#0B1B3F;color:#fff}.exam b{color:#F6C445}
.lbl{font:600 8.8pt M;letter-spacing:.12em;text-transform:uppercase;display:block;margin-bottom:1.2mm}
.term .lbl{color:#2A6FC4}.simple .lbl{color:#0E7A43}.exam .lbl{color:#2DD4BF}
table{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:11.4pt}
th{background:#0B1B3F;color:#fff;font:700 10.5pt PS;text-align:left;padding:2.4mm 3mm}
td{border-bottom:1px solid #DCE2EE;padding:2.4mm 3mm;vertical-align:top}
tr:nth-child(even) td{background:#F6F8FC}
.big{font:700 22pt PS;color:#0B1B3F}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.card{border:1px solid #DCE2EE;border-radius:3mm;padding:3.5mm 4mm}
.card h3{margin-top:0}
.num{display:inline-grid;place-items:center;width:8mm;height:8mm;border-radius:50%;background:#F6C445;color:#0B1B3F;font:700 11pt PS;margin-right:2mm}
.case{border:1.5px solid #0B1B3F;border-radius:3mm;padding:3.5mm 4.5mm;margin-bottom:3.5mm}
.case .q{font-weight:600;margin-bottom:2mm}
.case ol{list-style:upper-alpha;margin:0}
.flow{display:flex;flex-direction:column;gap:1.5mm;margin:2mm 0 4mm}
.flow div{background:#F6F8FC;border:1px solid #DCE2EE;border-radius:2mm;padding:2mm 3.5mm}
.flow i{font-style:normal;text-align:center;color:#6B7894;line-height:1}
.tip{font-size:11pt;color:#53607A}
/* portada */
.cover{background:radial-gradient(130mm 110mm at 175mm 40mm,rgba(45,212,191,.30),transparent 70%),linear-gradient(150deg,#0B1B3F,#0A2A63 60%,#0B1B3F);color:#fff;padding:22mm 18mm}
.cover .br{display:flex;align-items:center;gap:4mm}.cover .ic{width:22mm;height:21mm;background:#fff;border-radius:4mm;display:grid;place-items:center}
.cover .br b{font:700 19pt/1 S;letter-spacing:.03em;display:block}.cover .br em{font:600 9.5pt M;letter-spacing:.42em;color:#2DD4BF;font-style:normal;display:block;margin-top:2mm}
.badge{display:inline-block;background:#F6C445;color:#0B1B3F;font:700 22pt PS;padding:3mm 6mm;border-radius:3mm;margin-top:30mm;letter-spacing:.02em}
.cover h1{color:#fff;font-size:40pt;margin-top:8mm;line-height:1.05}
.cover h1 span{color:#F6C445}
.cover .sub{font-size:15pt;color:#C9D4EA;max-width:150mm;margin-top:6mm}
.cover .chips{display:flex;flex-wrap:wrap;gap:2.5mm;margin-top:10mm}
.cover .chips span{border:1px solid rgba(255,255,255,.35);border-radius:99px;padding:1.8mm 4mm;font:600 10pt I}
.cover .foot{position:absolute;left:18mm;right:18mm;bottom:16mm;display:flex;justify-content:space-between;align-items:flex-end}
.cover .foot .u{font:700 17pt S}.cover .foot .u span{color:#2DD4BF}.cover .foot .d{font:600 9pt M;letter-spacing:.12em;color:#C9D4EA;text-transform:uppercase;text-align:right}
.cover .stats{position:absolute;left:18mm;right:18mm;bottom:40mm;display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}.cover .stats div{border-top:1.5mm solid #F6C445;padding-top:3mm;font-size:11pt;color:#C9D4EA}.cover .stats b{display:block;font:700 30pt/1 PS;color:#fff;margin-bottom:1.5mm}
.pic{position:absolute;top:24mm;right:17mm;width:19mm;height:19mm;border-radius:4mm;background:#EEF4FF;display:grid;place-items:center}.pic svg{width:15mm;height:15mm}
.pg:has(.pic) h1{max-width:calc(100% - 24mm)}
.op{padding:0}.op-top{height:150mm;position:relative;padding:16mm 17mm 10mm;display:flex;align-items:center;justify-content:center}
.op-num{position:absolute;top:12mm;left:17mm;font:600 10pt M;letter-spacing:.24em;text-transform:uppercase;color:#fff}
.op-art{width:100%;background:#fff;border-radius:6mm;padding:7mm}
.op-body{padding:10mm 17mm}.op-body h1{font-size:28pt}
.op-list{background:#F6F8FC;border-radius:3mm;padding:4mm 6mm;margin-top:4mm}.op-list .lbl{color:#B5651D}
.art{margin:2mm auto 3mm}
.cover .cart{position:absolute;left:18mm;right:18mm;top:180mm;display:flex;justify-content:center}.cover .cart svg{width:88mm !important}
.i4{display:grid;grid-template-columns:1fr 1fr;gap:6mm}.i4 div{display:flex;align-items:center;gap:4mm;background:#F6F8FC;border-radius:4mm;padding:4mm}.i4 b{font:700 14pt PS;color:#0B1B3F}
.end{background:linear-gradient(150deg,#0B1B3F,#0A2A63);color:#fff}
.end h1{color:#fff}.end .lead{color:#C9D4EA}
.end .cta{background:#F6C445;color:#0B1B3F;border-radius:3mm;padding:5mm 6mm;font:700 15pt PS;margin:6mm 0}
.end table td{border-color:rgba(255,255,255,.15);color:#fff}.end tr:nth-child(even) td{background:rgba(255,255,255,.05)}
.end th{background:#F6C445;color:#0B1B3F}
.legal{font-size:9.2pt;color:#AFC0DE;position:absolute;left:17mm;right:17mm;bottom:14mm}
'''.replace('{F}',F)
PAGES=[]
N=[0]
KEYS={}
def page(sec,body,cls='',key=None,ic=None):
    N[0]+=1;n=N[0]
    if key: KEYS[key]=n
    if ic: body='<div class="pic">%s</div>'%icon(ic,70)+body
    hd='' if cls else '<div class="hd"><span><b>Guía de estudio</b> · Concurso docente 2026</span><span>%s</span></div>'%sec
    ft='' if cls else '<div class="ft"><span>concursosdelestado.com</span><span>%d</span></div>'%n
    PAGES.append('<section class="pg %s">%s%s%s</section>'%(cls,hd,body,ft))
def T(term,txt): return '<div class="box term"><span class="lbl">Término</span><b>%s.</b> %s</div>'%(term,txt)
def NO(src,txt): return '<div class="box norma"><span class="src">%s</span><q>%s</q></div>'%(src,txt)
def SI(txt): return '<div class="box simple"><span class="lbl">En palabras simples</span>%s</div>'%txt
def EX(txt): return '<div class="box exam"><span class="lbl">Para la prueba</span>%s</div>'%txt
exec(open('/tmp/cce/ebd/ill.py',encoding='utf-8').read())
exec(open('/tmp/cce/ebd/content.py',encoding='utf-8').read())
body=''.join(PAGES)
import re as _re
body=_re.sub(r'\{p:(\w+)\}',lambda m:str(KEYS[m.group(1)]),body)
html='<!doctype html><html lang="es"><meta charset="utf-8"><title>Guía de estudio · Concurso docente 2026</title><style>%s</style><body>%s</body></html>'%(CSS,body)
open('/tmp/cce/ebd/out/guia.html','w',encoding='utf-8').write(html);print('pages',N[0])
