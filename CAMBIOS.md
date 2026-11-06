
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

## 2026-11-05 10:49 - cartilla.enc
Procuraduria, "Mi convocatoria": las funciones de los cargos que hablan de ciudadania, canales de atencion y lenguaje claro enlazan a Atencion al usuario; conservacion y expedientes a Gestion documental; viaticos, caja menor y gasto a Presupuesto; rendicion de cuentas y audiencias publicas a Gestion publica; desaparicion forzada y violencia contra la mujer a Derechos humanos.

## 2026-11-05 10:55 - cartilla.enc
Procuraduria: dos lecciones nuevas con 13 preguntas situacionales, asignadas solo a los cargos cuyas funciones las mencionan. (1) "Metodologias de servicio a la ciudadania": caracterizacion, diagnostico de canales (ciudadano incognito, taller de desafio) y actualizacion del protocolo, para funciones sobre canales de atencion, caracterizacion, lenguaje claro y grupos de valor. (2) "Auditoria interna en la Procuraduria": informe de gestion de la Oficina de Control Interno del primer semestre de 2026 y auditoria a la Regional de Instruccion de Boyaca, para funciones de control interno, auditoria, autocontrol y planes de mejoramiento. Aparecen en "Lecciones segun las funciones de tu empleo".

## 2026-11-05 11:04 - cartilla.enc
Procuraduria: las dos lecciones nuevas (metodologias de servicio a la ciudadania y auditoria interna de la OCI) muestran una etiqueta verde "Nuevo" en la lista de lecciones del curso, en el capitulo y en el titulo de la leccion.

## 2026-11-05 11:06 - cartilla.enc
DIAN: la leccion "Rendicion de cuentas: Ley 1757 de 2015 y la estrategia 2026 de la DIAN" muestra la etiqueta verde "Nuevo" en la lista de lecciones del capitulo y en su titulo.

## 2026-11-05 11:20 - cartilla.enc
Procuraduria: revision de las citas del Decreto Ley 262 de 2000 contra el texto oficial (Funcion Publica). Se corrige el numeral del articulo 7 sobre la planta globalizada (era 32, es el 34) y la pregunta de experiencia ya no atribuye la definicion al articulo 6 del decreto (ese articulo trata la falta absoluta del Procurador): se atribuye a las preguntas frecuentes oficiales del concurso. El resto de las citas revisadas coincide con el texto.

## 2026-11-05 12:40 - cartilla.enc
Docentes: en las ~790 preguntas del banco, las cuatro opciones de respuesta ahora tienen un largo parecido (la diferencia mediana entre la mas larga y la mas corta es de ~11 %), para que no se pueda adivinar la correcta por su extension. Se reescribieron distractores y se acortaron respuestas correctas demasiado largas sin cambiar su contenido. La posicion de la respuesta correcta no cambia.

## 2026-11-05 17:05 - cartilla.enc
Docentes, cargo coordinador: nueva lección "Jornada, calendario y asignación académica" (Decreto 1850 de 2002, compilado en el Decreto 1075 de 2015: 40 semanas lectivas y 5 de desarrollo institucional, intensidad mínima semanal por nivel, jornada de docentes y directivos, 22 horas de asignación en secundaria y media) y 4 preguntas situacionales nuevas con sus explicaciones.

## 2026-11-05 19:30 - cartilla.enc
Procuraduría, capítulo Gestión documental: 18 temas nuevos basados en el Acuerdo 001 de 2024 del AGN (Acuerdo Único de la Función Archivística), con artículos citados textualmente, ejemplo de oficina, resumen "En palabras simples", caso y 3 preguntas situacionales cada uno. Base para todos los empleos con gestión documental (9 temas): mapa del Acuerdo, a quién obliga, vigilancia, comités, TRD y TVD, expediente electrónico e híbrido, transferencias y disposición final, conservación y preservación, acceso y reserva. Profundización solo para empleos cuya convocatoria menciona archivo, archivística o correspondencia (9 temas): Sistema Nacional de Archivos, RENAHC, BIC-CDA, archivos privados, fondos acumulados, derechos humanos y audiovisuales, reconstrucción de expedientes, expedientes pensionales e historias laborales, cámaras de comercio y curadores urbanos.

## 2026-11-05 20:40 - cartilla.enc
DIAN: nueva lección de repaso "Tríada misional a fondo: servicio, control y gestión de riesgos de cumplimiento" (Modelo de Gestión Institucional 2025, sec. 3.2.5, 3.3 y 3.3.1): complemento entre servicio y control, riesgo subjetivo, moral tributaria, gestión de riesgos en tiempo real con intervención preventiva, y NSGT/NSGA del CONPES 3993 de 2020. Incluye 2 casos con 6 preguntas situacionales y 2 fichas. Aparece en los mismos cargos que ya ven la lección del modelo.

## 2026-11-05 22:10 - cartilla.enc
Docentes, todos los niveles: nuevo capítulo "Estatuto docente: Decreto Ley 1278 de 2002" con 8 lecciones (quién es quién y función docente, concurso de méritos, lista de elegibles y nombramientos, período de prueba, Escalafón, los tres tipos de evaluación, deberes y prohibiciones, situaciones administrativas y retiro). Artículos citados textualmente, ejemplo de colegio, resumen "En palabras simples", lo que se pregunta en el examen y 24 preguntas situacionales con explicación.

## 2026-11-05 22:35 - cartilla.enc
Docentes, todos los niveles: nuevo capítulo "Cómo funciona el sistema escolar: Ley 715 de 2001 y Ley 115 de 1994" con 6 lecciones (competencias de la Nación, departamentos y municipios; institución educativa, centro educativo y niveles; funciones del rector; Fondo de Servicios Educativos; PEI, manual de convivencia y rol del educador; gobierno escolar con Consejo Directivo y Consejo Académico). Artículos citados textualmente, ejemplo de colegio, resumen "En palabras simples", "Para el examen" y 18 preguntas situacionales con explicación.

## 2026-11-05 23:05 - cartilla.enc
Docentes, todos los niveles: nuevo capítulo "Convivencia escolar: Ley 1620 de 2013 y Decreto 1965 de 2013" con 7 lecciones (conflicto, agresión y acoso; Comité Escolar de Convivencia; situaciones Tipo I, II y III; protocolo Tipo I; protocolo Tipo II; protocolo Tipo III; responsabilidades de docentes y rector y componentes de la Ruta de Atención Integral). Artículos citados textualmente, ejemplo de colegio, resumen "En palabras simples", "Para el examen" y 21 preguntas situacionales con explicación.

## 2026-11-05 23:40 - cartilla.enc
Docentes, todos los niveles: nuevo capítulo "Educación inclusiva: Decreto 1421 de 2017" con 5 lecciones (educación inclusiva y principios; DUA, currículo flexible y ajustes razonables; acceso, matrícula y no discriminación; PIAR y acta de acuerdo; informe anual, permanencia y corresponsabilidad de la familia). Artículos citados textualmente, ejemplo de aula, resumen "En palabras simples", "Para el examen" y 15 preguntas situacionales con explicación.

## 2026-11-05 23:58 - cartilla.enc
Docentes, directivos docentes: nuevo capítulo "Gestión directiva con la Ley 115: evaluación institucional, jornada y personero" con 3 lecciones (evaluación institucional anual y plan remedial; jornada escolar y calendario académico; personero de los estudiantes) y 8 preguntas situacionales con explicación. Solo aparece en el nivel de directivos docentes.

## 2026-11-06 00:20 - cartilla.enc
Docentes, todos los niveles: nuevo capítulo "Talleres de aula y rectoría: casos para decidir qué hacer" con 5 casos (estudiante con discapacidad que llega a mitad de año; ciberacoso en el grupo de WhatsApp; primer año como docente nombrado por concurso; rector y Fondo de Servicios Educativos; queja de una estudiante contra un docente). Cada caso trae el paso a paso, lo que no se hace y 3 preguntas para decidir (15 en total).

## 2026-11-05 23:25 - cartilla.enc
Docentes: nuevo capítulo «Práctica de aula: matemáticas con casos» (6 casos de aula con paso a paso y cita textual de los Estándares del MEN, más entrenamiento de razonamiento cuantitativo; 10 preguntas situacionales). Aparece para secundaria y media.

## 2026-11-05 23:45 - cartilla.enc
Docentes: nuevo capítulo «Práctica de aula: lengua castellana con casos» (6 casos de aula con paso a paso y cita textual de los Estándares del Lenguaje del MEN, más entrenamiento de lectura crítica con un texto analizado; 10 preguntas situacionales). Aparece para secundaria y media.

## 2026-11-06 00:05 - cartilla.enc
Docentes: nuevo capítulo «Práctica de aula: inglés con casos» (6 casos con paso a paso y cita textual de la Guía 22 del MEN, más lectura en inglés analizada; 10 preguntas situacionales). Aparece para secundaria y media.

## 2026-11-06 00:30 - cartilla.enc
Docentes: dos capítulos nuevos, «Práctica de aula: ciencias naturales con casos» y «Práctica de aula: ciencias sociales y ciudadanas con casos» (casos con paso a paso y cita textual de los Estándares del MEN, entrenamiento de razonamiento con datos y de hecho/opinión/argumento; 20 preguntas situacionales). Sociales y ciudadanas también aparece para preescolar y primaria.

## 2026-11-05 23:29 - cartilla.enc
Docentes: nuevo capítulo «Funciones del docente: lo que dice la norma, caso por caso» (áreas art. 23, PEI, plan de estudios, evaluación institucional, calendario, gobierno escolar, Ley 1098). Contenido enseñado con texto de la norma, paso a paso y preguntas.

## 2026-11-06 00:55 - cartilla.enc
Docentes: el capítulo «Tus funciones como docente de aula» se reescribió para enseñar el contenido: las 29 funciones, cada una con lo que dice la norma (cita textual de Ley 115, Ley 1620, Ley 1098 y Decreto 1421 cuando la hay), qué significa, caso, paso a paso, lo que no se hace y clave de examen; 16 preguntas situacionales.

## 2026-11-06 01:20 - cartilla.enc
Docentes: reescritos para enseñar el contenido los capítulos de funciones específicas de preescolar, primaria y docente de área (norma con cita textual cuando la hay, caso, paso a paso, lo que no se hace y clave de examen; preguntas situacionales nuevas en preescolar).

## 2026-11-06 01:50 - cartilla.enc
Docentes: reescritos para enseñar el contenido los capítulos de funciones del docente orientador, del coordinador y del rector o director rural (cada función con el texto de la norma —Ley 715, Ley 115, Ley 1620, Decreto 1965, Ley 1098, Decreto Ley 1278—, qué significa, caso, paso a paso, lo que no se hace y clave de examen; 12 preguntas situacionales nuevas). Corregida la clasificación de situaciones tipo I, II y III en el capítulo del docente de aula.

## 2026-11-06 02:15 - cartilla.enc
Docentes: nuevo capítulo «Evaluación de desempeño: cómo te evalúan cada año» (qué se evalúa y quién evalúa, los cinco principios, el proceso con carpeta de evidencias, la entrevista final, Formato A y plan de desarrollo; citas del Decreto Ley 1278, la Ley 715 y el Manual del MEN; 12 preguntas situacionales). Aparece para todos los niveles.

## 2026-11-06 03:05 - cartilla.enc
Docentes: cada aspirante ve solo lo que corresponde a su cargo según el manual de funciones. Los capítulos de práctica de aula (matemáticas, lengua, inglés, ciencias naturales, sociales) salen solo para el área que corresponde; el manual de títulos muestra solo el área del cargo; el manual de preescolar/primaria y el de rector/coordinador muestran solo el cargo; y las lecciones y preguntas de funciones del rector (Ley 715, Fondo de Servicios Educativos) ya no aparecen a docentes de aula.

## 2026-11-06 00:10 - sitio.pak
Página del concurso Docentes renovada con los datos oficiales del tablero de la CNSC: 31.163 vacantes, 90 entidades, 23 empleos con sus vacantes, las 7 etapas, cronograma preliminar, ponderación de pruebas, valoración de antecedentes, Ley 2418 y tips de inscripción. Se corrigieron cifras y preguntas frecuentes antiguas.

## 2026-11-06 00:20 - sitio.pak
Se restaura la versión anterior del sitio (del 4 de noviembre) porque la publicación de las 00:08 se armó con una copia local desactualizada y borraba cambios recientes del sitio. La página de Docentes se volverá a publicar sobre la versión correcta.

## 2026-11-06 00:30 - sitio.pak
Página del concurso Docentes: la sección «Docentes: lo que debes saber» se actualizó con los datos oficiales del tablero de la CNSC (31.163 vacantes, 90 entidades, 23 empleos, etapas, cronograma preliminar, pesos de las pruebas, valoración de antecedentes, Ley 2418 y tips de inscripción). Se retiró la información antigua (28.000 plazas, 82 entidades, nota de RTVC). El resto del sitio no cambió.

## 2026-11-06 00:45 - sitio.pak
Página del concurso Docentes: la sección informativa ahora copia la estructura del tablero oficial de la CNSC, en 10 pestañas (resumen, qué es la CNSC, vacantes con gráficas por empleo, fases y cronograma, ponderación con simulador de puntaje, Ley 2418, requisitos y funciones completas de los 23 empleos, valoración de antecedentes por grupo, entrevista y tips para participar). Solo cambia esa página.

## 2026-11-06 01:10 - cartilla.enc
Docentes: se quitaron las preguntas y los simulacros sobre las etapas del concurso, los antecedentes, el manual de funciones y títulos, y los capítulos «Tu cargo». Las preguntas de la cartilla quedan solo sobre contenido que se evalúa (normas, pedagogía, áreas, lectura crítica, razonamiento, gestión y competencias).

## 2026-11-06 01:20 - sitio.pak
Página Docentes: las pestañas del proceso pasan de barra deslizable a botones en dos filas, con efecto al pasar el mouse. Solo cambia esa página.

## 2026-11-06 01:30 - sitio.pak
Página Docentes: se quita la pestaña «Qué es la CNSC»; quedan 9 pestañas renumeradas. Solo cambia esa página.

## 2026-11-06 01:45 - sitio.pak
Página Docentes: ajuste de versión celular (tablas de ponderación y antecedentes sin desplazamiento horizontal, con el factor como encabezado de grupo). Solo cambia esa página.

## 2026-11-06 02:05 - sitio.pak
Página Docentes: el selector de empleo de la pestaña «Requisitos y funciones» pasa a ser un buscador que despliega los resultados hacia abajo mientras escribes (sin tildes ni mayúsculas, con teclado). Solo cambia esa página.
