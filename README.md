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

### Cómo se publica un ebook gratis (16 nov 2026)
1. El PDF se guarda en el Drive de Ariel, carpeta EBOOKS CONCURSOS DEL ESTADO, compartido como "cualquier persona con el enlace" (lector). No se sube a cPanel ni al repositorio.
2. php.pak: se agrega el id del ebook en ce_ebooks() de _suscripcion.php (archivo, título, página) y en $EB de descargar.php con el enlace de Drive (uc?export=download&id=...). La primera descarga trae el PDF de Drive y lo guarda en ce_data/ebook.
3. Los ebooks de Docentes ('doc' y 'gdoc') se entregan solo por correo: revisar ce_respuesta_confirmado (_suscripcion.php) y confirmar.php. Marcador del correo masivo en acceso/lib.php: {enlace_ebook_<id>}. El bot (acceso/chat_core.php) debe nombrar todos los ebooks.
4. sitio.pak: página de captación copiada de guias/ebook-concurso-docente.html (mismo formulario y JS, cambiando ebook:"<id>"), tarjeta en guias/index.html, sitemap, portada og-ebook-<id>-portada.png, vistas previas og-ebook-<id>-p1..p3.png y tarjeta para redes og-ebook-<id>.png (1200x630).
5. Imagen para Facebook 1080x1350 con "EBOOK GRATIS" grande; se guarda en el mismo Drive. El copy de Facebook no lleva enlaces (la dirección va en la imagen); sí puede llevar el WhatsApp.


## Guía 34 (directivos): usar SIEMPRE la versión 2026
Desde el 16-nov-2026 las lecciones de directivos usan la Guía 34 actualizada por el MEN en 2026 ("Ruta de Mejoramiento Institucional"): plan de mejoramiento ANUAL, 4 áreas, 15 procesos, 45 componentes. No volver a escribir "horizonte de tres años" ni los procesos de 2008 (seguimiento académico como proceso aparte, relaciones con el entorno, apoyo a la gestión académica). Los scripts con el texto de las lecciones NO van en este repo (es público y las lecciones son de pago); viven en el espacio de trabajo de la IA y se describen en CAMBIOS.md.
