
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

## 2026-11-06 12:00 - sitio.pak
Concurso docente: la evaluación de muestra de la página ahora tiene 10 preguntas situacionales de contenido profundo (convivencia, inclusión, matemáticas, lenguaje, lectura, cuantitativo, naturales); se quitaron las de etapas e inscripción.

## 2026-11-06 01:10 - sitio.pak
Concurso docente: la sección "Evaluación de muestra" se reemplaza por información del simulacro gratis (30 preguntas con respuesta razonada) y botones para crear cuenta gratis o entrar al panel. Solo cambia concursos/docentes.html.

## 2026-11-06 01:35 - sitio.pak
Concurso docente, simulador del puntaje final: ahora es evidente que el usuario escribe sus datos (pasos 1 y 2, casillas grandes con borde y "/ 100", barra deslizable, aporte en puntos por prueba, aviso del mínimo aprobatorio en aptitudes). Solo cambia concursos/docentes.html.

## 2026-11-06 02:05 - sitio.pak
Concurso docente, facilidad de uso para personas mayores: recuadro "Cómo usar esta página" con 4 pasos, botones A- / A / A+ para el tamaño de letra (se recuerda), pestañas más grandes con subtítulo y marca "Estás aquí", botones "Anterior / Siguiente" al final de cada tema, letra y contraste mayores y foco visible. Solo cambia concursos/docentes.html.

## 2026-11-06 02:30 - sitio.pak
SEO del concurso docente: título y descripción con 2026, CNSC, vacantes y requisitos; imagen propia para compartir (og-docentes.png) con texto alternativo; tres preguntas frecuentes nuevas (vacantes, peso de las pruebas, requisitos) en la página y en los datos estructurados; fecha de modificación y sitemap actualizados.

## 2026-11-06 02:50 - sitio.pak
SEO de CAR: título con 2026, descripción con "simulacro gratis" (antes decía evaluación de muestra), imagen propia para compartir (og-car.png) con texto alternativo y fecha del sitemap actualizada. Solo cambian concursos/corporaciones-autonomas-regionales.html, sitemap.xml y la imagen nueva.

## 2026-11-06 03:30 - sitio.pak
SEO del concurso docente: 23 páginas nuevas, una por empleo (/cargos/docentes/...), más un listado (/cargos/docentes/). Cada una trae vacantes, título requerido y alternativa, experiencia, funciones, peso de las pruebas, tabla de valoración de antecedentes, enlaces a los temarios gratis, preguntas frecuentes con datos estructurados y botones de pago/WhatsApp. Se agregan al sitemap (748 a 772 URLs) y se enlazan desde la pestaña "Requisitos y funciones" de la página de Docentes. Además, textos de precio de Docentes pasan a tuteo.

## 2026-11-06 04:00 - sitio.pak
Páginas por empleo docente en celular: las funciones generales quedan plegadas ("toca para verlas") y las específicas abiertas, y la tabla de antecedentes se ajusta mejor (la página pasa de unos 12.300 a unos 8.300 píxeles de alto). Solo cambian las 24 páginas de cargos/docentes.

## 2026-11-06 05:00 - sitio.pak
SEO del concurso docente: 121 páginas nuevas de vacantes en /vacantes-docentes/ (listado, 30 departamentos y 90 entidades territoriales). Cada página muestra las vacantes por entidad y por empleo, las reservadas para personas con discapacidad, enlaces a los requisitos de cada empleo, preguntas frecuentes con datos estructurados y botones de pago/WhatsApp. Datos del tablero de la CNSC (corte 14 de octubre de 2026), con las sumas verificadas contra los 31.163 totales y contra cada empleo. Se agregan al sitemap (772 a 893 URLs) y se enlazan desde la pestaña "Vacantes" de la página de Docentes. Solo cambian concursos/docentes.html, el sitemap y las páginas nuevas.

## 2026-11-06 05:30 - sitio.pak
SEO del concurso docente: página nueva "Concurso docente 2026: fechas, cronograma e inscripciones" (/concursos/docentes-fechas) con el cronograma preliminar del tablero de la CNSC, inscripciones, costo, pruebas, vigencia de las listas y preguntas frecuentes con datos estructurados. Se enlaza desde la pestaña Fases de Docentes y desde el listado de vacantes, y se agrega al sitemap (893 a 894 URLs).

## 2026-11-06 01:36 - sitio.pak
Las paginas de empleos docentes y vacantes por departamento se movieron a rutas planas dentro de concursos/ (concursos/docentes-empleos, docentes-empleo-*, docentes-vacantes, docentes-vacantes-*) porque el actualizador del servidor solo publica concursos/*.html planos y las carpetas cargos/docentes/ y vacantes-docentes/ daban 404. Enlaces, canonicals, JSON-LD y sitemap reescritos.

## 6 nov 2026, 11:40 — Tercer ebook gratis: Concurso docente 2026 (embudo completo)
- Nueva guía en PDF de 16 páginas "Concurso docente 2026: tu ruta, paso a paso" (cifras CNSC del 6-nov, cronograma, pruebas y pesos, cálculo de puntaje, 23 empleos, antecedentes, inscripción, documentos, plan de 4 semanas, enlaces para registrarse/pagar/ver el concurso y "Quiénes somos").
- Página de captación /guias/ebook-concurso-docente (mismo formulario y proceso que los otros ebooks: nombre, correo y WhatsApp, política de datos y términos obligatorios, mercadeo opcional), con tarjeta en /guias y entrada en el sitemap.
- Servidor (php.pak): ebook id "doc" en _suscripcion.php y descargar.php (enlace firmado de 30 días; si el PDF no está en el servidor, redirige al PDF del repositorio), marcador {enlace_ebook_doc} en el correo masivo y el bot ahora dice que hay tres ebooks gratis.
- PDF agregado al repositorio en ebook/guia-concurso-docente-2026.pdf.

## 6 nov 2026, 13:40 — Docentes: 30 lecciones con contenido real y normas textuales
- Se reescriben 30 lecciones de la cartilla Docentes que solo traían el esquema (Qué evalúa / Qué debes estudiar / Cómo te lo preguntan). Ahora explican, dan el procedimiento paso a paso y citan la norma literal, para que nadie tenga que buscar la ley aparte.
- Docente, gestión: planeación y organización; competencias pedagógicas y didácticas (DUA, Decreto 1421); evaluación del aprendizaje (SIEE, Decreto 1075); participación y seguimiento; recursos pedagógicos; comunicación institucional (CPACA art. 14, Ley 1581 art. 7); comunidad y entorno (consejo de padres, Ley 1620, Ley 1098).
- Orientador: 8 lecciones (Ley 1620 arts. 13, 19, 29 a 33; Decreto 1965 arts. 39 a 45, protocolos Tipo I, II y III).
- Directivos: 8 lecciones (Ley 115 arts. 73 y 142 a 145; Ley 715 art. 10; Decreto 1075 fondo de servicios educativos y consejo de padres; Decreto Ley 1278 art. 6).
- Competencias comportamentales: 7 lecciones (liderazgo, comunicación, trabajo en equipo, negociación y mediación, compromiso, iniciativa, orientación al logro) con lo que dice el Anexo técnico 2026 sobre la entrevista (10 %, clasificatoria, rúbrica con conductas observables) y el método STAR.
- Control: cada fragmento citado se verifica por programa contra el texto del artículo (falla si no aparece literal). Se cargó la cartilla en navegador sin errores, ida y vuelta de cifrado verificada.
- Cambio en 2 lecciones de Directivos (Ejecución y Comunidad): se condensó el texto largo previo; se perdieron los apartados sobre Decreto 915 de 2016 y el concurso.
- Solo cambia cartilla.enc (bloque DOCDATA y su copia comprimida). Para volver atrás: revertir este commit.

## 6 nov 2026, 14:05 — Docentes: se restaura texto previo en 8 lecciones
- La publicación de las 13:40 reemplazó por completo 30 lecciones; en 8 de ellas la versión nueva quedó más corta que la anterior (Orientador: protocolos y participación; Directivos: planeación, ejecución, talento humano, comunicación y comunidad; Competencias: trabajo en equipo) y se había perdido material (p. ej. Decreto 915 y el concurso, Mérito y Constitución art. 125, ley y manual de convivencia).
- Se agrega al final de esas 8 lecciones el bloque "Para profundizar" con los apartados anteriores, sin los párrafos de esquema repetidos ni el resumen de tipos de situaciones "(verifica)", que ahora está citado textual del Decreto 1965.
- Solo cambia cartilla.enc. Para volver atrás: revertir este commit.

## 6 nov 2026, 14:20 — Ebook concurso docente: se entrega solo por correo
- Al registrarse en /guias/ebook-concurso-docente ya no empieza ninguna descarga directa ni aparece botón de descarga. El mensaje de confirmación dice: "¡Listo! El ebook fue enviado a tu correo electrónico (correo)". El PDF se baja únicamente desde el botón del correo (enlace firmado de 30 días).
- Si el correo no se pudo enviar, se muestra que el registro quedó listo y se pide escribir por WhatsApp (no se ofrece descarga).
- La página cambia el botón a "Recibir el ebook gratis en mi correo" y el texto "la descarga empieza al instante" a "te enviamos el ebook al instante a tu correo".
- Confirmación por enlace (confirmar.php) y respuesta de la API (_suscripcion.php): solo para el ebook "doc"; los ebooks de Procuraduría y comportamentales no cambian.
- Nota: el PDF sigue en el repositorio público (ebook/guia-concurso-docente-2026.pdf) porque el enlace del correo lo sirve desde ahí. Quien conozca esa dirección puede bajarlo sin el correo.
- Archivos: php.pak (_suscripcion.php, confirmar.php) y sitio.pak (guias/ebook-concurso-docente.html). Para volver atrás: revertir este commit.

## 6 nov 2026, 14:40 — Ebook docente: el PDF se sirve desde Google Drive y sale del repositorio
- El enlace firmado del correo (descargar.php) ahora lleva al PDF en Google Drive (carpeta EBOOKS CONCURSOS DEL ESTADO, compartido solo con quien tenga el enlace). Ya no apunta a GitHub.
- Se elimina ebook/guia-concurso-docente-2026.pdf del repositorio público, así que ya no hay una copia descargable ahí (queda en el historial de commits anteriores).
- Solo cambia php.pak (descargar.php). Para volver atrás: revertir este commit.

## 6 nov 2026, 14:50 — Ebook docente: el botón del correo descarga de inmediato desde nuestro dominio
- descargar.php: si el PDF aún no está en el servidor, lo trae una sola vez del respaldo en Google Drive, lo guarda en ce_data/ebook y lo entrega directo (Content-Disposition: attachment). La persona toca el botón del correo y el PDF empieza a bajar al instante, sin pasar por la pantalla de Drive. Si el servidor no puede traerlo, mantiene la redirección a Drive como respaldo.
- Solo cambia php.pak (descargar.php). Para volver atrás: revertir este commit.

## 6 nov 2026, 15:30 — Docentes: lectura crítica y razonamiento cuantitativo con contenido completo (y ahora visibles)
- Hallazgo: los capítulos "Lectura crítica en el contexto escolar" y "Razonamiento cuantitativo en el aula" existían en la cartilla pero no estaban asignados a ningún nivel (doc-pri, doc-sec, doc-ori, doc-dir, doc-todos), así que nadie los veía. Se agregan a CORE de DOCAPP: ahora aparecen en los cinco niveles, con sus 18 y 19 preguntas.
- Lectura crítica: de 3 lecciones de unos 300 caracteres a 6 de 1.600 a 3.000: tres niveles de lectura (con ejemplo resuelto), tesis, argumentos y errores de razonamiento, lectura de tablas y gráficos (tabla de matrícula con cuentas), tipos de texto escolar (circular, acta, informe, norma, noticia), estrategia en la prueba (tiempo, descarte, distractores) y práctica guiada con tres casos.
- Razonamiento cuantitativo: de 3 lecciones a 6: promedio ponderado y nota mínima, porcentajes y variaciones (puntos porcentuales), proporciones y regla de tres, cálculo a mano sin calculadora (el Anexo técnico prohíbe calculadoras), media, mediana, moda y probabilidad simple, y cinco problemas típicos de colegio resueltos paso a paso.
- Ancla: Anexo técnico 2026, num. 2 (la prueba de aptitudes y competencias básicas incluye lectura crítica y razonamiento cuantitativo; eliminatoria con mínimo 60 docentes y 70 directivos).
- Control: cada cuenta de los ejemplos y de las prácticas se verificó por programa; la cartilla carga sin errores y los dos capítulos aparecen en los cinco niveles; ida y vuelta de cifrado verificada.
- Solo cambia cartilla.enc. Para volver atrás: revertir este commit.

## 6 nov 2026, 16:05 — Docentes: matemáticas y lengua castellana, 6 lecciones nuevas en cada una
- Matemáticas (esp-mat, de 8 a 14 lecciones): estándares textuales de básica secundaria por pensamiento (numérico, variacional, espacial, métrico y aleatorio); pensamiento numérico con ejemplos y errores típicos (fracciones, potencias, signos); pensamiento variacional (proporcionalidad, función lineal, ecuaciones, patrones); espacial y métrico (áreas, volúmenes, Pitágoras, Tales); datos, gráficos y probabilidad; y resolución de problemas y planeación de la clase (fases de Pólya, ejemplo de planeación, evaluación formativa).
- Lengua castellana (esp-len, de 8 a 14): producción textual como proceso (con estándares textuales y rúbrica), comprensión e interpretación (estrategias antes, durante y después, preguntas de tres niveles), literatura y plan lector, medios y ética de la comunicación, gramática y ortografía en el enfoque comunicativo (por qué/porque, sino/si no, tildes, puntuación) y planeación y evaluación de la clase.
- Las lecciones anteriores se conservan; las nuevas se agregan al final. Cada estándar citado se verificó literal contra el documento del Ministerio (Estándares 2006). Las cuentas de los ejemplos se verificaron por programa. Los estándares de matemáticas se agrupan por pensamiento y por la básica secundaria (6.º a 9.º) y no por pares de grados, porque el texto fuente del PDF mezcla las columnas.
- Solo cambia cartilla.enc. Para volver atrás: revertir este commit.

## Docentes: ingles, sociales y ciencias naturales con 14 lecciones nuevas
- esp-ing +5 (meta B1 y escala MCE, estandares por habilidad con citas literales, enfoque comunicativo, correccion y evaluacion de las cuatro habilidades, lectura y escritura con estrategias).
- esp-soc +4 (estandares de ciencias sociales, competencias ciudadanas, fuentes historicas y causalidad, geografia y mapas).
- esp-nat +5 (estandares de ciencias naturales, indagacion con ejemplo, seguridad y residuos, modelos y problemas, educacion ambiental y PRAE). Visible tambien en fisica, quimica y biologia (comparten el bloque base).
- Todas las citas de estandares se verificaron contra el texto oficial (assert). Ninguna leccion existente se modifico. Solo cambia cartilla.enc.

## Docentes: religion, etica, educacion fisica, filosofia, economia, tecnologia y artes (+15 lecciones)
- esp-rel +2, esp-eti +3, esp-efi +2, esp-fil +2, esp-eco +2, esp-tec +1, esp-art +1 (artes comparte base con musica, danza, escenicas y plasticas).
- Citas literales solo de Ley 115 de 1994 (arts. 14, 23, 24, 25, 31, 32), verificadas por assert. No hay texto oficial de estandares de artes/EF/religion/filosofia/tecnologia en el Drive; cuando el usuario los suba se amplian con citas.
- Solo cambia cartilla.enc; ninguna leccion previa se toco.

## Docentes: preescolar y primaria (+7 lecciones)
- esp-pre +4 (definicion y fines, objetivos del art. 16, ingreso sin pruebas y edad de transicion, valoracion cualitativa) y esp-prim +3 (objetivos del ciclo, planeacion con proyectos y multigrado, evaluacion y retroalimentacion).
- Citas literales de Ley 115 (arts. 15, 16, 17, 21) y Decreto 1075 de 2015 (arts. 2.3.3.2.2.1.4, 2.3.3.2.2.2.1, 2.3.3.2.2.3.4, 2.3.3.2.2.3.5), verificadas por assert. Solo cambia cartilla.enc.

## Aviso para cualquier Claude que edite la cartilla
- cartilla.enc es un solo archivo cifrado: cada commit lo reemplaza completo. Antes de editar: `git pull`, descifrar el cartilla.enc ACTUAL del repo (inverso de /tmp/qa/enc2.py) y trabajar sobre ese HTML; nunca sobre un HTML de trabajo anterior, porque se perderian las lecciones agregadas despues.
- Antes de cada push: `git fetch` y confirmar que no hay commits nuevos; si los hay, volver a aplicar los cambios sobre la version nueva.
- Despues de publicar: verificar que cada bloque tenga >= lecciones y >= caracteres que antes.

## Docentes: rector, coordinador y director rural (+9 lecciones)
- esp-rec +4 (funciones Ley 715 art. 10 con casos, Fondo de Servicios Educativos, Consejo Directivo vs Consejo Academico, evaluacion y permanencia), esp-coo +3 (alcance del cargo, ruta de convivencia, apoyo academico), esp-dru +2 (responsabilidad y diferencia con rector, escuela rural y comunidad).
- Citas literales de Ley 715 (arts. 10, 11), Decreto Ley 1278 (art. 6) y Decreto 1075 (arts. 2.3.3.1.5.6, .5.7, .5.8, 2.3.3.2.2.3.5), verificadas por assert. Solo cambia cartilla.enc.

## Docentes: manual de funciones (+6 lecciones)
- man-ori +2 (funciones del orientador con casos; registro, confidencialidad y articulacion), man-dir +2 (funcion general de directivos; asignacion de funciones), man-sec +2 (no licenciados y periodo de prueba; funciones del docente de secundaria).
- Citas literales de la Resolucion MEN 3842 de 2022 (Anexo tecnico I: 1.1, 2.2.3, 3.7, 3.8), verificadas por assert. Solo cambia cartilla.enc.

## Docentes: Sobre el concurso, +7 lecciones de la prueba
- Bloque prueba +7: reclamaciones (2.7), ajustes razonables (2.2), experiencia traslapada y no doble contabilizacion (5.1.7-5.1.8), calculo del puntaje de experiencia con ejemplo (5.1.10), relacion con el empleo y sin ventaja territorial (5.1.9), desempate y vigencia de la lista, periodo de prueba (8).
- Citas literales del Anexo tecnico Docentes y Directivos Docentes 2026, verificadas por assert. Los valores por año de los ejemplos son ilustrativos y asi se dice en la leccion. Solo cambia cartilla.enc.

## Docentes: fisica, quimica y biologia (+9 lecciones)
- esp-fis +3 (mecanica con problemas, masa/peso/densidad, electricidad-magnetismo-gravitacion), esp-qui +3 (estructura de la materia, reacciones y mol, niveles de representacion), esp-bio +3 (celula y transporte, genetica, ecosistemas y energia).
- Estandares citados literalmente del documento de Ciencias Naturales (MEN 2004), verificados por assert; todos los calculos numericos se comprobaron en codigo. Solo cambia cartilla.enc.

## Docentes: refuerzo de lecciones por nivel en gestion academica y comunitaria (+5)
- fa-ga +4 (dominio curricular preescolar/primaria, planeacion secundaria/media, pedagogicas secundaria/media, evaluacion preescolar/primaria) y fa-gco +1 (interaccion con la comunidad en media). Cada una lleva su campo niv (doc-pri o doc-sec) para que solo la vea ese nivel.
- Citas literales de Ley 115 (arts. 16, 21, 30) y Decreto 1075 (arts. 2.3.3.3.3.1, .3.3, .3.4, .3.5, .3.6), verificadas por assert. Solo cambia cartilla.enc.

## Docentes: bloque general del manual (+5 lecciones)
- manual +5: siete competencias comportamentales en situaciones, licenciado y tecnologo (3.1), titulos extranjeros/registro calificado/habilitacion (3.2-3.3), saberes previos y evaluacion de desempeño (3.4 y 3.6), perfil de media tecnica (3.5).
- Citas literales de la Resolucion MEN 3842 de 2022 (Anexo tecnico I: 2.1.2, 3.1 a 3.6), verificadas por assert. Solo cambia cartilla.enc.

## Cambio del numero de WhatsApp en todo el sitio
- Numero anterior 316 698 2472 (wa.me/573166982472) -> nuevo 312 690 8321 (wa.me/573126908321).
- sitio.pak: 897 de 968 archivos (paginas, guias, cargos, terminos). php.pak: 6 de 16 (correo del ebook, correos de acceso, chat con la IA, suscripcion, lib). cartilla.enc: 28 apariciones (enlaces y textos). Mismo largo en bytes, asi que no cambian offsets de la cartilla.
- NO se tocaron constantes numericas de funciones hash (por ejemplo 3266489909), que no son telefonos.
- Quedan fuera del repo y deben revisarse a mano: imagenes con el numero impreso, PDF/ebooks en Drive, textos de Facebook, perfil de WhatsApp Business, y cualquier numero guardado en la base o en ajustes del servidor.

## Vuelve el numero de WhatsApp 316 698 2472 (revierte el cambio al 312 690 8321)
- Motivo: el WhatsApp 312 690 8321 quedo "en revision" por varios registros seguidos y no recibe mensajes de la pagina; el 316 698 2472 tiene la cuenta restaurada con grupos y chats. Medida temporal: se devuelve el numero para no perder ventas.
- Se revirtio el commit 99b96e1 (sitio.pak, php.pak, cartilla.enc quedan como en b36ac1a). No hay otros cambios posteriores a ese commit, asi que la reversion es exacta. Se verifico HMAC de los tres paquetes: 0 apariciones del 312 y todas las del 316.
- Cuando el 312 690 8321 salga de revision y Ariel lo confirme, repetir el reemplazo (ver entrada anterior "Cambio del numero de WhatsApp en todo el sitio").
- Fuera del repo (PDF en Drive de las guias docente/Procuraduria/comportamentales) siguen con 312 690 8321: hay que volver a corregirlos si el cambio dura.

## SEO: titulos y descripciones mas cortos y con el concurso al inicio (186 paginas)
- Solo cambia sitio.pak, y dentro de el unicamente las etiquetas <title> y <meta name="description"> de 186 paginas; el resto de cada archivo es identico (se verifico comparando cada archivo contra el publicado). No cambian aspecto, textos visibles, enlaces ni imagenes.
- cargos/procuraduria (126): el titulo pasa de "Cargo · Dependencia · Procuraduría" a "Procuraduría 2026 · Cargo · Dependencia" (se conserva el "(2)" de los repetidos). cargos/dian (2): "DIAN 2676 · Cargo · Dependencia". concursos (Docentes): "Concurso docente 2026 · Empleo: requisitos y vacantes".
- Descripciones: 48 que pasaban de 160 caracteres quedan dentro del limite (en las de vacantes se quito la frase final "Mira cuantas hay en cada empleo."; se reescribieron guias/prueba-el-metodo y concursos/examen-estado-abogados). Ningun titulo nuevo repetido.
- Motivo: Search Console (6/11) mostraba titulos cortados en los resultados. Los titulos siguen siendo largos (en Google se corta el final, que es la dependencia); lo importante queda al inicio.
- Lo que Google rechazo ("Rastreada: sin indexar") y sigue pendiente, con aprobacion de Claudia antes de tocar: guias/noticias-concursos y dos cargos DIAN (gestor-ii-administracion-de-cartera-y-recaudo-devoluciones, inspector-i-gestion-del-riesgo-y-programas). guias/simulacro-dian-2676 y los otros guias/simulacro-* son paginas de paso con noindex a proposito: no tocarlas.
- Para otro Claude: si vas a editar sitio.pak, parte del sitio.pak actual del repo (no de una copia local) y no pises estas etiquetas. Para volver atras: revertir este commit.

## Docentes: capitulo nuevo de etica, psicotecnica y evaluacion, y ayudas visuales en Decreto 1278 y Convivencia
QUE SE HIZO
- Cartilla Docentes (cifrada en cartilla.enc). Tres capitulos nuevos, entre las competencias comportamentales y lectura critica: "etica" (Etica y ciudadania, 8 lecciones, 33 preguntas), "psico" (Prueba psicotecnica y entrevista, 6 lecciones, 24 preguntas) y "evaprend" (Evaluar para aprender: Decreto 1290, SIEE y evaluacion formativa, 6 lecciones, 23 preguntas). Se agregaron a CORE de DOCAPP, asi aparecen en todos los perfiles docentes.
- Mapas conceptuales y diagramas de flujo dentro de las lecciones de los tres capitulos nuevos y de nor-1278 (ingreso, periodo de prueba, escalafon, evaluaciones, deberes) y nor-conv (ruta, Tipo I/II/III, comite, conflicto/agresion/acoso). Tres videos cortos con voz femenina latinoamericana neutra (Piper es_MX) incrustados en base64 en etica, nor-1278 y nor-conv (1 min 20 s a 1 min 45 s).
- Verificado antes de subir: los demas bloques quedaron identicos; solo cambian nor-1278 y nor-conv (lecciones intactas, solo se insertaron figuras) y la linea CORE. Preguntas: 798 -> 878. Descifrado de ida y vuelta igual al HTML candidato. Prueba en Chrome a 400 px sin desbordes y videos con duracion correcta.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (sha igual a la base), se insertaron los bloques con scripts de /tmp/work (etica_data.py, psico_data.py, evalu_data.py, visuals.py, build2.py y build5.py), se cifro con la clave de .ce_key y se verifico. Antes de editar: git pull y descifrar el cartilla.enc actual, no partir de copias locales.
- Contenido de psicotecnica y entrevista basado en el Anexo tecnico CNSC 2026 (nums. 2.1, 2.2 y 6); el art. 4 del Decreto 1278 va parafraseado (no se pudo citar literal). Evaluacion basada en Decreto 1290 de 2009 compilado en el 1075 de 2015, seccion 3; sin cifras de asistencia (las define cada colegio).

QUE FALTA
- Videos para psico y evaprend; mapas y flujos en los capitulos de gestion academica por cargo (aula, orientador, directivo); leccion corta de TIC. Esperar los ejes tematicos del ICFES antes de agregar Constitucion, derecho administrativo o Ley 2383 de 2025. Voz: es Piper es_MX (no hay voz colombiana disponible).

## Docentes: mapas y flujos en evaluacion de desempeno y educacion inclusiva
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): 4 figuras nuevas dentro de lecciones existentes. ev-des: mapa de los cinco principios (leccion 2) y flujo de los cuatro momentos de la evaluacion (leccion 4). nor-incl: flujo de matricula de un estudiante con discapacidad (leccion 3) y flujo del PIAR al acta de acuerdo (leccion 4).
- Solo se insertaron figuras: el texto de las lecciones y las preguntas no cambiaron (verificado bloque por bloque contra lo publicado). Prueba en Chrome a 400 px sin desbordes.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert de ida y vuelta, se insertaron las figuras con visuals.py (flow y cmap) y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Mapas y flujos en gestion academica por cargo (aula, orientador, directivo), nor-715, nor-dir y nor-casos; leccion corta de TIC; videos para psico y evaprend.

## Docentes: mapas y flujos en gestion academica de aula, orientador y directivo
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): 5 figuras nuevas dentro de lecciones existentes. fa-ga: flujo "de donde baja tu planeacion" (leccion 3) y mapa de las cuatro ideas pedagogicas (leccion 5). fo-ga: mapa de articulacion del orientador y funciones del art. 32 de la Ley 1620 (leccion 1). fd-gd: flujo de seis pasos para planear con la Guia 34 (leccion 1) y mapa "cada asunto lo decide la instancia competente" (leccion 2).
- Solo se insertaron figuras: texto de lecciones y preguntas intactos (verificado bloque por bloque contra lo publicado). Prueba en Chrome a 400 px con perfiles primaria, matematicas, orientador y rector, sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se insertaron las figuras con visuals.py justo despues del parrafo que las explica y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en las lecciones especificas por nivel de fa-ga (preescolar y primaria, secundaria y media), en fo-ga restante, fd-ga, fd-gad y fd-gco, nor-715, nor-dir y nor-casos; leccion corta de TIC; videos para psico y evaprend.

## Docentes: videos de psicotecnica y evaluacion, figuras por nivel y 4 figuras de normatividad/directivos
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): video narrado de ~90 s al inicio de los capitulos "Prueba psicotecnica y entrevista" y "Evaluar para aprender". Cinco flujos especificos por nivel en fa-ga (secundaria y media, preescolar y primaria, conducta en clase, evaluar en primeros grados, reclamo de nota). Cuatro figuras nuevas: mapa de niveles y establecimientos (nor-715), mapa de funciones del rector (nor-715), flujo de evaluacion institucional anual (nor-dir) y flujo del orden del gasto en 8 pasos (fd-gad).
- Solo se agregaron videos y figuras: texto de lecciones y preguntas intactos (verificado bloque por bloque). Prueba en Chrome a 400 px sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert de ida y vuelta, se agregaron las figuras con visuals.py y los videos (mp4 en base64, voz Piper es_MX) y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en fd-ga, fd-gco, fo-gad, fo-gco y nor-casos; videos para otros capitulos; leccion corta de TIC solo si se pide.

## Docentes: 9 figuras en talleres de casos y gestion directiva/orientador
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): 5 flujos en los talleres de nor-casos (discapacidad a mitad de ano, ciberacoso, periodo de prueba, Fondo de Servicios Educativos, queja contra docente); fd-ga flujo "de los resultados a las decisiones"; fd-gco flujo de queja publica en redes y mapa de situaciones Tipo I, II y III; fo-gco mapa de la red de apoyo del orientador.
- Solo figuras: texto de lecciones y preguntas intactos (verificado bloque por bloque). Prueba en Chrome a 400 px sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se agregaron las figuras con visuals.py (flow y cmap) y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en fo-gad; videos para otros capitulos.

## Docentes: 2 figuras en gestion administrativa del orientador (fo-gad)
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): fo-gad leccion 1 mapa de uso seguro y reservado de recursos de orientacion; leccion 2 flujo de seguimiento de un caso de convivencia (acta, verificacion, escalamiento o remision).
- Solo figuras: texto y preguntas intactos. Prueba en Chrome sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se agregaron las figuras con visuals.py y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en fa-gad, fa-gco, fo-ga restante, antecedentes, cc, manual y fun-norm; videos para otros capitulos.

## Docentes: 13 figuras en aula (fa-gad, fa-gco), orientador (fo-ga), competencias y funciones del docente
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): fa-gad flujo para elegir un recurso y mapa del gobierno escolar; fa-gco flujo ante un padre molesto, flujo de proyecto con la comunidad y flujo del proyecto del agua (media); fo-ga mapa de protocolos Tipo I, II y III y flujo del Tipo III; cc flujo de escucha activa y de mediacion en 7 pasos; fun-norm flujos de evaluacion institucional y calendario, mapa de representacion estudiantil, flujos de sospecha de maltrato y de acceso/permanencia.
- Solo figuras: texto y preguntas intactos (verificado bloque por bloque). Prueba en Chrome a 400 px sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se agregaron las figuras con visuals.py y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en antecedentes (ant-*), manual y el resto de lecciones de cc y fun-norm; videos para otros capitulos.

## Docentes: 8 figuras en antecedentes (todos los cargos) y competencias comportamentales
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): mapas "como se reparten los 100 puntos" en ant-aula, ant-ori y ant-dir (rector, coordinador, director rural), con topes y puntos por factor; en cc, flujos del metodo STAR (liderazgo), reparto de tareas (trabajo en equipo) y metodo de la iniciativa.
- Solo figuras: texto y preguntas intactos (verificado bloque por bloque). Prueba en Chrome a 400 px sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se agregaron las figuras con visuals.py (flow y cmap) y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en manual y lecciones sueltas de cc y fun-norm; videos para otros capitulos.
