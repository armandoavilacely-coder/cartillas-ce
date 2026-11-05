
## 2026-11-03 06:47 - cartilla.enc
Corrige las explicaciones de 6 preguntas de ofimática (Excel, Word y Outlook) en las cartillas DIAN y Procuraduría: #¡DIV/0!, CONTARA, Ctrl+N, F7, Ctrl+1 y confirmación de lectura. Las respuestas correctas no cambian; ahora cada explicación habla de la respuesta correcta.

## 2026-11-03 06:48 - cartilla.enc
Corrige la publicacion anterior: la reconstruccion habia dejado fuera la funcion de indicadores de la cartilla (REF_API). Se restaura la version completa (control: 309 cargos con listado y temas enlazados) y se aplican solo las correcciones de 6 explicaciones de ofimatica (#¡DIV/0!, CONTARA, Ctrl+N, F7, Ctrl+1 y confirmacion de lectura en Outlook) en DIAN y Procuraduria.

## 2026-11-03 07:35 - cartilla.enc
Se retrocede la cartilla a la version del 31 de octubre (commit a408e22), por solicitud de Claudia, mientras se revisan los reportes de ingreso de esta manana. Se deshacen las dos publicaciones de hoy (ef0ac33 y 32d7386): correcciones de explicaciones de ofimatica (DIAN y Procuraduria). El historial no se reescribe: es un commit nuevo que restaura el archivo.

## 2026-11-03 08:02 - cartilla.enc
Parche sobre la version publicada del 31 de octubre (con panel admin y los 4 concursos): el error de BUSCARV pasa de #N/A a #N/D en 13 sitios de DIAN y Procuraduria (el nombre en Excel en español); tabla de atajos aclara que Ctrl+E es Seleccionar todo solo en Word y en Excel es Relleno rapido; explicaciones corregidas del riesgo de deteccion, la carrera especifica de la DIAN (Decreto Ley 927 de 2023) y el FURAG; la regla de formato condicional ya no pinta filas vencidas. Freno de seguridad verificado: no pierde contenido.

## 2026-11-03 21:50 - cartilla.enc
Cuadernillos de DIAN y Procuraduria: al terminar, ademas de "Para repasar" (solo las falladas), ahora hay un desplegable "Revisar todo el cuadernillo (N preguntas, con tu respuesta y la correcta)". Muestra todas las preguntas: en las de conocimientos, las opciones con la correcta en verde (check) y tu respuesta errada en rojo, mas la explicacion; en las comportamentales e integridad (DIAN), tu respuesta y la alineada con el perfil. Marca cada una como acertaste, por repasar o sin responder. Pedido por una clienta que no podia repasar el cuadernillo completo. Solo se agrega codigo en endExam (DIAN) y endQ (Procuraduria): el resto de la cartilla queda identico a la version del 3 de noviembre 08:02 (control: mismas 4.150 preguntas, ida y vuelta de cifrado verificada).


## 3 nov 2026, 23:05 — Simulacro gratis DIAN 2676: de 30 a 50 preguntas
- El simulacro gratis de la DIAN (cuenta gratuita) pasa de 30 a 50 preguntas, cada una con su razón. Se añaden 20 nuevas: Aduanero 3, Analítica 4, Fiscalización 4, Comunicaciones/gestión 4, La DIAN e integridad 3, Cartera 2. Quedan 50 repartidas en las 6 áreas y el resultado por área suma sobre 50.
- Se actualizan los textos de esa página (título, descripción, "Unos 45 minutos") y el catálogo gratis del panel (lib.php) a "50 preguntas".
- Los demás concursos y los mensajes de ventas (que dicen 30) no cambian.
- Para volver atrás: revertir este commit (restaura cartilla.enc y php.pak anteriores).

## 3 nov 2026, 23:50 — SEO: títulos de cargos más cortos y sitemap
- 405 páginas de cargos (DIAN y Procuraduría) tenían títulos de 64 a 136 caracteres que Google corta. Ahora llevan "Cargo · Dependencia · Concurso" en unos 60 a 66 caracteres, sin la palabra "Cartilla" al inicio y sin puntos suspensivos. Los títulos siguen siendo únicos (se mantiene el sufijo (2), (3) donde dos empleos coinciden). El H1 y el contenido no cambian.
- Se agrega al sitemap la página concursos/examen-estado-abogados, que estaba fuera.
- Para volver atrás: revertir este commit.

## 4 nov 2026, 07:40 — SEO: corrección de títulos de cargos
- El cambio de ayer (79ca5e1) recortaba tanto algunos títulos que varios cargos 3PU-17 quedaban casi iguales ("Preventivo · Procuraduría (2)…(6)"). Ahora los cargos que chocaban al acortarse usan una versión un poco más larga que conserva lo que los distingue (hasta 97 caracteres solo en esos casos); los demás siguen en unos 60.
- Resultado: 410 títulos de cargos revisados, ninguno repetido en todo el sitio, solo 16 con sufijo (n). Solo cambia la etiqueta <title>; el contenido de las páginas no cambia.
- Sitemap: se mantiene examen-estado-abogados.

## 4 nov 2026, 10:15 — Celular: menú y búsqueda por concurso en todo el sitio
- Antes, en pantallas de celular se ocultaban todos los enlaces de navegación y el encabezado ocupaba dos filas. Ahora es una sola fila: logo, "Cuenta gratis", "Mi cartilla" y un botón de menú (☰).
- El menú abre un panel con: búsqueda de cargo con selector de concurso (DIAN, Procuraduría, CAR, Docentes), enlaces a cada concurso, Inicio, Cómo funciona, Precio, Guías, Preguntas, Suscríbete, WhatsApp y modo claro/oscuro.
- En las páginas de cargos, guías y concursos aparece una barra "Buscar mi cargo por concurso" bajo el encabezado, que abre el menú con la búsqueda. La búsqueda lleva a la portada con el cargo y el concurso ya cargados (/?q=...&c=...).
- El botón flotante de WhatsApp pasa a ser un círculo para no tapar el texto, y se oculta cuando ya está la barra "Pedir mi cartilla por WhatsApp". El botón de compartir sube para no pisarla.
- Escritorio sin cambios. Se aplica a las 749 páginas con encabezado. Para volver atrás: revertir este commit.

## 4 nov 2026, 10:55 — Celular: ajuste para pantallas de 320 px
- En celulares muy angostos (320 px) el encabezado nuevo se salía 10 px a la derecha y aparecía desplazamiento horizontal. Se reducen relleno, tamaño de letra y logo en pantallas de hasta 360 px. Sin cambios en pantallas mayores ni en escritorio.

## 2026-11-04 11:50 — Simulacros gratis: pregunta final en 61 enunciados
- Procuraduría (10–30), CAR (11–30) y Docentes (11–30): los casos terminaban sin la pregunta (reporte de un cliente, p. ej. Procuraduría 28). Se agregó la pregunta "¿…?" a cada uno; opciones, respuestas y explicaciones no cambian.
- Solo cartilla.enc (los simulacros gratis viajan dentro de la cartilla).

## 2026-11-04 14:05 — Revisión de preguntas: explicaciones y enunciados
- Auditadas 4.978 preguntas (cartillas DIAN, Procuraduría, CAR, Docentes y simulacros gratis).
- 1.061 explicaciones que eran solo una cita ("Art. 67 CPACA.") o una palabra ahora dicen cuál es la respuesta correcta y por qué, conservando la cita como "Fundamento".
- 5 preguntas de Procuraduría tenían invertidos el caso y la pregunta ("Según el art. 41" / "¿Cuándo se perfecciona...?"): corregidas, con la norma completa.
- 1 pregunta DIAN sin pregunta final: corregida.
- Las copias comprimidas (br-dian, br-pgn) que recibe casi todo navegador estaban desactualizadas frente al texto fuente: regeneradas, así que también llegan las correcciones anteriores.
- Pendiente: ~1.470 preguntas donde la opción correcta es bastante más larga que las otras (se adivina por longitud).

## 2026-11-04 16:55 — Cartilla más rápida
- Los datos de CAR y Docentes (6,2 MB) salieron del bloque principal a `<script id="d-car">` y `<script id="d-doc">` (+ copias br-dcar, br-ddoc).
- acceso/index.php (php.pak): a quien no tiene CAR/Docentes ya no se le envían; a quien sí, van como archivo aparte cacheado (`/acceso/?js=dcar|ddoc`).
- Marcador CE-PUB corregido (estaba desfasado desde el cambio del simulacro de 50): el servidor vuelve a leer solo la parte necesaria del archivo en vez de los 40 MB completos.
- Página de un alumno DIAN/Procuraduría: de ~1,6 MB comprimidos a ~0,2 MB.

## 2026-11-04 18:10 — Cuadernillo: revisión pregunta por pregunta
- Resultado del cuadernillo (DIAN y Procuraduría): nuevo recuadro "Revisa pregunta por pregunta" con Anterior/Siguiente y filtro (todas, falladas y sin responder, acertadas). Muestra el caso, el enunciado, las opciones con ✓ correcta y ✗ tu respuesta, y la explicación.
- Antes la revisión completa estaba escondida al final en un desplegable; la lista "Para repasar" quedó como resumen plegable debajo.

## 2026-11-04 19:20 — Revisión completa en todos los resultados
- Nuevo revisor común (window.__ceRVH / __ceRI / __ceRV): cada pregunta muestra caso, enunciado, todas las opciones con ✓ correcta y ✗ tu respuesta, "Sin responder" si aplica y "Por qué" con la explicación; navegación una por una y filtro Todas / Falladas y sin responder / Acertadas.
- Aplicado en: práctica y examen de DIAN, Procuraduría, CAR y Docentes; cuadernillos DIAN y Procuraduría (se quitó la lista resumida); cuestionarios de capítulos y lecciones (motor QUIZ); simulacros gratis DIAN 50, Procuraduría, CAR y Docentes; cuestionario del capítulo gratis de derecho de petición; curso de abogados.

## 2026-11-04 20:30 — Verificación de respuestas DIAN con cifras y plazos
- Revisadas 794 preguntas DIAN (cartilla + simulacro gratis de 50) con plazos, cifras, porcentajes, UVT y sanciones; las dudosas se verificaron en fuente (art. 260-11, art. 640, art. 804 ET; Ley 2586 de 2026).
- Corregidas 2 claves equivocadas sobre imputación del pago (art. 804 ET, imputación proporcional desde la Ley 1819 de 2016): pregunta del banco DIAN (clave pasa a "en proporción") y pregunta 1 del simulacro gratis de 50 (reescrita con cifras limpias).
- Nota agregada a la pregunta de interés moratorio "según la Ley 1066": hoy es usura de consumo menos dos puntos.
- 7 explicaciones con comas sobrantes ("25 %,.").

## 2026-11-04 21:40 — Verificación DIAN contra los 11 documentos oficiales
- Se cotejaron 308 preguntas DIAN con los documentos fuente: Ley 2586 de 2026, Acuerdo 21 de 2025 (DIAN 2676), Resolución 0065 de 2024 (diccionario de competencias), PGD v3, cartilla CT-CAC-0054, Código de Integridad CG-TAH-0002, PTEP 2025-2026 v3, PR-CAC-0494, Resolución 000017 de 2018, Manual de Contratación MN-FI-0013 y PEI 2024-2026. Ninguna clave errada.
- Ley 2586, caso del serial mal digitado: la explicación ahora cita la corrección sin sanción en 30 días hábiles (art. 15, num. 15.2.2.4), la multa del 15 % / 30 % FOB (art. 17, num. 4) y que la aprehensión solo procede si no se paga (art. 26, num. 2).
- PGD, metadatos del firmante: se cambia un distractor que mencionaba "el tamaño del archivo", que sí es metadato mínimo y podía confundir.

## 2026-11-04 20:30 (Bogotá) — DIAN: revisión de las 1.237 preguntas restantes (sin cifras)
- Se revisaron una por una las preguntas DIAN que no tenían cifras ni citaban los 11 documentos (procedimiento tributario, CPACA, archivo, control interno, contratación, cambiario, aduanero, LA/FT, analítica, ofimática, razonamiento). Ninguna otra clave errada.
- Imputación del pago (caso del contribuyente que paga 10 millones): decía "sanciones, intereses e impuesto" (regla anterior a 2016). Ahora la clave es la imputación proporcional del art. 804 E.T. (Ley 1819 de 2016) y el caso se ajusta. En otra pregunta, "reimputa en el orden legal" pasa a "en la proporción legal".
- Plan Anticorrupción: 3 preguntas (DIAN, Procuraduría y la versión de práctica) daban como respuesta el Plan Anticorrupción y de Atención al Ciudadano. Desde la Ley 2195 de 2022 y el Decreto 1122 de 2024 es el Programa de Transparencia y Ética Pública con su plan anual; se actualizan clave y explicación. También se actualizan la lección de la Ley 1474 (art. 73) y la entrada del glosario.
- Estructura DIAN: la explicación de las siete subdirecciones de la Dirección de Gestión de Impuestos ahora las nombra completas (Decreto 1742 de 2020, art. 5).

## 4 nov 2026 — Procuraduría: revisión de las 1.038 preguntas
- Se revisaron las 1.038 preguntas de Procuraduría contra el Código General Disciplinario (Ley 1952 de 2019 con la Ley 2094 de 2021), el CPACA, la Ley 2220, las leyes 80/1150, 594, 1448, 1581 y 1010 y la Constitución. Todas se ven con pregunta, opciones, respuesta correcta y explicación en cuadernillos, simulacros y quices.
- Corregida una clave errónea (cooptación de la política: la respuesta correcta era la primera opción).
- Prescripción y caducidad: la explicación de la prescripción ahora cita el art. 33 (cinco años desde la consumación, se interrumpe con la notificación del fallo de primera instancia) y aclara que la caducidad figura en el art. 32 pero la ley no le fija término. La pregunta que confundía caducidad con "no iniciar a tiempo" pasa a preguntar qué interrumpe la prescripción.
- Falta grave culposa: sanción corregida a suspensión de uno a doce meses (art. 48, num. 4).
- Gobierno Digital: se reemplazan los "dos componentes" (TIC para el Estado y para la Sociedad) por los cinco elementos del Decreto 767 de 2022.
- Se retira el número de artículo no verificado del Decreto Ley 263 de 2000 y se aclara la atribución del rango de humedad del papel (no es el del Acuerdo 049 de 2000 del AGN, derogado).

## 4 nov 2026 (noche) — Procuraduría: cotejo con el Plan de Conservación, PINAR y políticas
- Se cotejaron las preguntas de gestión documental con el Plan de Conservación Documental (DO-PL-02) y el PINAR (DO-PL-01): ocho programas (el de saneamiento ambiental es el tercero), SIC = Plan de Conservación + Plan de Preservación Digital, proyectos 4 (SIC), 6 (SGDEA) y 12 (Biblioteca) y el objetivo de ponderar aspectos críticos, todos coinciden.
- La explicación de la humedad del papel se ajusta al plan: 40 % a 50 % de humedad relativa, entre 15 y 20 °C y 100 lux o menos, rangos que el plan atribuye al Archivo General de la Nación.

## 4 nov 2026 (noche) — Procuraduría: cotejo con las Resoluciones 130 de 2024 y 435 de 2022
- Resolución 130 de 2024 (instrumentos archivísticos): coinciden las preguntas sobre qué adopta el art. 1 (política, PINAR, PGD y SIC), que la Tabla de Control de Acceso sigue vigente por el art. 2, y las definiciones de PGD, PINAR y SIC.
- Resolución 435 de 2022 (acoso laboral y Comités de Convivencia): coinciden las preguntas de integración (dos y dos con suplentes), sesiones trimestrales con cinco días de antelación, desistimiento tácito al mes, inasistencia del denunciado y buzón violeta.
- Una pregunta cambia: el acoso sexual no va "a la Procuraduría" sino al buzón violeta para activar el protocolo, con cita de los arts. 22 y siguientes.

## 5 nov 2026 — DIAN: OPEC 236911 (Inspector II, ficha TP-DE-3003)
- Se carga el listado oficial de indicadores del empleo 236911 (Inspector II, nivel Profesional, todos los procesos, ficha transversal TP-DE-3003): 11 funcionales y 15 comportamentales y de valores, tomados de la consulta de indicadores del proceso DIAN 2676. Ahora la OPEC aparece en el mapa del cargo y en el listado oficial, y cada indicador lleva a la lección donde se estudia.
- Cobertura: los 26 indicadores quedan enlazados a una lección existente (MIPG, control interno y auditoría, estructura y misionalidad, razonamiento analítico, competencias y valores). Se agrega al capítulo del cargo la lección "Gestión del riesgo e indicadores" (del proceso de planeación) para el indicador de gestión.
- Pendiente: la estrategia de rendición de cuentas se estudia hoy en la lección de PQRSF (Ley 1757 de 2015); falta una lección propia con el texto de la norma.

## 2026-11-05 10:32 - cartilla.enc
Nueva leccion "Rendicion de cuentas: Ley 1757 de 2015 y la estrategia 2026 de la DIAN" en Gestion publica y en el capitulo transversal del Inspector II (OPEC 236911), con la Ley 1757 arts. 48 a 56, los elementos y etapas del Manual Unico y el caso DIAN (autodiagnostico 2025, Comites TAC). Incluye 10 preguntas con explicacion y 3 fichas; el indicador "Estrategia de rendicion de cuentas" ahora enlaza a esa leccion.
