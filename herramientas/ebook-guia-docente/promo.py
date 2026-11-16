import re,base64
F='file:///tmp/cce/fonts/'
logo=open('/tmp/cce/fix9/logo.svg').read()
def lg(w,h): return re.sub(r'width="\d+" height="\d+"','width="%d" height="%d"'%(w,h),logo)
cov='data:image/png;base64,'+base64.b64encode(open('/tmp/cce/ebd/out/img/og-ebook-gdoc-portada.png','rb').read()).decode()
p2='data:image/png;base64,'+base64.b64encode(open('/tmp/cce/ebd/out/img/og-ebook-gdoc-p2.png','rb').read()).decode()
FONTS='''@font-face{font-family:I;src:url(%sinter.woff2)}@font-face{font-family:PS;font-weight:700;src:url(%sps700.woff2)}@font-face{font-family:S;font-weight:700;src:url(%sserif7.woff2)}@font-face{font-family:M;font-weight:600;src:url(%smono6.woff2)}*{margin:0;box-sizing:border-box}'''%(F,F,F,F)
fb='''<!doctype html><meta charset="utf-8"><style>%s
body{width:1080px;height:1350px;overflow:hidden;background:#fff;font-family:I;color:#0B1B3F}
.top{display:flex;align-items:center;gap:22px;padding:56px 64px 0}.top b{font:700 46px/1 S;letter-spacing:.03em;display:block}.top em{font:600 20px M;letter-spacing:.42em;color:#0F8F86;font-style:normal;display:block;margin-top:10px}
.band{margin:44px 0 0;background:#0B1B3F;padding:30px 64px 34px;position:relative}
.band .eb{display:inline-block;background:#F6C445;color:#0B1B3F;font:700 112px/1 PS;padding:14px 30px 18px;border-radius:18px;letter-spacing:.01em;transform:rotate(-2deg)}
.band h1{color:#fff;font:700 62px/1.05 PS;margin-top:26px}.band h1 span{color:#2DD4BF}
.mid{display:flex;gap:40px;padding:44px 64px 0;align-items:flex-start}
.mid .bk{flex:none;width:380px;position:relative}
.mid .bk img{width:100%%;display:block;border-radius:10px;box-shadow:14px 14px 0 #2DD4BF,0 20px 40px rgba(11,27,63,.25);transform:rotate(-3deg)}
.mid ul{list-style:none;padding:0;margin:6px 0 0}.mid li{display:flex;gap:16px;font:600 31px/1.25 I;margin-bottom:26px}.mid li i{flex:none;width:44px;height:44px;border-radius:50%%;background:#12A05A;color:#fff;font:700 26px/44px PS;text-align:center;font-style:normal}
.ft{position:absolute;left:0;right:0;bottom:0;background:#F6C445;padding:26px 64px;display:flex;justify-content:space-between;align-items:center}
.ft .u{font:700 44px S}.ft .u span{color:#0F6E68}.ft .d{font:700 26px PS;text-align:right}
</style>
<div class="top">%s<div><b>CONCURSOS</b><em>DEL ESTADO</em></div></div>
<div class="band"><span class="eb">EBOOK GRATIS</span><h1>Guía de estudio<br><span>Concurso docente 2026</span></h1></div>
<div class="mid"><div class="bk"><img src="%s"></div><ul>
<li><i>✓</i>Qué evalúa la prueba eliminatoria, componente por componente</li>
<li><i>✓</i>Las normas que todo docente debe dominar, explicadas</li>
<li><i>✓</i>7 casos resueltos con su porqué</li>
<li><i>✓</i>Plan de estudio y glosario</li></ul></div>
<div class="ft"><div class="u">concursosdelestado<span>.com</span></div><div class="d">24 páginas · PDF<br>Llega a tu correo</div></div>'''%(FONTS,lg(118,110),cov)
og='''<!doctype html><meta charset="utf-8"><style>%s
body{width:1200px;height:630px;overflow:hidden;font-family:I;color:#fff;background:radial-gradient(520px 420px at 1040px 60px,rgba(45,212,191,.28),transparent 70%%),linear-gradient(135deg,#0B1B3F,#0A2A63 60%%,#0B1B3F)}
.c{position:relative;height:630px;padding:56px 70px}
.br{display:flex;align-items:center;gap:16px}.br .ic{width:84px;height:80px;background:#fff;border-radius:16px;display:grid;place-items:center}.br b{display:block;font:700 33px/1 S;letter-spacing:.03em}.br em{display:block;font:600 17px/1 M;letter-spacing:.42em;color:#2DD4BF;font-style:normal;margin-top:8px}
.eb{display:inline-block;margin-top:44px;background:#F6C445;color:#0B1B3F;font:700 40px/1 PS;padding:12px 20px;border-radius:12px}
h1{margin-top:22px;font:700 60px/1.06 PS;max-width:640px}h1 span{color:#F6C445}
.u{position:absolute;left:70px;bottom:46px;font:700 32px S}.u span{color:#2DD4BF}
img{position:absolute;right:90px;top:70px;width:330px;border-radius:10px;box-shadow:12px 12px 0 #2DD4BF;transform:rotate(3deg)}
</style><div class="c"><div class="br"><div class="ic">%s</div><div><b>CONCURSOS</b><em>DEL ESTADO</em></div></div><div class="eb">EBOOK GRATIS</div><h1>Guía de estudio<br><span>Concurso docente 2026</span></h1><div class="u">concursosdelestado<span>.com</span></div><img src="%s"></div>'''%(FONTS,lg(62,58),cov)
open('/tmp/cce/ebd/out/fb.html','w').write(fb);open('/tmp/cce/ebd/out/og.html','w').write(og)
