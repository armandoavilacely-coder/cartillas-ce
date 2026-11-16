# -*- coding: utf-8 -*-
# Ilustraciones SVG propias del ebook (estilo plano, colores de la marca).
NV='#0B1B3F';BL='#2A6FC4';TL='#2DD4BF';GD='#F6C445';GR='#12A05A';RD='#C23A4B';LB='#EEF4FF';SK='#F2C6A0';SK2='#C98E62';WH='#FFFFFF';GY='#DCE2EE'

def svg(w,h,body,vb=None):
    vb=vb or '0 0 %d %d'%(w,h)
    return '<svg viewBox="%s" width="100%%" style="display:block" xmlns="http://www.w3.org/2000/svg" role="img">%s</svg>'%(vb,body)

def person(x,y,s=1,shirt=BL,skin=SK,hair=NV,arm=None):
    # persona sencilla: cabeza, pelo, torso redondeado
    return ('<g transform="translate(%s %s) scale(%s)">'
     '<rect x="-26" y="34" width="52" height="62" rx="22" fill="%s"/>'
     '<rect x="-7" y="24" width="14" height="14" fill="%s"/>'
     '<circle cx="0" cy="12" r="18" fill="%s"/>'
     '<path d="M-18 10 a18 18 0 0 1 36 0 q-6 -9 -18 -9 q-12 0 -18 9z" fill="%s"/>'
     '%s</g>')%(x,y,s,shirt,skin,skin,hair,arm or '')

def cover_scene():
    b=('<rect x="0" y="0" width="520" height="300" rx="24" fill="#12306B" opacity=".55"/>'
       # tablero
       '<rect x="40" y="40" width="250" height="150" rx="10" fill="#0E3B2E" stroke="#8A5A2B" stroke-width="10"/>'
       '<text x="62" y="88" font-family="PS" font-size="26" fill="#EAF0FF">a² + b² = c²</text>'
       '<path d="M62 110 h120" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
       '<path d="M62 132 h170" stroke="#EAF0FF" stroke-width="4" stroke-linecap="round" opacity=".7"/>'
       '<path d="M62 152 h90" stroke="#EAF0FF" stroke-width="4" stroke-linecap="round" opacity=".7"/>'
       '<circle cx="250" cy="150" r="20" fill="none" stroke="%s" stroke-width="5"/><path d="M240 150 l7 7 l14 -16" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>'
       % (GD,TL,TL))
    b+=person(360,120,1.25,shirt=GR,arm='<path d="M-24 50 q-30 -20 -48 -50" stroke="%s" stroke-width="13" stroke-linecap="round" fill="none"/>'%GR)
    # libros
    b+=('<rect x="300" y="230" width="190" height="22" rx="4" fill="%s"/><rect x="315" y="208" width="160" height="22" rx="4" fill="%s"/><rect x="330" y="186" width="130" height="22" rx="4" fill="%s"/>'
        '<path d="M450 190 l40 -60 l12 8 l-40 60z" fill="%s"/><path d="M450 190 l-4 16 l14 -8z" fill="%s"/>'%(RD,BL,GD,GD,SK))
    return svg(520,300,b)

def pesos_chart():
    rows=[('Docentes',[(55,NV,'55 %'),(5,TL,'5'),(30,BL,'30 %'),(10,GD,'10')]),
          ('Directivos',[(55,NV,'55 %'),(10,TL,'10'),(25,BL,'25 %'),(10,GD,'10')])]
    b='';y=10
    for name,segs in rows:
        b+='<text x="0" y="%d" font-family="PS" font-size="20" fill="%s">%s</text>'%(y+33,NV,name)
        x=125
        for v,c,l in segs:
            w=v*4.0
            b+='<rect x="%.1f" y="%d" width="%.1f" height="50" fill="%s"/>'%(x,y,w-3,c)
            col=WH if c in (NV,BL) else NV
            b+='<text x="%.1f" y="%d" font-family="PS" font-size="18" fill="%s" text-anchor="middle">%s</text>'%(x+w/2-1.5,y+32,col,l)
            x+=w
        y+=70
    lg=[(NV,'Aptitudes y competencias básicas · eliminatoria'),(TL,'Psicotécnica'),(BL,'Valoración de antecedentes'),(GD,'Entrevista')]
    for i,(c,t) in enumerate(lg):
        ly=y+8+i*28
        b+='<rect x="125" y="%d" width="18" height="18" rx="3" fill="%s"/><text x="152" y="%d" font-family="I" font-size="16" fill="%s">%s</text>'%(ly,c,ly+15,NV,t)
    return svg(530,y+8+4*28,b)

def icon(kind,size=64):
    s={'leer':'<rect x="8" y="10" width="34" height="44" rx="4" fill="%s"/><path d="M15 22h20M15 30h20M15 38h12" stroke="%s" stroke-width="3" stroke-linecap="round"/><circle cx="42" cy="40" r="12" fill="none" stroke="%s" stroke-width="5"/><path d="M50 49 l9 9" stroke="%s" stroke-width="6" stroke-linecap="round"/>'%(WH,BL,NV,NV),
       'num':'<rect x="10" y="8" width="44" height="50" rx="6" fill="%s"/><rect x="16" y="14" width="32" height="12" rx="2" fill="%s"/><text x="45" y="24" font-family="PS" font-size="10" fill="%s" text-anchor="end">3,95</text>%s'%(NV,TL,NV,''.join('<circle cx="%d" cy="%d" r="3.6" fill="%s"/>'%(20+12*(i%3),34+10*(i//3),GD if i==8 else WH) for i in range(9))),
       'eti':'<path d="M32 8 l20 8 v16 c0 14 -10 22 -20 26 c-10 -4 -20 -12 -20 -26 v-16z" fill="%s"/><path d="M23 33 l7 7 l13 -15" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'%(GR,WH),
       'ped':'<path d="M6 26 l26 -14 l26 14 l-26 14z" fill="%s"/><path d="M16 32 v12 c0 5 32 5 32 0 v-12 l-16 8z" fill="%s"/><path d="M54 28 v16" stroke="%s" stroke-width="3"/><circle cx="54" cy="46" r="3.5" fill="%s"/>'%(NV,BL,GD,GD),
       'ley':'<path d="M32 10 v42 M18 52 h28" stroke="%s" stroke-width="4" stroke-linecap="round"/><path d="M12 22 h40" stroke="%s" stroke-width="4" stroke-linecap="round"/><path d="M12 22 l-7 16 h14z M52 22 l-7 16 h14z" fill="%s"/><circle cx="32" cy="10" r="4" fill="%s"/>'%(NV,NV,GD,GD),
       'eval':'<rect x="12" y="8" width="40" height="50" rx="5" fill="%s"/><rect x="24" y="4" width="16" height="9" rx="3" fill="%s"/><path d="M20 26 l4 4 l7 -8 M20 40 l4 4 l7 -8" stroke="%s" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="M36 27h10M36 41h10" stroke="%s" stroke-width="3.5" stroke-linecap="round"/>'%(WH,NV,GR,BL),
       'conv':'<circle cx="22" cy="24" r="10" fill="%s"/><circle cx="42" cy="24" r="10" fill="%s"/><path d="M8 54 c0 -14 28 -14 28 0z" fill="%s"/><path d="M28 54 c0 -14 28 -14 28 0z" fill="%s"/>'%(SK,SK2,BL,GR),
       'inc':'<circle cx="32" cy="32" r="22" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="8 5"/><circle cx="32" cy="12" r="6" fill="%s"/><circle cx="52" cy="38" r="6" fill="%s"/><circle cx="14" cy="40" r="6" fill="%s"/><path d="M26 34 q6 8 12 0" stroke="%s" stroke-width="4" fill="none" stroke-linecap="round"/>'%(TL,GD,RD,BL,NV),
       'cargo':'<rect x="6" y="40" width="52" height="16" rx="3" fill="%s"/><rect x="14" y="26" width="36" height="16" rx="3" fill="%s"/><rect x="22" y="12" width="20" height="16" rx="3" fill="%s"/>'%(BL,TL,GD),
       'mente':'<path d="M20 56 v-10 c-9 -5 -12 -14 -10 -22 c3 -12 15 -18 27 -16 c11 2 18 11 17 22 l5 8 h-6 v8 c0 4 -3 6 -7 6 h-6 v4z" fill="%s"/><circle cx="34" cy="27" r="7" fill="none" stroke="%s" stroke-width="4"/><path d="M34 15v5M34 34v5M22 27h5M41 27h5" stroke="%s" stroke-width="4" stroke-linecap="round"/>'%(NV,GD,GD),
       'lapiz':'<path d="M14 50 l30 -30 l8 8 l-30 30 h-8z" fill="%s"/><path d="M44 20 l5 -5 l8 8 l-5 5z" fill="%s"/><path d="M14 50 v8 h8z" fill="%s"/>'%(GD,RD,NV),
       'ruta':'<path d="M10 54 c20 0 10 -22 26 -22 s10 -20 22 -20" stroke="%s" stroke-width="5" fill="none" stroke-dasharray="7 6" stroke-linecap="round"/><circle cx="10" cy="54" r="6" fill="%s"/><path d="M52 4 v18 M52 4 l10 4 l-10 4" stroke="%s" stroke-width="3.5" fill="%s"/>'%(BL,GR,RD,RD),
       'libro':'<path d="M8 14 c10 -4 18 -4 24 2 v40 c-6 -6 -14 -6 -24 -2z" fill="%s"/><path d="M56 14 c-10 -4 -18 -4 -24 2 v40 c6 -6 14 -6 24 -2z" fill="%s"/>'%(BL,TL),
      }[kind]
    return '<svg viewBox="0 0 64 64" width="%d" height="%d" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">%s</svg>'%(size,size,s)

def semaforo():
    items=[('III',RD,'Presunto delito','Policía de Infancia y Adolescencia y autoridades'),('II',GD,'Repetido o daño sin incapacidad','Protocolo II: proteger, informar a las familias, reparar'),('I',GR,'Esporádico y sin daño','Protocolo I: mediar y reparar en el aula')]
    b='<rect x="0" y="0" width="90" height="250" rx="22" fill="%s"/>'%NV
    for i,(t,c,a,p) in enumerate(items):
        cy=45+i*80
        b+='<circle cx="45" cy="%d" r="31" fill="%s"/><text x="45" y="%d" font-family="PS" font-size="24" fill="%s" text-anchor="middle">%s</text>'%(cy,c,cy+9,WH if c!=GD else NV,t)
        b+='<path d="M90 %d h26" stroke="%s" stroke-width="4"/>'%(cy,c)
        b+='<rect x="118" y="%d" width="400" height="62" rx="10" fill="%s" stroke="%s" stroke-width="2"/>'%(cy-31,'#F6F8FC',c)
        b+='<text x="134" y="%d" font-family="PS" font-size="18" fill="%s">Tipo %s · %s</text>'%(cy-5,NV,t,a)
        b+='<text x="134" y="%d" font-family="I" font-size="14" fill="#33415C">%s</text>'%(cy+18,p)
    return svg(520,250,b)

def termometro():
    lv=[('Superior',GR),('Alto',BL),('Básico',GD),('Bajo',RD)]
    b='';w=128
    for i,(t,c) in enumerate(lv):
        x=i*(w+6)
        b+='<rect x="%d" y="22" width="%d" height="46" rx="8" fill="%s"/><text x="%d" y="52" font-family="PS" font-size="17" fill="%s" text-anchor="middle">%s</text>'%(x,w,c,x+w/2,NV if c==GD else WH,t)
    b+='<path d="M4 10 h520" stroke="%s" stroke-width="3" marker-end="url(#a)"/><defs><marker id="a" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10z" fill="%s"/></marker></defs>'%(GY,GY)
    b+='<text x="0" y="90" font-family="I" font-size="13" fill="#53607A">Supera los desempeños necesarios</text><text x="536" y="90" font-family="I" font-size="13" fill="#53607A" text-anchor="end">No los supera</text>'
    return svg(536,96,b)

def niveles_lectura():
    st=[('Literal','¿Qué dice?',BL),('Inferencial','¿Qué se deduce?',TL),('Crítico','¿Qué tan sólido es?',GD)]
    b=''
    for i,(t,q,c) in enumerate(st):
        x=i*170;y=110-i*40
        b+='<rect x="%d" y="%d" width="160" height="%d" rx="8" fill="%s"/>'%(x,y,150-y,c)
        b+='<text x="%d" y="%d" font-family="PS" font-size="19" fill="%s" text-anchor="middle">%s</text>'%(x+80,y+30,NV if c!=BL else WH,t)
        b+='<text x="%d" y="%d" font-family="I" font-size="14" fill="%s" text-anchor="middle">%s</text>'%(x+80,y+52,NV if c!=BL else WH,q)
    return svg(510,152,b)

def balanza():
    b=('<path d="M200 20 v120 M140 140 h120" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
       '<path d="M60 40 h280" stroke="%s" stroke-width="6" stroke-linecap="round" transform="rotate(-6 200 40)"/>'
       '<circle cx="200" cy="20" r="9" fill="%s"/>'
       '<path d="M70 32 l-30 50 h60z" fill="none" stroke="%s" stroke-width="3"/><path d="M30 82 a40 14 0 0 0 80 0z" fill="%s"/>'
       '<text x="70" y="110" font-family="PS" font-size="16" fill="%s" text-anchor="middle">Proyecto 50 %%</text>'
       '<path d="M330 50 l-30 50 h60z" fill="none" stroke="%s" stroke-width="3"/><path d="M290 100 a40 14 0 0 0 80 0z" fill="%s"/>'
       '<text x="330" y="128" font-family="PS" font-size="16" fill="%s" text-anchor="middle">Parcial 30 %% + taller 20 %%</text>')%(NV,NV,GD,NV,BL,NV,NV,TL,NV)
    return svg(400,150,b)

def escuela():
    b=('<rect x="60" y="70" width="300" height="140" fill="%s"/><path d="M40 75 l170 -60 l170 60z" fill="%s"/>'
       '<rect x="185" y="140" width="50" height="70" rx="4" fill="%s"/>'%(LB,RD,NV))
    for i in range(4):
        x=85+i*70+(30 if i>=2 else 0)
        if x>330: continue
        b+='<rect x="%d" y="95" width="40" height="34" rx="3" fill="%s"/>'%(x,BL)
    b+='<circle cx="210" cy="45" r="14" fill="%s"/><path d="M210 12 v-14 M210 -2 l18 6 l-18 6" stroke="%s" stroke-width="3" fill="%s"/>'%(WH,NV,GD)
    b+=person(420,110,0.9,shirt=GR)+person(470,118,0.8,shirt=GD)+person(10,112,0.9,shirt=BL)
    return svg(520,215,b,vb='-30 -10 540 225')

def roles():
    data=[('Rector',GD,'Dirige el colegio'),('Coordinador',TL,'Coordina lo académico y la convivencia'),('Docente de aula',BL,'Enseña a sus estudiantes'),('Orientador',GR,'Acompaña y orienta')]
    b=''
    for i,(t,c,d) in enumerate(data):
        x=i*132
        b+=person(x+60,10,0.75,shirt=c)
        b+='<text x="%d" y="112" font-family="PS" font-size="15" fill="%s" text-anchor="middle">%s</text>'%(x+60,NV,t)
    return svg(530,122,b)

def rueda7():
    import math
    comp=['Liderazgo','Comunicación','Trabajo en equipo','Negociación','Compromiso','Iniciativa','Orientación al logro']
    cols=[BL,TL,GR,GD,RD,'#7C5CCF','#E07A2F']
    b='<circle cx="250" cy="150" r="64" fill="%s"/><text x="250" y="146" font-family="PS" font-size="16" fill="%s" text-anchor="middle">7 competencias</text><text x="250" y="166" font-family="I" font-size="11.5" fill="%s" text-anchor="middle">comportamentales</text>'%(NV,WH,'#C9D4EA')
    for i,(t,c) in enumerate(zip(comp,cols)):
        a=-math.pi/2+i*2*math.pi/7;x=250+128*math.cos(a);y=150+112*math.sin(a)
        b+='<path d="M%.0f %.0f L%.0f %.0f" stroke="%s" stroke-width="3"/>'%(250+64*math.cos(a),150+64*math.sin(a),x,y,GY)
        b+='<circle cx="%.0f" cy="%.0f" r="13" fill="%s"/><text x="%.0f" y="%.0f" font-family="PS" font-size="13" fill="%s" text-anchor="middle">%s</text>'%(x,y,c,x,y+4,WH,i+1)
        anchor='start' if math.cos(a)>0.2 else ('end' if math.cos(a)<-0.2 else 'middle')
        dx=18 if anchor=='start' else (-18 if anchor=='end' else 0);dy=5 if anchor!='middle' else (-20 if y<150 else 30)
        b+='<text x="%.0f" y="%.0f" font-family="PS" font-size="15" fill="%s" text-anchor="%s">%s</text>'%(x+dx,y+dy,NV,anchor,t)
    return svg(640,300,b,vb='-70 0 640 300')

def camino():
    pts=[(30,150,'1','Base común',GR),(150,90,'2','Normas',BL),(270,150,'3','Tu cargo',TL),(390,90,'4','Competencias',GD),(500,150,'5','Simulacros',RD)]
    b='<path d="M30 150 C90 150 90 90 150 90 S210 150 270 150 S330 90 390 90 S450 150 500 150" stroke="%s" stroke-width="22" fill="none" stroke-linecap="round"/>'%GY
    b+='<path d="M30 150 C90 150 90 90 150 90 S210 150 270 150 S330 90 390 90 S450 150 500 150" stroke="%s" stroke-width="3" fill="none" stroke-dasharray="10 8"/>'%WH
    for x,y,n,t,c in pts:
        b+='<circle cx="%d" cy="%d" r="20" fill="%s"/><text x="%d" y="%d" font-family="PS" font-size="18" fill="%s" text-anchor="middle">%s</text>'%(x,y,c,x,y+6,NV if c==GD else WH,n)
        ty=y-32 if y>100 else y+44
        b+='<text x="%d" y="%d" font-family="PS" font-size="15" fill="%s" text-anchor="middle">%s</text>'%(x,ty,NV,t)
    b+='<path d="M552 150 v-60 M552 90 l26 9 l-26 9" stroke="%s" stroke-width="4" fill="%s"/><text x="562" y="80" font-family="PS" font-size="14" fill="%s" text-anchor="middle">Prueba</text>'%(NV,GD,NV)
    return svg(620,170,b,vb='-30 40 630 160')

def piar():
    p=[('Docente de aula',BL),('Docente de apoyo',TL),('Familia',GD),('Estudiante',GR)]
    b='<rect x="170" y="70" width="180" height="70" rx="12" fill="%s"/><text x="260" y="102" font-family="PS" font-size="22" fill="%s" text-anchor="middle">PIAR</text><text x="260" y="124" font-family="I" font-size="13" fill="%s" text-anchor="middle">primer trimestre</text>'%(NV,GD,'#C9D4EA')
    pos=[(50,30),(470,30),(50,170),(470,170)]
    for (t,c),(x,y) in zip(p,pos):
        b+=person(x,y-28,0.5,shirt=c)
        b+='<text x="%d" y="%d" font-family="PS" font-size="14" fill="%s" text-anchor="middle">%s</text>'%(x,y+40,NV,t)
        b+='<path d="M%d %d L%d %d" stroke="%s" stroke-width="3" stroke-dasharray="6 5"/>'%(x+(40 if x<260 else -40),y+5,(170 if x<260 else 350),105,GY)
    return svg(520,220,b,vb='0 -10 520 230')

def opener(num,title,text,items,art,color=BL):
    li=''.join('<li>%s</li>'%i for i in items)
    return ('<div class="op-top" style="background:linear-gradient(160deg,%s,#0B1B3F)"><div class="op-num">%s</div><div class="op-art">%s</div></div>'
            '<div class="op-body"><h1>%s</h1><p class="lead">%s</p><div class="op-list"><span class="lbl">En este capítulo</span><ul>%s</ul></div></div>')%(color,num,art,title,text,li)
