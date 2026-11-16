# -*- coding: utf-8 -*-
import re,json,gzip,hmac,hashlib,os,base64,brotli,sys,random
src=open("/tmp/cce/fix/abog.py",encoding="utf-8").read();exec(src[:src.index("def rezip")])  # la clave vive fuera del repo
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
ek=hashlib.sha256(b'enc'+key.encode()).digest();mk=hashlib.sha256(b'mac'+key.encode()).digest()
d=open('/tmp/cce/repo/cartilla.enc','rb').read();iv=d[3:19];mac=d[19:51];ct=d[51:]
assert hmac.compare_digest(mac,hmac.new(mk,iv+ct,hashlib.sha256).digest())
x=Cipher(algorithms.AES(ek),modes.CBC(iv)).decryptor();x=x.update(ct)+x.finalize()
u=padding.PKCS7(128).unpadder();x=u.update(x)+u.finalize()
h=gzip.decompress(x).decode('utf-8')
a=h.index('<script id="d-doc">')+19;e=h.index('</script>',a)
dd=h[a:e];pre='window.DOCDATA=';tail0=dd[len(pre):]
D,_end=json.JSONDecoder().raw_decode(tail0);suf=tail0[_end:]
assert json.dumps(D,ensure_ascii=False,separators=(',',':'))==tail0[:_end]
sys.path.insert(0,'/tmp/cce/fix7');import enr_e as M; import dir_b as OLD
B={b['id']:b for b in D['bloques']}
rng=random.Random(16112117)
nl=nq=0
oldq={q for _,q,*r in OLD.Q}
for bid,rep in M.REPL.items():
    idx={l['t']:l for l in B[bid]['lecciones']}
    for t,p in rep.items():
        if t in idx: idx[t]['p']=p; idx[t]['nuevo']=True
        else: B[bid]['lecciones'].append({'t':t,'p':p,'nuevo':True})
        nl+=1
    n0=len(B[bid]['preguntas']); B[bid]['preguntas']=[q for q in B[bid]['preguntas'] if q['q'] not in oldq]; print('preguntas viejas retiradas',n0-len(B[bid]['preguntas']))
    c0=len(B[bid]['conceptos']); B[bid]['conceptos']=[c for c in B[bid]['conceptos'] if c['t'] not in M.OLD_C_T]+M.C[bid]; print('conceptos',c0,'->',len(B[bid]['conceptos']))
    B[bid]['nuevo']='2026-11-16'
TL=["es lo que se hizo el año pasado","así se ahorra tiempo en el cronograma","lo recomendó un colega con experiencia","es la opción que menos tensiones genera","varios compañeros lo ven razonable","lo pide la urgencia del momento","es la práctica más común en otros colegios","así nadie se siente perjudicado"]
k=0
for bid,q,ok,bad,ex in M.Q:
    assert not any(x['q']==q for x in B[bid]['preguntas'])
    bad=bad[:];idx=list(range(len(bad)));rng.shuffle(idx)
    # Tanda B3: si la correcta es la más corta, se recorta la justificación (', porque…') de 1 o 2 distractores
    if len(ok)<min(map(len,bad)):
        for j in idx[:rng.choice([1,2,2,3])]:
            if ', porque' in bad[j]: bad[j]=bad[j].split(', porque')[0]
    for j in idx[:rng.choice([0,0,1,1,2,3])]:
        add=[]
        while len(bad[j])+sum(len(t)+3 for t in add)<len(ok)-8 and len(add)<2:
            add.append(TL[k%len(TL)]);k+=1
        if add: bad[j]=bad[j].rstrip('.')+' ('+'; '.join(add)+')'
    o=[ok]+bad; rng.shuffle(o)
    B[bid]['preguntas'].append({"q":q,"o":o,"a":o.index(ok),"e":ex,"nuevo":True}); nq+=1
print('lecciones',nl,'preguntas',nq)
import collections
for bid in M.REPL:
    n=sum(1 for x in M.Q if x[0]==bid);qs=B[bid]['preguntas'][-n:]
    print(bid,'pos',dict(collections.Counter(q['a'] for q in qs)),'larga',sum(1 for q in qs if len(q['o'][q['a']])==max(map(len,q['o']))),'corta',sum(1 for q in qs if len(q['o'][q['a']])==min(map(len,q['o']))),'total preg',len(B[bid]['preguntas']))
    for l in B[bid]['lecciones']:
        t=''.join(l['p'])
        for tag in ['table','tr','td','th','b','i','blockquote','div']: assert len(re.findall('<%s[ >]'%tag,t))==len(re.findall('</%s>'%tag,t)),(l['t'],tag)
new=pre+json.dumps(D,ensure_ascii=False,separators=(',',':'))+suf
h2=h[:a]+new+h[e:]
m=re.search(r'(<script type="application/x-br" id="br-ddoc">)(.*?)(</script>)',h2,re.S)
nb=base64.b64encode(brotli.compress(new.encode('utf-8'),quality=11)).decode()
h2=h2[:m.start(2)]+nb+h2[m.end(2):]
pos=h2.encode('utf-8').index(b'<script type="application/json" id="pub-data">')
h2=re.sub(r'<!--CE-PUB@\d+-->','<!--CE-PUB@%d-->'%pos,h2)
open('/tmp/cce/fix7/cartilla_new.html','w',encoding='utf-8').write(h2)
gz=gzip.compress(h2.encode('utf-8'),9,mtime=0)
iv=os.urandom(16);pd=padding.PKCS7(128).padder();data=pd.update(gz)+pd.finalize()
c=Cipher(algorithms.AES(ek),modes.CBC(iv)).encryptor();ct=c.update(data)+c.finalize()
open('/tmp/cce/fix7/cartilla.enc','wb').write(b'CE1'+iv+hmac.new(mk,iv+ct,hashlib.sha256).digest()+ct)
print('ok',os.path.getsize('/tmp/cce/fix7/cartilla.enc'),'CE-PUB',pos)
