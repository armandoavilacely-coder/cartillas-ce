# -*- coding: utf-8 -*-
import sys,html as H
COPY_DIAN='''📢 Concurso DIAN 2676: ¿cuándo salen los resultados de la prueba escrita?

Si presentaste el examen del domingo 8 de noviembre, los resultados iniciales se esperan entre el 21 y el 30 de noviembre en SIMO.

📌 Lo que debes saber:
✅ Tendrás 5 días hábiles para reclamar, solo por SIMO.
✅ Los resultados definitivos se esperan entre el 21 y el 30 de diciembre.
⚠️ La fecha exacta la confirma la CNSC; el rango sale del cronograma del contrato con el operador.

Revisa tu correo y tu cuenta de SIMO estos días.'''
SIG='\n\n✍️ concursosdelestado.com'
CSS='''<style>.ceshare{margin:1.6rem 0;padding:1rem 1.1rem;border:1px solid var(--line,#D5DBE7);border-radius:10px;background:var(--paper,#fff)}.ceshare h2{margin:0 0 .3rem;font-size:1.05rem}.ceshare p{margin:0 0 .8rem;font-size:.9rem;opacity:.8}.ceshare .sb{display:flex;flex-wrap:wrap;gap:.5rem}.ceshare button{display:inline-flex;align-items:center;gap:.45rem;border:0;border-radius:999px;padding:.55rem .95rem;font:600 .9rem/1 inherit;color:#fff;cursor:pointer;min-height:40px}.ceshare button svg{width:18px;height:18px;fill:currentColor}.ceshare .fb{background:#1877F2}.ceshare .wa{background:#1FA855}.ceshare .x{background:#111}.ceshare .li{background:#0A66C2}.ceshare .tg{background:#229ED9}.ceshare .cp{background:#E9EDF5;color:#0B1B3F}.ceshare button:focus-visible{outline:3px solid #F6C445;outline-offset:2px}#ceToast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:#0B1B3F;color:#fff;padding:.7rem 1rem;border-radius:8px;font-size:.92rem;z-index:99999;max-width:calc(100% - 32px);box-shadow:0 6px 24px rgba(0,0,0,.25);opacity:0;transition:opacity .2s;pointer-events:none}#ceToast.on{opacity:1}</style>'''
I={'fb':'<path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.4V11H7v4h3v9h4v-9h3l1-4h-4V8.6c0-.4.3-.6.6-.6z"/>',
'wa':'<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-3.3-1.1-5.5-4.4-5.7-4.6-.2-.2-1.3-1.8-1.3-3.4s.8-2.4 1.2-2.7c.3-.3.6-.4.8-.4h.6c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .6l-.4.6-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.4 1.8 2.2 1.2 1.1 2.3 1.4 2.6 1.6.3.1.5.1.7-.1l1-1.2c.2-.3.4-.2.7-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.2 1.5z"/>',
'x':'<path d="M17.8 3H21l-7 8 8.2 10H16l-5-6.2L5.4 21H2.2l7.5-8.6L2 3h6.4l4.5 5.7zm-1.1 16h1.7L7.4 4.8H5.6z"/>',
'li':'<path d="M4.5 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM3 9h3v12H3zm6 0h2.9v1.7c.4-.8 1.4-1.9 3.4-1.9 3.6 0 4.2 2.3 4.2 5.3V21h-3v-6c0-1.4 0-3.3-2-3.3s-2.4 1.6-2.4 3.2V21H9z"/>',
'tg':'<path d="M21.5 3.6 2.9 10.8c-1.3.5-1.2 1.2-.2 1.5l4.8 1.5 1.8 5.6c.2.6.4.8.9.8.4 0 .6-.2.9-.4l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.2-15c.3-1.3-.5-1.9-1.6-1.4zM8.6 13.4l9.3-5.9-7.2 6.8-.3 3.2z"/>',
'cp':'<path d="M16 1H4a2 2 0 0 0-2 2v14h2V3h12zm3 4H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm0 16H8V7h11z"/>'}
L=[('fb','Facebook'),('wa','WhatsApp'),('x','X'),('li','LinkedIn'),('tg','Telegram'),('cp','Copiar resumen')]
JS='''<script id="ce-share-js">(function(){var src=document.getElementById('ce-copy');if(!src)return;var t=src.textContent.trim(),sig='\\n\\n\\u270D\\uFE0F concursosdelestado.com',e=encodeURIComponent;
function base(){var c=document.querySelector('link[rel="canonical"]');return (c?c.href:location.origin+location.pathname).split('#')[0].split('?')[0]}
function url(n){return base()+'?f='+n}
function txt(n){return t+'\\n\\n\\uD83D\\uDD17 '+url(n)+sig}
function track(n){try{if(window.fbq)fbq('trackCustom','Share',{method:n})}catch(x){}}
function toast(m){var d=document.getElementById('ceToast');if(!d){d=document.createElement('div');d.id='ceToast';d.setAttribute('role','status');document.body.appendChild(d);}d.textContent=m;d.classList.add('on');clearTimeout(d._t);d._t=setTimeout(function(){d.classList.remove('on')},4000);}
function fb(s){var a=document.createElement('textarea');a.value=s;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(x){}a.remove();}
function cp(s){if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(s).catch(function(){fb(s)})}else fb(s)}
function go(n){var u=e(url(n));return n==='fb'?'https://www.facebook.com/sharer/sharer.php?u='+u:n==='wa'?'https://wa.me/?text='+e(txt(n)):n==='x'?'https://twitter.com/intent/tweet?url='+u+'&text='+e(t.split('\\n')[0]+sig):n==='li'?'https://www.linkedin.com/sharing/share-offsite/?url='+u:n==='tg'?'https://t.me/share/url?url='+u+'&text='+e(t+sig):n==='em'?'mailto:?subject='+e(document.title)+'&body='+e(txt(n)):''}
function msg(n){return n==='cp'?'Resumen y enlace copiados. Pégalos donde quieras.':'Resumen copiado. Pégalo en tu publicación.'}
var b=document.querySelector('.ceshare');
if(b)b.addEventListener('click',function(ev){var k=ev.target.closest('button[data-n]');if(!k)return;var n=k.getAttribute('data-n');cp(txt(n));track(n);toast(msg(n));var g=go(n);if(g){var w=window.open(g,'_blank');if(w){try{w.opener=null}catch(x){}}else location.href=g;}});
var f=document.getElementById('ce-share');
if(f)f.addEventListener('click',function(ev){var k=ev.target.closest('[data-n]');if(!k||!f.contains(k))return;var n=k.getAttribute('data-n');
 if(k.tagName==='A'){k.href=go(n)||k.href;cp(txt(n));toast(msg(n));}
 else if(n==='cp'){ev.stopImmediatePropagation();ev.preventDefault();cp(txt(n));track('cp');f.classList.remove('on');toast(msg(n));}},true);
})();</script>'''
def block(url,copy):
    btn=''.join('<button type="button" class="%s" data-n="%s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>%s</button>'%(k,k,I[k],n) for k,n in L)
    return CSS+'<section class="ceshare" data-url="%s" aria-label="Compartir esta noticia"><h2>Compartir esta noticia</h2><p>Al tocar una red se copia un resumen de la noticia con su enlace. Solo tienes que pegarlo en tu publicación.</p><div class="sb">%s</div></section><script type="text/plain" id="ce-copy">%s</script>'%(url,btn,H.escape(copy,quote=False))
if __name__=='__main__':
    f=sys.argv[1];h=open(f,encoding='utf-8').read()
    url='https://www.concursosdelestado.com/guias/noticia-dian-2676-resultados-prueba-escrita-noviembre'
    assert 'ceshare' not in h
    i=h.index('<p class="srcbox">')
    h=h[:i]+block(url,COPY_DIAN)+h[i:]
    h=h.replace('</body>',JS+'</body>',1)
    open(f,'w',encoding='utf-8').write(h);print('ok')
