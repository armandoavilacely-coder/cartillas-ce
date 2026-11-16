# -*- coding: utf-8 -*-
import json,re
logo=open('/tmp/cce/fix9/logo.svg').read()
logo=re.sub(r'width="\d+" height="\d+"','width="62" height="58"',logo)
N=[
('noticia-dian-2676-resultados-prueba-escrita-noviembre','DIAN 2676','#12A05A','Resultados de la prueba escrita','Se esperan del 21 al 30 de noviembre','16 nov 2026'),
('noticia-dian-prueba-escrita-8-noviembre','DIAN 2676','#12A05A','Ya se presentó la prueba escrita','218.051 citados en 51 ciudades','10 nov 2026'),
('noticia-procuraduria-cronograma-lista-definitiva-30-noviembre','Procuraduría 2026','#C23A4B','Calendario hasta la lista definitiva de admitidos','Lista definitiva: 30 de noviembre','8 nov 2026'),
('noticia-car-inscripciones-aplazadas-31-diciembre','Concurso CAR','#3E9A37','Las inscripciones siguen aplazadas','La CNSC aún no da nueva fecha','10 nov 2026'),
('noticia-concurso-docente-2026-28000-vacantes','Docentes 2026','#3B82D6','Inscripción de vacantes para personas con discapacidad','Del 23 de noviembre al 15 de enero','9 nov 2026'),
]
F='/tmp/cce/fonts/'
CSS='''@font-face{font-family:I;src:url(%sinter.woff2)}@font-face{font-family:PS;font-weight:700;src:url(%sps700.woff2)}@font-face{font-family:PS;font-weight:600;src:url(%sps600.woff2)}@font-face{font-family:S;font-weight:700;src:url(%sserif7.woff2)}@font-face{font-family:M;font-weight:600;src:url(%smono6.woff2)}
*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;overflow:hidden}
.c{position:relative;width:1200px;height:630px;padding:56px 70px;color:#fff;background:radial-gradient(520px 420px at 1040px 60px,rgba(45,212,191,.28),transparent 70%),linear-gradient(135deg,#0B1B3F,#0A2A63 60%,#0B1B3F);font-family:I;overflow:hidden}
.c:before{content:"";position:absolute;right:-160px;top:-260px;width:560px;height:560px;border-radius:50%%;border:2px solid rgba(255,255,255,.10)}
.bar{position:absolute;left:0;top:0;width:100%%;height:12px;background:var(--k)}
.top{display:flex;align-items:center;justify-content:space-between}
.br{display:flex;align-items:center;gap:16px}.br .ic{width:84px;height:80px;background:#fff;border-radius:16px;display:grid;place-items:center}
.br b{display:block;font:700 33px/1 S;letter-spacing:.03em}.br em{display:block;font:600 17px/1 M;letter-spacing:.42em;color:#2DD4BF;font-style:normal;margin-top:8px}
.tag{font:600 20px/1 M;letter-spacing:.2em;text-transform:uppercase;background:var(--k);padding:12px 18px;border-radius:8px}
.kick{margin-top:52px;font:600 22px/1 M;letter-spacing:.22em;text-transform:uppercase;color:#F6C445}
h1{margin-top:18px;font:700 66px/1.06 PS;letter-spacing:-.015em;max-width:1000px}
.dato{display:inline-flex;align-items:center;gap:14px;margin-top:28px;background:#F6C445;color:#0B1B3F;font:700 32px/1 PS;padding:16px 24px;border-radius:12px}
.dato i{width:14px;height:14px;border-radius:50%%;background:#0B1B3F;display:block}
.ft{position:absolute;left:70px;right:70px;bottom:46px;display:flex;justify-content:space-between;align-items:baseline}
.ft .u{font:700 34px/1 S}.ft .u span{color:#2DD4BF}.ft .d{font:600 20px/1 M;letter-spacing:.12em;color:#C9D4EA;text-transform:uppercase}
'''.replace('%%','%').replace('%s',F)
for slug,tag,k,h,dato,d in N:
    small=' style="font-size:60px"' if len(h)>40 else ' style="font-size:80px"' if len(h)<34 else ''
    html='<!doctype html><meta charset="utf-8"><style>%s</style><div class="c" style="--k:%s"><div class="bar"></div><div class="top"><div class="br"><div class="ic">%s</div><div><b>CONCURSOS</b><em>DEL ESTADO</em></div></div><div class="tag">%s</div></div><p class="kick">Noticia</p><h1%s>%s</h1><div class="dato"><i></i>%s</div><div class="ft"><div class="u">concursosdelestado<span>.com</span></div><div class="d">%s</div></div></div>'%(CSS,k,logo,tag,small,h,dato,d)
    open('/tmp/cce/fix9/og/'+slug+'.html','w',encoding='utf-8').write(html)
json.dump([n[0] for n in N],open('/tmp/cce/fix9/og/list.json','w'))
