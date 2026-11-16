# cartillas-ce

## Instrucciones para la IA que trabaje en este repositorio

Lee primero CAMBIOS.md (al final están los cambios más recientes). En cada commit agrega una entrada con: QUÉ SE HIZO, POR QUÉ, CÓMO SE HIZO y QUÉ FALTA. Así la otra IA sabe en qué vamos.

### Reglas que pidió Ariel (vigentes)
- No publicar cambios visuales sin mostrarle antes una maqueta (captura) y esperar su aprobación.
- El menú superior debe ser idéntico en todas las páginas.
- Lecciones nuevas: definición de términos, norma citada y explicación pedagógica; marcar "nuevo". Preguntas siempre de casos (situacionales), no de memoria.

### Regla de las noticias (16 nov 2026)
Toda noticia nueva en guias/noticia-*.html debe salir con estas tres cosas:
1. **Su tarjeta propia para redes** (og:image), nunca la genérica og-guias.png. Archivo en la raíz del sitio: og-<slug>.png de 1200x630. Estilo: fondo azul de la marca, logo, etiqueta del concurso con su color (DIAN #12A05A, Procuraduría #C23A4B, CAR #3E9A37, Docentes #3B82D6), la palabra NOTICIA, titular corto, dato clave en recuadro amarillo, fecha y concursosdelestado.com. Generador: herramientas/noticias/mkog.py (HTML + Playwright). Apuntar a ella og:image, og:image:alt, twitter:image, twitter:image:alt y "image" del NewsArticle en el JSON-LD.
2. **El bloque "Compartir esta noticia"** (Facebook, WhatsApp, X, LinkedIn, Telegram, Copiar resumen), antes de `<p class="srcbox">`, y el script ce-share-js antes de `</body>`. Generador: herramientas/noticias/share.py (funciones block(url, resumen) y JS).
3. **Su resumen para copiar**, en `<script type="text/plain" id="ce-copy">`: emojis 📢 📌 ✅ ⚠️, tuteo, sin prometer resultados. Al compartir se copia: resumen + "🔗 enlace?f=red" + "✍️ concursosdelestado.com" al final. El botón flotante "Compartir" también copia ese resumen en las noticias.

Además: agregarla en guias/noticias-concursos.html (principal o "Últimas noticias", y "Para no perderte"), actualizar la fecha "Actualizado el", y añadirla a sitemap.xml. Después de publicar, Ariel debe pedir la indexación en Search Console y pasar el enlace por el depurador de Facebook ("Volver a extraer").
