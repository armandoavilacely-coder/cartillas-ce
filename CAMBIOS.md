## 2026-11-18 · Admin: versión celular de Rendimiento y Estadísticas
- Qué: en pantallas pequeñas las cajas de Rendimiento van en una sola columna (antes una quedaba como tira vertical); el botón Cerrar no se parte; las tarjetas de cifras van de a dos por fila con números que se ajustan; se quitaron anchos mínimos que obligaban a deslizar tablas y el embudo; las tablas de comparación por origen se reacomodan; el menú inferior ya no parte "Comunicación".
- Por qué: en el celular se veía desordenado y con columnas aplastadas. En computador no cambia nada.

## 2026-11-18 · Admin: gráficas más claras en Rendimiento y Estadísticas
- Qué: las listas planas pasan a barras con etiqueta completa, porcentaje del total y la mayor resaltada; la hora pasa a columnas con eje, promedio y pico; el origen de visitas a una barra al 100 %; nuevas tablas "qué origen lleva más a WhatsApp / suscribe más" con tasa (clics entre visitantes del mismo origen); los ID numéricos de campaña de Meta se muestran como "Anuncio Meta …".
- Por qué: el volumen solo no dice qué origen es mejor; la tasa sí. Y los gráficos planos con texto cortado dificultaban leer. No cambia datos ni otras pantallas.

## 2026-11-18 · Admin: barra superior más compacta
- Qué: título más pequeño, se quita la palabra "ADMINISTRACIÓN" y el nombre de usuario en pantallas menores de 1600 px, y se reducen los espacios de los botones del menú.
- Por qué: que todo quepa en la barra sin barras de desplazamiento. Solo cambia la apariencia.

## 2026-11-18 · Admin: dona de estado de leads en Estadísticas
- Qué: nueva gráfica de dona (activos, en proceso, fríos, perdidos) en Estadísticas.
- Por qué: ver de un vistazo cómo está la base de clientes. Solo se agrega una caja; no cambia datos ni otras gráficas. El mapa de calor de leads por día y hora ya existía.

## 2026-11-18 · Admin: pantalla "Rendimiento de marketing"
- Qué: nueva pantalla en Comunicación con inversión Meta, conversaciones, costo por conversación y por venta, campañas, contenido que suscribe y lleva a WhatsApp, guías más leídas, origen de clics y mejor hora, y recomendaciones de la semana.
- Por qué: para decidir contenido y publicidad (Facebook, Instagram, WhatsApp) con datos reales que ya se guardan. No cambia ningún dato ni otra pantalla.


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

## Docentes: 7 figuras en funciones del docente (fun-norm), manual y competencias
QUE SE HIZO
- Cartilla Docentes (cartilla.enc): fun-norm mapa de las nueve areas obligatorias (Ley 115 art. 23), flujo para modificar el PEI y flujo para cambiar el plan de estudios; cc flujo del ciclo de mejora SMART; manual mapa de las 7 competencias comportamentales y flujos de titulos habilitantes y de quien es licenciado.
- Solo figuras: texto y preguntas intactos (verificado bloque por bloque). Prueba en Chrome a 400 px sin errores.

COMO SE HIZO (para continuar)
- Se descifro el cartilla.enc vigente (igual a la base), se reserializo DOCDATA con assert, se agregaron las figuras con visuals.py y se cifro con la clave de .ce_key. Antes de editar: git pull y descifrar el cartilla.enc actual.

QUE FALTA
- Figuras en lecciones sueltas (cc 4, manual restante, fun-norm restante, fa-ga restante); videos para otros capitulos.

## 7 nov 2026, 14:10 — Publicidad: calendario de 14 días (7 al 20 de noviembre), 3 publicaciones diarias
QUE SE HIZO
- En la sección Publicidad del admin se agregan 42 publicaciones (solo Procuraduría y Docentes), 3 por día, del sábado 7 al viernes 20 de noviembre de 2026: 6 en la semana del 2 al 8 (días 7 y 8), 21 en la semana del 9 al 15 y 15 en la semana del 16 al 22 (hasta el 20).
- Mezcla con marketing de contenidos: noticias de calendario, contenido útil (puntaje, reclamaciones y apelación, funciones, requisitos y competencias del empleo 4SU-11; etapas, normas, PIAR y DUA, convivencia escolar y consejos de estudio en Docentes), retos con respuesta a las 9:00 p. m., encuestas y piezas de transparencia sobre lo que se vende.
- Cada una lleva imagen de feed (4:5) y de historia (9:16), con ilustración y la palabra del concurso en grande, y textos para página, grupos, WhatsApp, historia, estado y respuesta a comentarios.
COMO SE HIZO
- Parche sobre el cartilla.enc ya publicado (commit db20e5b): se descifró, se agregaron las semanas al JSON de pub-data (id 2026-11-09 y 2026-11-16, y las 6 publicaciones de los días 7 y 8 a la semana 2026-11-02) y se volvió a cifrar. Control: el resto de la cartilla queda idéntico, las semanas anteriores no cambian y el cifrado ida y vuelta coincide.
QUE FALTA
- Verificar en la plataforma oficial las fechas de la Procuraduría el día anterior a cada pieza de calendario (7, 9, 11, 12, 16, 17 y 20 de noviembre) y confirmar el texto del art. 40 del Decreto 1965 de 2013 antes de la pieza del 16.
- Confirmar si existe simulacro gratis de Procuraduría (los textos de respuesta lo ofrecen).

## 7 nov 2026, 14:45 — Publicidad: corrección de fechas de Docentes y nuevo diseño de las 42 piezas
QUE SE HIZO
- Se corrige la información de Docentes con la fuente oficial (página de la CNSC y Resolución 11673 del 6 de noviembre de 2026): la inscripción para personas con discapacidad va del 23 de noviembre de 2026 al 15 de enero de 2027, con más de 2.200 vacantes reservadas. Se quitan las fechas no confirmadas que venían de medios ("Ene–Feb 2027" y "segundo semestre de 2027") de la pieza del calendario, "no estudies a última hora" y "errores al estudiar", y de sus textos.
- Nuevo diseño de las 42 imágenes (feed y historia) de Procuraduría y Docentes: cada concurso con el estilo de color y letra de su entidad (Docentes azul y amarillo; Procuraduría azul marino y dorado), sin logos; fondos blancos y azules intercalados con degradado, textura y brillos; más espacio entre textos y cuadros; se quitan tarjetas que repetían lo del cuadro principal; las historias respetan las zonas seguras.
COMO SE HIZO
- Parche sobre el cartilla.enc ya publicado (commit 9976555): se descifró, se reemplazaron por id las 42 publicaciones de pub-data (textos de Docentes corregidos e imágenes nuevas) y se volvió a cifrar. Control: la semana del 26 de octubre y las 17 primeras publicaciones de la semana del 2 de noviembre quedan idénticas; el resto del cartilla.enc no cambia.
QUE FALTA
- Verificar en la plataforma oficial las fechas de la Procuraduría el día anterior a cada pieza de calendario (9, 11, 12, 16, 17 y 20 de noviembre) y confirmar si existe simulacro gratis de Procuraduría.
- Las fechas de inscripción general y de pruebas de Docentes las anunciará la CNSC; actualizar las piezas cuando salgan.

## 2026-11-07 · Cartilla Docentes: ampliación del área de matemáticas
QUE SE HIZO: en el capítulo «Tu área: matemáticas» se agregaron 30 preguntas nuevas (de 15 a 45) y la lección «Grados 10.° y 11.°: lo que cambia en la media».
COMO SE HIZO: se anexaron al final del capítulo (sin mover las lecciones existentes, para conservar el avance de los usuarios). Preguntas de caso con enunciado largo y tres opciones plausibles, por pensamiento (numérico, variacional, espacial y métrico, aleatorio, didáctica).
QUE FALTA: citar textualmente los estándares de 10.° y 11.° (hoy parafraseados); ampliar «Práctica de aula: matemáticas con casos» (10 preguntas); actualizar fechas cuando la CNSC anuncie inscripción general y pruebas.

## 2026-11-07 · Cartilla Docentes: estándares textuales de 10.° y 11.° en matemáticas
QUE SE HIZO: la lección «Grados 10.° y 11.°: lo que cambia en la media» ahora cita textualmente los estándares de décimo a undécimo por pensamiento (numérico, variacional, espacial, métrico y aleatorio) del MEN (2006). Se quitaron menciones que no están en los estándares (sistemas de ecuaciones, volúmenes).
COMO SE HIZO: se tomó el texto del PDF oficial de los Estándares Básicos de Competencias en Matemáticas y se reemplazó la lección parafraseada; sin mover lecciones ni preguntas.
QUE FALTA: ampliar «Práctica de aula: matemáticas con casos»; actualizar fechas cuando la CNSC anuncie inscripción general y pruebas.

## 2026-11-07 · Cartillas: letrerito «Nuevo» para contenido nuevo
QUE SE HIZO: la cartilla Docentes muestra la etiqueta «NUEVO» en el capítulo (inicio), en cada lección nueva (lista y encabezado) y «N NUEVAS» en el botón de práctica. Quedaron marcadas la lección de grados 10.° y 11.° y las 30 preguntas nuevas de matemáticas.
COMO SE HIZO: campo `nuevo` en capítulo, lección o pregunta de los datos; la cartilla lo lee al armar los capítulos y pinta la etiqueta (estilo propio inyectado). Sin mover lecciones ni avance de usuarios.
QUE FALTA: aplicar el mismo mecanismo en las cartillas DIAN y Procuraduría; regla acordada: todo contenido nuevo en cualquier concurso lleva «Nuevo». Retirar la etiqueta cuando deje de ser novedad.

## 2026-11-07 · Cartillas: el audio de la página lee pesos y no dólares
QUE SE HIZO: el audio de página, de resúmenes y de videos con voz de todas las cartillas (Docentes, DIAN y Procuraduría) ahora lee los valores con "$" como pesos (ej. "$4.500.000" se lee «4500000 pesos»; "$3,5 millones" como «3,5 millones de pesos»; "COP" como «pesos colombianos»).
COMO SE HIZO: un script al inicio del archivo intercepta speechSynthesis.speak y reescribe el texto antes de que suene; no toca el texto que se ve en pantalla.
QUE FALTA: confirmar escuchando con una voz real en el celular.

## 2026-11-07 · Cartillas DIAN y Procuraduría: explicaciones de los casos en su pregunta correcta
QUE SE HIZO: en la cartilla DIAN más de 100 de las 167 explicaciones completas de los casos aparecían en la pregunta equivocada (la respuesta marcada como correcta sí estaba bien). Se reasignaron todas a su pregunta, en los casos y en el simulacro. Procuraduría usaba el mismo sistema y quedó con la misma corrección.
COMO SE HIZO: las explicaciones se asignaban por posición del caso (ej. "58.0") y al agregar casos las posiciones se corrieron. Ahora la clave es el texto del caso y de la pregunta, así que no se descuadra aunque se agreguen casos. Se verificó cargando la cartilla en un navegador: 1.429 preguntas DIAN revisadas, las 167 explicaciones caen en su pregunta.
QUE FALTA: ampliar explicaciones muy cortas (algunas solo citan el artículo, ej. "Artículo 89.").

## 2026-11-07 · Cartilla DIAN: Word y Excel aparece en el simulacro por capítulo
QUE SE HIZO: el capítulo «Word y Excel: del nivel básico al medio» no salía en la lista del simulacro por capítulo (sus 52 preguntas solo salían en el general). Ya aparece.
COMO SE HIZO: se agregó su nombre a la lista de bloques (BLOQUES.OFIM) que alimenta el selector del simulacro. Verificación completa de la cartilla DIAN en navegador: 33 capítulos, 530 lecciones, 540 fichas y 1.429 preguntas sin claves inválidas ni opciones repetidas.
QUE FALTA: equilibrar el largo de opciones en 119 preguntas donde la correcta es notoriamente la más larga; ampliar la explicación «Artículo 89.» (recurso por correo electrónico).

## 2026-11-07 · Cartillas DIAN y Procuraduría: opciones equilibradas y quices sin respuestas regaladas
QUE SE HIZO: DIAN: en 76 preguntas la respuesta correcta era notoriamente la opción más larga; se reescribieron las opciones incorrectas para que el largo sea parejo y sigan siendo creíbles (la correcta y su explicación no cambian). Se amplió la explicación «Artículo 89.» (recurso por correo electrónico). Procuraduría: auditoría completa (27 capítulos, 387 lecciones, 819 preguntas de casos, simulacro y quices) y se quitaron de los quices 24 preguntas de concepto cuya descripción ya traía escrita la respuesta.
COMO SE HIZO: script al final de cada cartilla que reemplaza las opciones por texto de pregunta + respuesta correcta (en casos, simulacro y repaso) y filtra el banco del quiz de Procuraduría. Verificado en navegador.
QUE FALTA: Procuraduría: ampliar 293 explicaciones de casos demasiado cortas (USU, COMP, PGN y DISC primero); equilibrar el largo en 381 preguntas de quices generados desde glosario y normas; nota de vigencia (Ley 1952, art. 56) en la prohibición para exservidores de la Ley 1474.

## 2026-11-08 21:15 - sitio.pak y php.pak
QUE SE HIZO: todos los precios de las cartillas suben $5.000 en todos los concursos y niveles (DIAN, Procuraduria, CAR y Docentes): 35/40/45/50 mil pasan a 40/45/50/55 mil. Paquete DIAN + Procuraduria: de $70.000 a $80.000. Se cambiaron 895 paginas (4.099 valores: botones Pagar, "desde $", preguntas frecuentes, terminos, guias, calculadora de pagar.html), el panel y el chat (lib.php, chat_core.php) y el cobro real (acceso/wompi.php, funcion wp_precio; este archivo no se instala desde GitHub: lo subio Claudia a mano a public_html/acceso). No cambian: el curso de Examen de Estado para abogados ($50.000), el Plus (+$20.000) ni gastrobarpossystem.
COMO SE HIZO: la primera version de los paquetes salio sin firma valida (se reutilizo el encabezado anterior) y actualizar.php la rechazo; se volvieron a firmar con HMAC (site/php + clave) y se verifico contra la firma de la version anterior. Sobre los paquetes publicados el 6 de noviembre (nada mas cambio); cada valor se reemplazo una sola vez con +5.000 y se verifico pagina por pagina que el resto del texto quedara identico. wompi.php se tomo de la copia del servidor. El monto que Wompi cobra y el que muestra pagar.html coinciden por concurso y nivel.
QUE FALTA: rehacer piezas con el precio viejo (ebook de Docentes del Drive, imagenes de anuncios y og-*.png con precio); revisar la zona de pagos en la pagina real.

## 2026-11-08 21:40 - sitio.pak y php.pak
QUE SE HIZO: (1) pagar.html: etiqueta Docentes pasa de "82 acuerdos CNSC" a "90 entidades". (2) descargar.php: los enlaces de respaldo de Drive de los 3 ebooks apuntan a los PDFs corregidos (docente v3, procuraduria v3, comportamentales v2) con precio por nivel y WhatsApp 316 698 2472.
COMO SE HIZO: se tomaron los paquetes vigentes, se cambio solo eso y se volvieron a firmar (HMAC verificado); php -l ok.
QUE FALTA: compartir como "cualquier persona con el enlace" los v3 de Docentes y Procuraduria en Drive, y subir los 3 PDFs a ce_data/ebook/ en el servidor. FORMATO-CARTILLA.md y cartilla nueva siguen sin publicar.

## 2026-11-08 22:15 - sitio.pak
QUE SE HIZO: se corrigieron 2.136 precios en los mensajes prellenados de los botones de WhatsApp (712 paginas de cargos y concursos), que seguian con el precio viejo porque el signo $ va codificado como %24. Ahora coinciden con el precio mostrado en cada pagina.
COMO SE HIZO: sitio.pak vigente, una sola pasada 35>40, 40>45, 45>50, 50>55 sobre %24NN.000 (curso abogados excluido); firma HMAC verificada. Auditoria: sin 312 690, sin 82 acuerdos, un solo WhatsApp (316 698 2472) y sin enlaces internos rotos.
QUE FALTA: decidir si se reemplazan los textos "diez preguntas gratis" (home, DIAN, Procuraduria, CAR y guias) por el simulacro gratis de 30 preguntas.

## 2026-11-08 22:25 - sitio.pak
QUE SE HIZO: sitemap.xml con lastmod 2026-11-08 en las 885 direcciones (el contenido de casi todas cambio hoy por los precios nuevos), para que Google vuelva a rastrearlas.
COMO SE HIZO: sitio.pak vigente, solo sitemap.xml; firma HMAC verificada.
QUE FALTA: las paginas de simulacro y capitulo gratis son noindex a proposito (redirigen al registro), por eso no se les tocaron titulos. Pedir indexacion en Search Console de las paginas de Docentes y Procuraduria; decidir el texto de las "diez preguntas gratis".

## Regla de commits (pedida por Claudia el 2026-11-08)
Todo commit y toda entrada de este historial debe llevar: QUE SE HIZO, POR QUE (el motivo), COMO SE HIZO y QUE FALTA. Aplica tambien a la otra IA que edita el repositorio.

## 2026-11-08 — Noticias propias y banner DIAN
QUE SE HIZO: la página de noticias ahora tiene notas propias (DIAN, Procuraduría, CAR, nueva sección Docentes, CNSC); el banner de cuenta regresiva de index y dian pasa a "Hoy se aplica la prueba escrita" y oculta el contador.
POR QUE: crear contenido auténtico y actual; el contador ya había llegado a cero.
COMO SE HIZO: edición de guias/noticias-concursos.html, index.html y dian.html dentro de sitio.pak y firma HMAC.
QUE FALTA: simulacros indexables por concurso y enlaces internos a cargos; reconciliar fechas de docentes.html.

## 2026-11-08 — Noticias como portal de noticias
QUE SE HIZO: guias/noticias-concursos ahora es un portal (portada, noticia principal, tarjetas por concurso, otros medios, fuentes oficiales) y 4 artículos propios en guias/noticias/<slug> con esquema NewsArticle; agregados al sitemap.
POR QUE: contenido auténtico e indexable, con aspecto de página de noticias real.
COMO SE HIZO: generador /tmp/np/build.py sobre sitio.pak con firma HMAC.
QUE FALTA: verificar que las URLs sin .html funcionen en subcarpeta; más artículos con la revisión diaria.

## 2026-11-08 — Receptor temporal de la OPEC publica de SIMO
QUE SE HIZO: se agrega opec-ingest.php (con clave y vencimiento 2026-11-10) para guardar en ce_data/opec la OPEC publica de SIMO.
POR QUE: guardar requisitos de cada cargo (estudio, experiencia, funciones) y no volver a consultar SIMO; base para evaluar hojas de vida.
COMO SE HIZO: php.pak = el publicado + un archivo nuevo, firmado con HMAC; el navegador envia los datos publicos de SIMO por bloques.
QUE FALTA: bajar los bloques, guardarlos en Drive y alimentar el modulo de hoja de vida.

## 2026-11-08 — Menú: CAR pasa a Noticias
QUE SE HIZO: en el menú superior de 900 páginas, el enlace "CAR" (/#car) se cambia por "Noticias" (/guias/noticias-concursos).
POR QUE: CAR ya está dentro del menú Concursos; el espacio se usa para las noticias propias.
COMO SE HIZO: reemplazo exacto del enlace en el encabezado de cada página dentro de sitio.pak, con firma HMAC.
QUE FALTA: nada de este cambio.

## 2026-11-08 — Copia temporal de la OPEC para llevarla al Drive
QUE SE HIZO: el bloque temporal de diagnostico.php (?opec=1) agrega la accion publicar/borrar, que deja un .json.gz con nombre no adivinable para bajar la OPEC publica de SIMO y la borra despues.
POR QUE: el filtro anti-robots del hosting no deja bajar los datos por consola; hace falta un archivo estatico para llevarlos al Drive.
COMO SE HIZO: php.pak publicado con diagnostico.php modificado, firmado con HMAC.
QUE FALTA: bajar el archivo, borrarlo del servidor y subir las ofertas al Drive; quitar el bloque temporal despues del 10 nov.

## 2026-11-09 — Evalúa tu hoja de vida (pago de $10.000 por evaluación)
QUE SE HIZO: página nueva /evalua-hoja-de-vida (subir hoja de vida, código de un solo uso, aceptación obligatoria de privacidad y términos); franja visible en inicio, DIAN, Procuraduría y Docentes; enlace "Hoja de vida" en el menú de 901 páginas; pagar.html muestra el código y el enlace correcto cuando el pago es de este producto (código que empieza por V-). Paquete php: cv.php (analiza con Haiku en dos pasos contra los requisitos exactos de la OPEC), _cv_opec.php (índice de 4.956 cargos de concursos abiertos) y _cv_codigos.php (códigos de una sola evaluación).
POR QUE: ofrecer a los aspirantes una evaluación de su hoja de vida frente a los requisitos reales de cada cargo, cobrada por evaluación (costo de IA cercano a US$0,004).
COMO SE HIZO: sitio.pak y php.pak firmados con HMAC. El código solo se consume si el análisis sale bien. La hoja de vida no se guarda; sí el registro de aceptación. wompi.php (con el producto "cv") y los tres php nuevos los subió Claudia a mano; el servidor no crea archivos nuevos desde GitHub.
QUE FALTA: prueba real con una hoja de vida; competencias solo por funciones y Decreto 815 (los manuales PDF son escaneos); fechas de inscripción por proceso; quitar el bloque temporal OPEC de diagnostico.php antes del 10 nov (los datos en ce_data/opec se conservan).

## 2026-11-09 — Código de supervisión para Evalúa tu hoja de vida
QUE SE HIZO: _cv_codigos.php acepta un código maestro de supervisión que no se consume y permite probar el analizador sin pagar.
POR QUE: Claudia necesita supervisar y probar el servicio de evaluación sin comprar un código cada vez.
COMO SE HIZO: solo se guarda el hash SHA-256 del código en el archivo (no el código); php.pak firmado con HMAC. Siguen vigentes el tope de 300 evaluaciones diarias y la aceptación obligatoria de privacidad y términos.
QUE FALTA: si el código se filtra, generar otro y publicar el hash nuevo.

## 2026-11-09 Evalúa tu hoja de vida: se retira del sitio mientras siguen las pruebas
QUE SE HIZO: se quita el enlace "Hoja de vida" del menú (901 páginas) y la franja "Evalúa tu hoja de vida" de inicio, DIAN, Procuraduría y Docentes; sitio.pak firmado de nuevo.
POR QUE: la evaluación sigue en pruebas (equivalencias estudio-experiencia, manuales, puntaje de antecedentes) y Claudia pidió no mostrarla al público todavía.
COMO SE HIZO: se quitaron del html el enlace y el bloque de la franja; la página /evalua-hoja-de-vida, cv.php y el pago siguen instalados para pruebas con el código de supervisión; pagar.html conserva el retorno del código V- para quien ya pague.
QUE FALTA: terminar pruebas y volver a mostrar enlace y franjas; texto de manuales por entidad; puntaje de valoración de antecedentes; quitar el bloque temporal OPEC de diagnostico.php antes del 10 nov.

## 2026-11-09 Noticia Docentes: inscripción de vacantes de discapacidad desde el 23 de noviembre
QUE SE HIZO: se actualiza la noticia de Docentes (mismo enlace) y su tarjeta en el portal de noticias: la CNSC, con la Resolución 11673 del 6 de noviembre de 2026, fijó el inicio de la inscripción de las 2.255 vacantes reservadas a personas con discapacidad (89 entidades, procesos 2917 a 3006) el 23 de noviembre de 2026; la inscripción general sigue como proyección 2027.
POR QUE: la nota anterior hablaba solo de fechas proyectadas y quedó vieja; Claudia pidió revisar la información de Docentes y sacar la noticia, con datos nuevos y de fuente oficial.
COMO SE HIZO: edición de guias/noticia-concurso-docente-2026-28000-vacantes.html y guias/noticias-concursos.html dentro de sitio.pak (firma HMAC); fuente: aviso de la CNSC del 6 de noviembre de 2026. No se usó la competencia como fuente.
QUE FALTA: confirmar la fecha de cierre de esta inscripción en el aviso de la CNSC (no pude abrir la página oficial desde aquí) y agregarla; publicar la noticia de inscripción general cuando haya fecha oficial.

## 2026-11-09 Noticia Docentes: fecha de cierre confirmada
QUE SE HIZO: la noticia de Docentes y su tarjeta en el portal indican que la inscripción de las vacantes reservadas a personas con discapacidad va del 23 de noviembre de 2026 al 15 de enero de 2027 (se quita la nota que pedía confirmar el cierre).
POR QUE: Claudia verificó en la página oficial de la CNSC (cnsc.gov.co) el banner con esas fechas.
COMO SE HIZO: edición de guias/noticia-concurso-docente-2026-28000-vacantes.html y guias/noticias-concursos.html dentro de sitio.pak firmado con HMAC.
QUE FALTA: publicar la noticia de inscripción general cuando haya fecha oficial.

## 9 nov 2026, 11:40 - sitio.pak (buscador de cargos)
- El buscador de cargos (inicio, /dian y /procuraduria) ahora encuentra por número de convocatoria: "01-2026", "1-2026", "234-2026" o "Convocatoria 01 - 2026" (también con "empleo" o "N.º" delante). Sale la cartilla del cargo al que pertenece ese empleo (ej. 01-2026 = Asesor 1AS-19 · Disciplinario; 234-2026 = Sustanciador 4SU-11). Solo Procuraduría. El texto de ayuda del buscador incluye el ejemplo 234-2026.

## 9 nov 2026, 11:55 - sitio.pak (buscador de /pagar)
- El buscador de cargo de la página de pago (/pagar) también encuentra por número de convocatoria: "01-2026", "234-2026", "Convocatoria 01 - 2026". Coincidencia exacta con el Empleo (1 no trae 10 ni 11). El texto del campo ahora dice "Cargo, código, N.º de empleo o convocatoria (01-2026)".

## 9 nov 2026, 12:20 - sitio.pak (todos los buscadores de cargo)
- Los buscadores de cargo del inicio, /dian, /procuraduria, CAR, Docentes y /pagar ahora aceptan casi cualquier forma de escribir: "1as19", "1AS-19", "1as 19", "asesor grado 19", "sustanciador 4su11", "01-2026", "01 de 2026", "convocatoria 234", "empleo 1", "N.º 234" y "OPEC 263296". Se ignoran palabras de relleno (convocatoria, empleo, grado, nivel, de, del...), se separa por guiones y puntos, y se compara también sin separadores. Convocatoria/empleo con número usa coincidencia exacta (1 no trae 10 ni 11). En el inicio, "OPEC 263296" ahora funciona igual que "263296".
- No cambia: el selector dentro de la cartilla cifrada ni los bots de chat/WhatsApp.

## 9 nov 2026, 17:00 - sitio.pak (enlace de Facebook en el encabezado)
QUE SE HIZO: se agregó un botón con el logo de Facebook (azul) en el encabezado, entre el menú ("Preguntas") y el botón de modo claro/oscuro, que abre https://www.facebook.com/concursosdelestado/ en otra pestaña. Está en las 901 páginas que tienen ese encabezado. En celular se oculta junto con el botón de la luna, como ya hacía el encabezado.
POR QUE: Claudia pidió incorporar el enlace de la página de Facebook al sitio, arriba y no en el pie de página.
COMO SE HIZO: se insertó un enlace con las clases "thm cefb" (mismo estilo del botón de la luna) justo antes del botón #thm en cada página, dentro de sitio.pak firmado con HMAC. Solo cambian esas 901 páginas.
QUE FALTA: publicar cuando Claudia diga "publica". Si quiere el enlace también en celular, hay que dejarlo visible en la regla móvil del encabezado.

## 9 nov 2026, 17:30 - sitio.pak (SEO: convocatoria en las páginas de cargos de Procuraduría)
QUE SE HIZO: en las 380 páginas de cargos de Procuraduría (/cargos/procuraduria/...) se agregó el número de convocatoria (ej. "Convocatoria No. 57-2026") en la primera línea visible bajo el título y en la meta descripción y og:description (hasta 3 convocatorias en la descripción, todas en el texto de la página).
POR QUE: Search Console muestra que casi todo el tráfico es DIAN y que los clientes buscan por número de convocatoria; las páginas de Procuraduría no lo mencionaban.
COMO SE HIZO: el número sale del campo de empleos de cada cargo en el buscador (Empleo N = Convocatoria N-2026, verificado con la convocatoria oficial No. 01-2026). Solo cambian esas 380 páginas dentro de sitio.pak firmado con HMAC.
QUE FALTA: lo mismo para DIAN no aplica (el concurso ya se presentó); revisar en Search Console las 31 páginas con noindex.

## 9 nov 2026, 19:55 - embudo de ventas del admin (limpieza de datos, sin cambio de código)
QUE SE HIZO: se vació el embudo de ventas (Admin > Ventas > Embudo): de 213 contactos se borraron 127 que no habían cerrado (95 Nuevo contacto, 20 Consulta, 11 Precio enviado, 1 Esperando pago). Se conservaron los 86 de "Código entregado". No cambió ningún archivo del sitio ni del servidor: no hay sitio.pak ni php.pak nuevos.
POR QUE: Claudia quería empezar de cero con el embudo; la mayoría eran contactos estancados de hace 10 a 20 días y con el precio viejo ($35.000). Se conservaron los clientes para no perder el historial de ventas ni las estadísticas (cierre y vendido del mes). Los códigos de acceso (accesos_admin) no se tocaron.
COMO SE HIZO: con la sesión de administradora, se llamó a la API del admin (crm_lista y luego crm_borrar, uno por uno, sobre las etapas distintas de "activo"). Antes se descargó el respaldo completo en JSON (respaldo-embudo-2026-11-09.json, en Descargas de Claudia y una copia en el localStorage del navegador del admin). Verificado después con crm_lista: 86 contactos, todos en "activo".
QUE FALTA (para la IA que edita cartilla.enc, donde vive la pantalla del embudo): quitar las barras de desplazamiento de cada columna del tablero y hacerlo más dinámico. (1) Las columnas crecen con su contenido, sin scroll interno. (2) Cada columna muestra solo las 5 tarjetas con seguimiento más urgente y un botón "ver todas". (3) Indicadores y Comprobante aparecen solo cuando tienen contactos. (4) Mover una tarjeta de etapa con un solo toque y actualizar al instante el contador de cada etapa. Publicar solo cuando Claudia diga "publica".

## 10 nov 2026 - sitio.pak (celular: menú inferior al alcance del pulgar y normas de accesibilidad móvil)
QUE SE HIZO: en las 901 páginas del sitio, en pantallas de hasta 640 px, se agregó una barra fija inferior con 5 botones: Inicio, Mi cargo, botón central amarillo, Mi cartilla y Más. El botón central es "Simulacro" (lleva al simulacro gratis del concurso de esa página) y en las páginas de cargo pasa a "Activar" (abre el pago, o WhatsApp si el pago aún no está habilitado). "Más" abre el menú lateral de siempre. Se oculta al escribir en un campo para no tapar el teclado. Se agregó el enlace "Saltar al contenido" (con id en <main>), objetivos táctiles de 44 px (botones, enlaces del pie, resúmenes de preguntas frecuentes, casillas 24 px), campos de 16 px (evita el zoom automático de iOS) y letra mínima de 12,5 px en etiquetas.
POR QUE: Claudia pidió mejorar la parte móvil según normas internacionales (WCAG 2.2, Apple HIG y Material: objetivos de 44-48 px, navegación inferior al alcance del pulgar).
COMO SE HIZO: bloque <style id="ce-mbnav-css">, <nav id="mbnav"> y <script id="ce-mbnav-js"> insertados antes de </body> en cada página. En móvil se ocultan el botón "Cuenta gratis" y el menú hamburguesa del encabezado, el botón flotante de WhatsApp y la barra .dock de las páginas de cargo (sus funciones quedan en la barra inferior). El botón de compartir y el aviso de cookies suben para no quedar tapados. El aviso de cookies conserva el texto legal completo (Meta y Google) y es más compacto. Medido con Chrome a 360 px: sin desborde horizontal en las páginas de prueba y objetivos pequeños bajaron de unos 41 a unos 3.
QUE FALTA: pagar.html y las guías de simulacro sin encabezado no llevan la barra. WhatsApp quedó dentro de "Más" (menú lateral). Probar en un celular real y revisar el contraste del botón compartir sobre texto.

## 10 nov 2026 - sitio.pak (celular: los enlaces abren en la misma pestaña)
QUE SE HIZO: en pantallas de hasta 640 px, los enlaces que abrían pestaña nueva (WhatsApp, Facebook, términos, privacidad, CNSC, menú de compartir) ahora abren en la misma pestaña. En computador no cambia.
POR QUE: Claudia pidió que en modo celular no se abran pestañas diferentes porque no hay necesidad.
COMO SE HIZO: script <script id="ce-mbself"> en las 901 páginas, después del script del menú inferior: al tocar un enlace con target="_blank" y pantalla <= 640 px, cambia el target a _self (escucha en captura, cubre enlaces creados después). Probado con Chrome: móvil misma pestaña, escritorio pestaña nueva.
QUE FALTA: si alguien no tiene WhatsApp instalado, saldrá del sitio hacia la página de WhatsApp.

## 10 nov 2026 - php.pak (diagnostico.php: se quita el receptor temporal de OPEC)
QUE SE HIZO: se eliminó de diagnostico.php el bloque temporal que recibía la OPEC pública de SIMO (se activaba con ?opec=1). El resto de la página de diagnóstico de correo y ebook queda igual.
POR QUE: el bloque vencía el 10 de nov de 2026 y ya cumplió su función; dejarlo era código abierto sin uso.
COMO SE HIZO: se borraron las 38 líneas del bloque (líneas 2 a 39), se verificó sintaxis con php -l y se reconstruyó php.pak firmado (CP1); los otros 18 archivos no cambiaron.
QUE FALTA: borrar a mano en el hosting, si existen, la carpeta ce_data/opec/ y el archivo opec-*.json.gz de la raíz (el servidor solo actualiza archivos existentes y no los borra).

## 10 nov 2026 - sitio.pak (noticias: DIAN post-prueba, enlace a Noticias en la portada y en el menú del celular)
QUE SE HIZO: (1) la noticia de la DIAN pasa de "hoy se aplica la prueba escrita" a "ya se presentó la prueba escrita, ahora vienen los resultados" (artículo, tarjeta principal de /guias/noticias-concursos, metadatos, fecha 10 nov y sitemap; se mantiene la URL ...-8-noviembre). (2) El aviso de la portada y de /dian dice "Ya se presentó la prueba escrita del concurso DIAN 2676" y conserva el enlace a Noticias. (3) Se agrega "Noticias" al menú lateral del celular (Más > Sitio) en las 901 páginas.
POR QUE: la portada seguía diciendo "Hoy se aplica" y el enlace a Noticias no se veía: el script de cuenta regresiva reescribía el texto del aviso al llegar la fecha y borraba el enlace; el enlace del menú superior se oculta bajo 1340 px y el menú del celular no lo tenía.
COMO SE HIZO: reemplazos exactos de texto; se quitó del script del aviso la línea que reescribía el título y el texto; ancla nueva en el menú lateral (ce-mnav-js). Verificado con Chrome a 360 y 1200 px; auditoría: menú superior, lateral y barra inferior idénticos en las 901 páginas.
QUE FALTA: el enlace Noticias del menú superior sigue oculto bajo 1340 px (decidir si se reubica); actualizar la noticia de Procuraduría el 11 nov con la decisión sobre reclamaciones; pagar.html sin barra inferior.

## 10 nov 2026 - cartilla.enc (precios del panel de administración: +$5.000 y Abogados $99.000)
QUE SE HIZO: en el panel de administración de la cartilla se actualizaron 92 precios de los mensajes de venta, las respuestas del bot, los guiones y la tabla de precios del embudo (NIVP/PRECIO) al esquema +$5.000 (DIAN y CAR: $40.000, $45.000, $50.000; Procuraduría: hasta $55.000 asesor y ejecutivo; Docente: $40.000, $45.000, $50.000, $55.000; "desde $40.000"; combo "ambos" $80.000; precio por defecto del cuadro financiero $45.000). Abogados · Examen de Estado pasa a $99.000 en todos sus listados.
POR QUE: Claudia encontró precios viejos dentro de la cartilla; el servidor ya cobraba con +$5.000 desde el 9 de nov pero estos textos seguían con los valores anteriores. Abogados se cobrará a $99.000 por decisión de Claudia.
COMO SE HIZO: se descifró la cartilla.enc publicada (commit 87e562c), se cambiaron solo los textos de precio en la región del administrador y se volvió a cifrar y firmar (CE1); se verificó que lo demás es idéntico byte por byte y que no queda ningún $35.000 en esos mensajes.
QUE FALTA: los mensajes dicen "simulacro gratis de 30 preguntas" y el de DIAN ya es de 50; si Abogados se vende con Wompi, el valor del producto en wompi.php (que se sube a mano) debe cambiarse a 99000.

## 10 nov 2026 - php.pak (Abogados $99.000 en el embudo)
QUE SE HIZO: en acceso/lib.php el precio de 'abog' en crm_precio pasa de 50000 a 99000; los otros 18 archivos no cambian.
POR QUE: el curso de Abogados se cobrará a $99.000 y el embudo debe sugerir ese valor.
COMO SE HIZO: se reconstruyó php.pak firmado (CP1) a partir del publicado, con ese único cambio.
QUE FALTA: nada de este cambio.

## 10 nov 2026 - sitio.pak (celular sin desbordes, Abogados $99.000 y hoja de vida oculta)
QUE SE HIZO: (1) en 913 páginas se agrega un bloque de estilos para celular (id ce-mob2): el texto largo ya no ensancha la página, las tablas llevan su propio desplazamiento, casillas de 24 px con zona táctil de 44 px, enlaces del pie tocables, letras de 13 px como mínimo y aviso de cookies más compacto; se corrige el desborde de pagar.html a 320-360 px y de procuraduria.html a 320 px. (2) La página del curso de Abogados cambia de $50.000 a $99.000 (6 menciones). (3) /evalua-hoja-de-vida pasa a noindex,nofollow y sale del sitemap.
POR QUE: pagar.html y procuraduria.html se desbordaban de lado en celulares angostos; Claudia pidió el precio de Abogados en $99.000 y que "Evalúa tu hoja de vida" siga escondida (seguía con index,follow y en el sitemap).
COMO SE HIZO: se partió del sitio.pak publicado (commit 87e562c), se revisaron 66 páginas de todas las carpetas a 320, 360 y 390 px y se reconstruyó sitio.pak firmado (CS1).
QUE FALTA: evalua-hoja-de-vida.html (oculta, en pruebas) todavía sobra 21 px a 320 px por el campo de subir archivo; pagar.html sigue sin barra inferior; quedan 3 frases en "usted" en la portada y el método.

## 10 nov 2026 - sitio.pak (Docentes: pestañas de la página con el texto cortado)
QUE SE HIZO: en concursos/docentes.html las 9 pestañas (Resumen, Vacantes, Fases, Ponderación, Ley 2418, Requisitos, Antecedentes, Entrevista, Tips) ya no se cortan: la rejilla .dp-tabs pasa de filas fijas de 56 px a filas automáticas y cada botón ocupa el alto de su fila.
POR QUE: Claudia vio que el subtítulo ("Lo esencial", "Paso a paso"…) quedaba tapado por la fila siguiente; las filas fijas de 56 px eran de la versión anterior y los botones actuales llevan subtítulo y la marca "Estás aquí" (hasta 114 px).
COMO SE HIZO: bloque de estilos id ce-dptabs al final del head de esa página; se verificó a 1327 y 390 px (ningún botón con texto cortado ni desborde) y se reconstruyó sitio.pak firmado (CS1) a partir del publicado en el commit anterior.
QUE FALTA: nada de este cambio; el error ya estaba publicado antes de los cambios de celular de hoy, no vino de ellos.

## 10 nov 2026 - sitio.pak (Docentes: fechas confirmadas por la CNSC y enlace al simulador oficial)
QUE SE HIZO: (1) en concursos/docentes.html y concursos/docentes-fechas.html la inscripción de las vacantes reservadas a personas con discapacidad pasa de "tercera semana de noviembre y diciembre" a "del 23 de noviembre de 2026 al 15 de enero de 2027" (Resolución 11673 del 6 de noviembre de 2026), en la fase Inscripciones, el cronograma, la lista de inscripciones y las preguntas frecuentes (incluido el dato estructurado). (2) Aviso "Fecha confirmada por la CNSC" arriba de las pestañas y del cronograma. (3) Cuadro en la pestaña Ley 2418 con las fechas, la gratuidad con certificado y las jornadas de acompañamiento por el sismo del 10 de agosto de 2026. (4) Cuadro "Simulador oficial de la CNSC" (publicado el 9 de noviembre) con enlace, aclarando que es orientativo, y recordando lo nuestro: la pestaña Ponderación y el simulacro gratis de 30 preguntas. (5) "Actualizado" de la página de fechas y lastmod del sitemap pasan al 10 de noviembre.
POR QUE: Claudia pidió revisar la página de la CNSC y mejorar Docentes con lo nuevo: la Resolución 11673 fijó las fechas que estaban como preliminares y la CNSC lanzó un simulador oficial de empleos, antecedentes y escalafón que conviene enlazar en vez de competir con él.
COMO SE HIZO: se revisó la página de la CNSC en el navegador (avisos, normatividad y las 5 pestañas del simulador); se partió del sitio.pak publicado (commit 6b98a3d), se cambiaron solo esos dos archivos y el sitemap con reemplazos exactos verificados, se revisó a 1280 y 390 px (sin desborde) y se reconstruyó sitio.pak firmado (CS1).
QUE FALTA: las inscripciones sin reserva (febrero de 2027) y las pruebas (octubre de 2027) siguen preliminares: actualizar cuando la CNSC publique el acuerdo con fechas. No se tocó el resto del sitio.

## 10 nov 2026 - cartilla.enc (precios viejos en las páginas gratis del panel)
QUE SE HIZO: en las 5 páginas gratis que se sirven dentro del panel (Curso: derecho de petición y los simulacros gratis de DIAN, Procuraduría, CAR y Docentes) se cambian 12 textos de precio de $35.000 a $40.000: "desde $35.000 según tu cargo" (aviso de pago en línea), "Pago único desde $35.000 según tu nivel" y el cuadro "¿Quieres la cartilla de tu cargo?" (DIAN cuesta, Procuraduría desde, CAR desde).
POR QUE: Claudia vio en el celular, dentro del curso de derecho de petición, el cuadro con $35.000 cuando el precio desde el 9 de noviembre es $40.000. La corrección anterior de cartilla.enc solo cubrió los mensajes del administrador; estas páginas viven en bloques aparte (x-fp) dentro de la cartilla.
COMO SE HIZO: se descifró la cartilla publicada (commit anterior), se decodificó cada bloque fp-*, se reemplazó $35.000 solo donde el contexto era de precio (comprobado con una regla que falla si no lo es) y se volvió a codificar; se re-cifró cartilla.enc y se verificó firma, descifrado idéntico y que todo lo que está fuera de esos bloques es idéntico byte a byte.
QUE FALTA: el cuadro dice "DIAN cuesta $40.000" aunque DIAN va de $40.000 a $50.000 según el nivel; conviene cambiarlo a "desde $40.000" en una próxima revisión de textos.

## 10 nov 2026 - sitio.pak (Docentes en celular: al tocar una pestaña el contenido ahora queda a la vista)
QUE SE HIZO: en concursos/docentes.html la función que cambia de pestaña (show) ahora, en pantallas de hasta 900 px, lleva la pantalla al comienzo del contenido de la pestaña elegida, justo debajo del encabezado fijo. En computador no cambia nada.
POR QUE: Claudia vio en el celular que al tocar una de las 9 pestañas la página la mandaba hacia arriba en vez de hacia abajo, donde está el contenido. La función llevaba la pantalla al comienzo de todo el bloque (aviso, guía y pestañas), que en el celular es muy alto, y el contenido queda mucho más abajo.
COMO SE HIZO: se partió del sitio.pak publicado, se cambió esa línea con un reemplazo exacto y se probó con navegador a 390 px: antes, el contenido de la pestaña quedaba fuera de la pantalla; ahora queda a 73 px del borde de arriba (justo bajo el encabezado) tanto con "Ponderación" como con "Tips"; los botones "Siguiente" y "Anterior" usan la misma función. Se reconstruyó sitio.pak firmado (CS1).
QUE FALTA: probar en un celular real (Android y iPhone); en computador el contenido de la pestaña queda cerca del borde de abajo de la pantalla, se puede subir en otra revisión.

## 10 nov 2026 - sitio.pak (Docentes en computador: al tocar una pestaña se ve su contenido)
QUE SE HIZO: en concursos/docentes.html la función de cambio de pestaña (show) ahora lleva la pantalla al comienzo del contenido de la pestaña elegida, bajo el encabezado fijo, también en computador (antes solo en celular).
POR QUE: Claudia vio que en computador pasaba lo mismo que en celular: al tocar una pestaña la página la mandaba hacia arriba, al aviso y la guía, y el contenido quedaba casi fuera de la pantalla.
COMO SE HIZO: se partió del sitio.pak publicado (commit 2fb06d0) y se quitó la condición de ancho de pantalla de esa función con un reemplazo exacto. Se probó con navegador a 1280 y 390 px: el contenido de la pestaña queda a unos 73 a 78 px del borde de arriba, justo bajo el encabezado. Se reconstruyó sitio.pak firmado (CS1).
QUE FALTA: al saltar al contenido las pestañas quedan arriba; se navega con "Anterior" y "Siguiente" del final de cada tema o subiendo. Si se prefiere ver siempre las pestañas, hacerlas pegajosas (sticky).

## 10 nov 2026 - sitio.pak (noticias: Docentes, DIAN y CAR con datos oficiales de la CNSC)
QUE SE HIZO: (1) Docentes: en la noticia del concurso se agregó "El tamaño del concurso": 31.163 vacantes en 89 entidades territoriales certificadas. (2) DIAN: en la noticia de la prueba escrita del 8 de noviembre se agregaron 218.051 citados, 300 instituciones, 51 ciudades y cerca de 2.700 aspirantes con discapacidad con ajustes razonables. (3) CAR: la noticia y su tarjeta dejan de decir "aplazadas hasta el 31 de diciembre" y pasan a decir que la compra de derechos y las inscripciones siguen aplazadas mientras rigen las medidas del Decreto Legislativo 1384 de 2026 (Resolución 10567 del 16 de septiembre de 2026); oferta oficial de 1.383 empleos y 1.832 vacantes, con la CDMB incorporada. La dirección de la noticia no cambió.
POR QUE: Claudia pidió revisar las noticias de los concursos (DIAN, Procuraduría, Docentes y CAR) con fuentes oficiales. La CNSC no fija el 31 de diciembre como fecha de inscripción; condiciona el aplazamiento al levantamiento de las medidas del sismo.
COMO SE HIZO: solo cnsc.gov.co como fuente (no se usó competencia); se partió del sitio.pak publicado, se cambiaron 4 archivos con reemplazos exactos y se reconstruyó sitio.pak firmado (CS1); se verificó firma y que solo esos 4 archivos difieren (973 entradas).
QUE FALTA: Procuraduría: no hubo dato oficial nuevo; revisar el 11 de nov por la decisión de reclamaciones. CAR: actualizar cuando la CNSC publique nueva fecha de inscripciones. Resultados de Valoración de Antecedentes de EON y CORPOMOJANA (12 de nov).

## 10 nov 2026 - sitio.pak (CAR: se corrige la noticia, Corponor sí informó el 31 de diciembre)
QUE SE HIZO: la noticia de CAR y su tarjeta vuelven a mencionar el 31 de diciembre de 2026, atribuido a Corponor (16 de octubre), junto con la Resolución 10567 de la CNSC y el Decreto Legislativo 1384; se aclara que la CNSC aún no anuncia la nueva fecha de inscripciones. Cifra: 1.832 vacantes en 33 corporaciones.
POR QUE: en el cambio anterior se dijo que la CNSC no fijaba el 31 de diciembre; Corponor, entidad oficial, sí lo publicó, así que había que presentar ambas fuentes.
COMO SE HIZO: reemplazos exactos sobre el sitio.pak publicado, firma verificada.
QUE FALTA: no se halló noticia de CAR fechada hoy; revisar mañana.

## 10 nov 2026 - sitio.pak (CAR: fecha de la noticia)
QUE SE HIZO: la tarjeta y la noticia de CAR pasan de "8 de noviembre" a "10 de noviembre de 2026" (fecha visible, datePublished/dateModified y lastmod del sitemap).
POR QUE: Claudia vio que la tarjeta seguía con la fecha vieja aunque el contenido se actualizó el 10.
COMO SE HIZO: reemplazos exactos sobre el sitio.pak publicado; firma verificada.
QUE FALTA: la portada mostraba aún el texto anterior de la tarjeta; debería actualizarse sola al llegar este pak (~10 min); si no, revisar de dónde lee la portada.

## 10 nov 2026 - sitio.pak (página de noticias con formato de portada de medio)
QUE SE HIZO: guias/noticias-concursos.html: cada noticia lleva una ilustración (degradado con los colores de la entidad y la palabra del concurso en grande); la noticia principal queda junto al bloque "Para no perderte" (4 enlaces); banner "Estudia lo que te toca a tu cargo" (cartillas interactivas, simulacro gratis de 30 preguntas) arriba y abajo de "Últimas noticias". No se mencionó el tutor con IA.
POR QUE: Claudia pidió que las noticias se vean como la portada de TBN. Se aprobó la maqueta y dijo "publica".
COMO SE HIZO: se partió del sitio.pak publicado; se añadió un bloque de estilos nuevo (npcss2) y marcas HTML con reemplazos exactos; se probó a 1280 y 390 px sin desborde; pak firmado (CS1); solo cambió ese archivo.
QUE FALTA: las ilustraciones son provisionales (degradados); las propias de cada noticia se crean al publicar cada noticia nueva. Las páginas de cada noticia (guias/noticia-*.html) aún no llevan ilustración.

## 10 nov 2026 - sitio.pak (textos de la página en tuteo: Docentes, inicio, DIAN, Procuraduría y CAR)
QUE SE HIZO: se cambiaron a tuteo 52 apariciones de 23 frases distintas con "usted" en 7 páginas públicas (index, procuraduria, dian, concursos/docentes, concursos/corporaciones-autonomas-regionales, guias/estudiar-por-cargo, guias/index). Ejemplos: "Consulte su cargo y verifique su cartilla" pasa a "Consulta tu cargo y verifica tu cartilla"; "Seleccione cada etapa" a "Selecciona cada etapa"; "Elija su concurso y busque su cargo" a "Elige tu concurso y busca tu cargo"; "Ajustada a su empleo" a "Ajustada a tu empleo"; en el simulacro de Docentes, "La cartilla completa le permite..." a "te permite...".
POR QUE: la regla es tuteo en todo el marketing, y en la revisión del sitio quedaban estas frases pendientes (CAMBIOS.md anterior, "QUE FALTA").
COMO SE HIZO: reemplazos de frases exactas, partiendo del sitio.pak publicado más reciente (commit de80187, que incluye los cambios de noticias de la otra sesión); se comprobó que solo cambian esos 7 archivos, que el número de etiquetas div no varía y que ya no queda ninguna de las frases viejas; se reconstruyó sitio.pak firmado (CS1).
QUE FALTA: no se tocaron las funciones citadas del Manual (por ejemplo "personal a su cargo"), que son texto oficial, ni la política de privacidad (documento legal en tono formal), ni las páginas de cada cargo (carpeta cargos), que tienen su propio texto. Si se quiere tuteo también en la política de privacidad, decidirlo aparte.

## 11 nov 2026 — Términos: vigencia de cada pago y de la promoción
- Términos de uso (terminos.html): se aclara el "desde" y el "hasta" del acceso de cada pago (desde que se confirma el pago o se activa el código hasta 30 días después de la prueba escrita; la fecha exacta sigue en "Vigencia" de la cuenta).
- Nueva cláusula en la sección 7: los valores publicados son de promoción y rigen hasta el 20 de noviembre de 2026, inclusive; los pagos aprobados en ese plazo conservan valor y vigencia; después los valores pueden cambiar. Fecha de actualización: 11 de noviembre de 2026.
- Qué falta: si el 20 de noviembre se mantiene o cambia el precio, actualizar esta cláusula, las páginas con precios y pagar.html. Para volver atrás: revertir este commit.

## 12 nov 2026 — Email marketing: subir imagen y programar envíos
- Subir imagen: en el formulario de Email marketing hay un campo «Subir imagen» (JPG o PNG). El navegador la reduce a máximo 1.200 px de ancho; el servidor valida que sea una imagen real (máximo 1,5 MB, 60 imágenes) y la guarda en ce_data/imagenes (no se borra al actualizar el sitio). Aparece en el desplegable «Imagen del correo» como «📤 nombre» y se ve en la vista previa y en el envío. Se sirve por acceso/api.php?a=imgc&f=up-<16 hex>.png|jpg.
- Programar envío: nuevo campo «Programar envío para (hora de Colombia)», botón «⏰ Programar envío a N» y botón «📅 Programados» (ver avance y cancelar). El servidor guarda el envío en ce_data/programados.json y lo manda por tandas de 40 en cada revisión, respetando bajas, mercadeo (si es comercial), límite diario y el horario de la Ley 2300 (un comercial fuera de horario se rechaza al programar y no sale hasta que esté en horario). Si el correo falla 3 veces seguidas el envío se detiene con estado «error».
- Quién revisa los envíos (sin crear nada): (1) la tarea cron que ya existe y corre acceso/actualizar.php: al terminar, lib.php corre los envíos vencidos (deja una línea «Programados» en ce_data/update.log); (2) respaldo por visitas: si hay un envío vencido y la última revisión fue hace más de 4 minutos, una visita al sitio lo corre después de responder; (3) opcional, más puntual: una tarea cron cada 5 minutos con curl a acceso/api.php?a=prog&t=TOKEN (el TOKEN y la línea se ven en «Programados»).
- Importante para quien mantenga esto: actualizar.php solo instala los archivos PHP de una lista fija (suscribir, baja, confirmar, descargar, diagnostico, prueba-correo, _suscripcion, _correo, acceso/api|lib|chat|chat_core|whatsapp|index, admin/index). Por eso NO se crearon archivos nuevos: todo vive en acceso/lib.php y acceso/api.php.
- Archivos: acceso/lib.php (cm_img_ok, cm_img_subir, cm_prog_*, 4 operaciones nuevas, ganchos), acceso/api.php (operaciones, rutas a=imgc y a=prog, out() capturable, gancho de visita) y cartilla.enc (formulario).
- Qué falta: probar un envío programado real a info@concursosdelestado.com; editar un envío ya programado (hoy solo se cancela y se vuelve a crear).
- Para volver atrás: revertir este commit.

## 12 nov 2026 — SEO de los 380 cargos de Procuraduría: títulos, descripciones y enlaces entre cargos
- QUE SE HIZO: en las 380 páginas de cargos/procuraduria/ (excepto el índice) se unificó el título, la descripción (meta y Open Graph) y se agregó el bloque «Cartillas de cargos parecidos» (hasta 6 enlaces) dentro de «Sigue estudiando».
- POR QUE: Search Console (16 oct–10 nov) mostró que casi todo el tráfico es de DIAN, concurso que ya se presentó (8 nov), y que la mayoría de las 207 páginas sin indexar son «Descubierta: actualmente sin indexar» (165): Google las conoce pero no las rastrea. Los títulos de Procuraduría tenían tres formatos distintos y 126 pasaban de 70 caracteres, a veces cortados a mitad de palabra («Donde se», «Relatoría»); 282 descripciones pasaban de 160.
- COMO SE HIZO: título «{Cargo} {CÓDIGO} Procuraduría · Conv. {n}» (la convocatoria hace único cada título; si aun así se repite se agrega la dependencia). Descripción de máximo 160 caracteres con cargo, código, convocatoria, ejes y lecciones y «Prueba 10 preguntas gratis». Enlaces entre cargos: primero hasta 4 del mismo cargo (otras dependencias) y luego del mismo tipo de empleo, repartidos para que casi todas reciban enlaces entrantes (379 de 380). Script: /tmp/cce/seo/seo2.py (no queda en el repo).
- QUE FALTA: pedir en Search Console la indexación de las páginas más importantes; revisar en 2 a 4 semanas si baja el número de «Descubierta: sin indexar»; decidir si las guías de simulacro (hoy noindex a propósito) pueden indexarse; marcar DIAN como «concurso presentado». Para volver atrás: revertir este commit.

## 12 nov 2026 · Portada centrada en Procuraduría
**QUE SE HIZO:** La portada dejó de girar alrededor de DIAN. Se quitó la franja "Ya se presentó DIAN 2676" y se puso una de Procuraduría (fechas 17, 20, 27 y 30 de nov). Se agregó la sección #procuraduria con los 4 niveles y precios. Se reordenó el orden de los concursos (Procuraduría, CAR, Docentes, DIAN) en título, descripción, buscador, cifras y textos. El ejemplo del tutorial usa cargos de Procuraduría.
**POR QUE:** La prueba de DIAN fue el 8 de nov y la demanda ahora está en Procuraduría.
**COMO SE HIZO:** Edición de index.html dentro de sitio.pak (script /tmp/cce/home).
**QUE FALTA:** Revisar las páginas internas con textos de DIAN (guías, /concursos) y el contenido que sale en el buscador por defecto.

## 12 nov 2026 · Portada: marca en el título y menú
**QUE SE HIZO:** El título de la portada ahora empieza con "Concursos del Estado:" (también og:title). El menú "Guías" lleva a /guias/ (página real) en vez del ancla. En el desplegable de Concursos, DIAN pasó al final de los que tienen cartilla.
**POR QUE:** Ayudar a que Google muestre subpáginas (enlaces de sitio) al buscar la marca, y que DIAN no sea lo primero.
**COMO SE HIZO:** Edición de index.html en sitio.pak.
**QUE FALTA:** Los enlaces de sitio los decide Google; pueden tardar semanas. Más búsquedas del nombre de la marca ayudan.

## 13 nov 2026 - cartilla.enc (copias comprimidas al día en todos los concursos, 63 preguntas por función en Docentes y 3 textos)
QUE SE HIZO: (1) Se regeneraron las seis copias comprimidas (br-dian, br-pgn, br-car, br-doc, br-dcar, br-ddoc) a partir de su fuente y se corrigió el marcador CE-PUB (decía 23278004; la posición real era 33218287; ahora 33283598). (2) Docentes: 63 preguntas nuevas, una por cada función del manual (Res. MEN 3842 de 2022) que no tenía práctica: fun-aula 20, esp-fpre 1, esp-fare 1, fun-ori 9, esp-frec 19, esp-fcoo 13. Casos con enunciado largo, 3 opciones de largo parejo, respuesta repartida (22/20/21), explicación con la función citada al pie de la letra y etiqueta «Nuevo»; van al final de cada capítulo. Total de preguntas: 908 a 971. (3) Motor de Docentes: «Tu avance se guarda en tu cuenta», fecha de inscripción de la Resolución 11673 (23 nov 2026 a 15 ene 2027, vacantes reservadas a discapacidad) y se quitó la mención al módulo «Aptitudes», que no existe.
POR QUE: Claudia pidió un análisis completo de Docentes frente a Procuraduría y completar según los manuales de funciones. Al revisar se encontró que el servidor entrega a los clientes (no a la administradora) la copia Brotli de cada módulo y esas copias estaban sin regenerar desde cerca del 4 de noviembre: a los clientes de Docentes no les llegaban los capítulos etica, psico y evaprend, las 30 preguntas de matemáticas, los videos ni las figuras; a DIAN y Procuraduría no les llegaban las correcciones del 7 de noviembre. Aprobó con «publica».
COMO SE HIZO: git pull, se descifró el cartilla.enc publicado (commit 06b46f3) y se comprobó que era la base; DOCDATA se reserializó con comprobación de ida y vuelta; las funciones se tomaron del texto de la resolución (Drive, carpeta CONCURSO DOCENTE); cada copia Brotli se verificó descomprimiéndola contra su fuente; prueba en Chrome a 400 px con rector, coordinador, orientador, matemáticas y preescolar, sin errores ni desbordes.
QUE FALTA: REGLA PARA TODA EDICION DE cartilla.enc: después de cambiar s-dian, s-pgn, s-car, s-doc, d-car o d-doc hay que regenerar su copia br-* y recalcular CE-PUB, o el cambio no llega a los clientes. Los datos de Docentes pesan 6,8 MB comprimidos por los videos. Pendiente por tandas (ver documento «Análisis cartilla Docentes»): ampliar funciones de orientador, coordinador y director rural; preguntas para los 15 capítulos que no tienen; simulacro en casos de 3 preguntas; Mi cargo numerado, Plazos, glosario y quiz por lección; fusionar 182 lecciones cortas; áreas delgadas. DIAN y Procuraduría aún dicen «Tu avance se guarda en el navegador donde estudies».

## 13 nov 2026 - cartilla.enc (Docentes, tanda 2: 9 lecciones nuevas para orientador, coordinador, director rural y directivos, y 8 preguntas)
QUE SE HIZO: lecciones nuevas al final de cada capítulo, con etiqueta «Nuevo»: fun-ori 3 (plan operativo anual; ruta de atención y reserva; límites del cargo), esp-fcoo 2 (coordinar lo académico; coordinar la convivencia), esp-dru 2 (requisitos frente al rector; las 24 funciones en una escuela pequeña) más 8 preguntas de caso de 3 opciones (el capítulo no tenía ninguna), fd-ga 1 (dirigir lo académico con evidencias) y fd-gad 1 (Fondo de Servicios Educativos, asignación académica y evaluación de desempeño). Lecciones: 451 a 460. Preguntas: 971 a 979.
POR QUE: el análisis del 13 de noviembre mostró que las funciones del orientador, del coordinador y del director rural estaban explicadas en unas 650 caracteres cada una y que la gestión académica y administrativa del directivo eran los capítulos más delgados. Claudia pidió seguir y aprobó con «publica»; pidió dejar por ahora las preguntas antiguas con 4 opciones.
COMO SE HIZO: sobre el cartilla.enc publicado (commit f56fdf5). Las citas del manual se validan contra el texto de la Res. MEN 3842 de 2022 (falla si el fragmento no está); las de leyes y decretos se reutilizan de las citas ya verificadas dentro de la cartilla, sin escribir ninguna de memoria. Tablas con ancho ajustado al celular. Se regeneró br-ddoc, se comprobaron las otras cinco copias contra su fuente y se recalculó CE-PUB (33335140). Se comprobó que todo lo que está fuera de los datos de Docentes es idéntico a lo publicado. Prueba en Chrome a 400 px con orientador, coordinador, director rural y rector, sin errores ni desbordes.
QUE FALTA: tanda 3, preguntas para los 14 capítulos que aún no tienen (prueba, ant-aula, ant-ori, ant-dir, manual, man-pri, man-sec, man-ori, man-dir, man-areas, esp-pre, esp-prim, esp-rec, esp-coo). Luego: simulacro en casos de 3 preguntas, Mi cargo numerado, Plazos, glosario y quiz por lección, fusionar lecciones cortas (requiere decisión de Claudia) y áreas delgadas.

## 13 nov 2026 - cartilla.enc (Docentes, tanda 3: 32 preguntas para «Tu cargo» de rector, coordinador, preescolar y primaria)
QUE SE HIZO: 8 preguntas de caso en cada capítulo esp-rec, esp-coo, esp-pre y esp-prim, que no tenían ninguna. Tres opciones de largo parejo, respuesta repartida (11/11/10), norma en la explicación y etiqueta «Nuevo». Preguntas: 979 a 1.011.
POR QUE: el análisis del 13 de noviembre encontró 15 capítulos sin preguntas; estos cuatro son contenido del cargo. Claudia aprobó con «publica».
COMO SE HIZO: sobre el cartilla.enc publicado (commit bff93cc); las preguntas salen solo de lo verificado en las lecciones de cada capítulo (Ley 715 art. 10, Decreto 1075, Decreto 1850 compilado, Ley 115 arts. 15, 16 y 21, Decreto 1421). Se regeneró br-ddoc, se comprobaron las otras cinco copias y se recalculó CE-PUB. Prueba en Chrome a 400 px con los cuatro cargos, sin errores.
QUE FALTA: ver la entrada siguiente.

## 13 nov 2026 - cartilla.enc (Docentes, tanda 4: 8 preguntas para el capítulo del manual de funciones)
QUE SE HIZO: 8 preguntas de caso en «El manual de funciones: competencias que se evalúan» (id manual): áreas de gestión del docente y del directivo, límites a la asignación de funciones (num. 3.7), perfil de la media técnica (3.5), el manual como referencia de la evaluación (3.6) y lo que acredita el profesional no licenciado (3.8). Cada explicación cita el manual al pie de la letra, validada contra el texto de la Res. MEN 3842 de 2022. Preguntas: 1.011 a 1.019.
POR QUE: capítulo sin preguntas; Claudia aprobó con «publica».
COMO SE HIZO: sobre la tanda 3 recién publicada; br-ddoc regenerada, otras copias comprobadas, CE-PUB recalculado; prueba a 400 px sin errores.
QUE FALTA: NO se pusieron preguntas en «Sobre el concurso» ni en los tres capítulos de antecedentes, porque el simulacro de Docentes toma preguntas de todos los capítulos del cargo y la regla de Claudia es que el simulacro sea solo de funciones y misionalidad. Tampoco en los cinco «Manual» por cargo y por área (repiten funciones ya cubiertas o son títulos habilitantes). Siguiente tanda aprobada: reforzar áreas delgadas (música, danzas, artes escénicas, artes plásticas y luego tecnología, educación física, filosofía y religión).

## 13 nov 2026 - cartilla.enc (Docentes, tanda 5: educación artística, 2 lecciones y 32 preguntas)
QUE SE HIZO: 2 lecciones nuevas en esp-art («Las tres competencias del área, en palabras del Ministerio»; «Espectador, creador y expositor: los procesos del aula y cómo se evalúan») y 32 preguntas de caso (esp-art 8, esp-mus 6, esp-dan 6, esp-esc 6, esp-pla 6), con etiqueta «Nuevo» al final de cada capítulo. Lecciones 460 a 462; preguntas 1.019 a 1.051.
POR QUE: eran las áreas más delgadas del concurso; Claudia pidió seguir con áreas y aprobó con «publica».
COMO SE HIZO: sobre el cartilla.enc publicado (commit f1fba02). Citas tomadas del Documento 16 del MEN (Orientaciones pedagógicas para la educación artística) y comprobadas contra el texto del PDF, con página verificada. Se regeneró br-ddoc, se comprobaron las otras copias y se recalculó CE-PUB (33401096). Fuera de los datos de Docentes todo es idéntico a lo publicado. Prueba a 400 px con los tres cargos, sin errores.
QUE FALTA: ver la entrada siguiente. REGLA: tras editar d-doc/s-doc hay que regenerar br-* y recalcular CE-PUB.

## 13 nov 2026 - cartilla.enc (Docentes, tanda 6: educación física, filosofía y tecnología, 3 lecciones y 18 preguntas)
QUE SE HIZO: una lección y 6 preguntas de caso en cada capítulo esp-efi (tres competencias, Doc. 15 MEN), esp-fil (crítica, dialógica y creativa, Doc. 14 MEN) y esp-tec (cuatro componentes, Guía 30 MEN), con etiqueta «Nuevo». Fuentes de efi y tec ampliadas. Lecciones 462 a 465; preguntas 1.051 a 1.069.
POR QUE: seguir reforzando áreas delgadas; Claudia aprobó con «publica».
COMO SE HIZO: sobre la tanda 5 recién publicada. Citas comprobadas contra el texto de los PDF del MEN (sin número de página, no se verificó la paginación impresa). br-ddoc regenerada, CE-PUB 33428367. Prueba a 400 px sin errores.
INSTRUCCIONES PARA OTRA IA: tras editar d-doc/s-doc regenerar br-* y recalcular CE-PUB; contenido nuevo con etiqueta «Nuevo» al final del capítulo; no mover el orden de lecciones/preguntas existentes (rompe el avance guardado).
QUE FALTA: religión (esp-rel): conseguir Decreto 4500 de 2006 y Ley 133 de 1994 oficiales antes de escribir. Luego: simulacro en casos de 3 preguntas, Mi cargo numerado, Plazos, glosario y quiz por lección, fusión de lecciones cortas (decide Claudia), preguntas antiguas de 4 a 3 opciones (por ahora se dejan).

## 13 nov 2026 - cartilla.enc (Docentes, tanda 7: educación religiosa, 1 lección y 8 preguntas)
QUE SE HIZO: lección nueva «El Decreto 4500 de 2006, artículo por artículo» (arts. 2 a 8 con cita textual, tabla para ubicar el artículo y clave de examen) y 8 preguntas de caso de 3 opciones en esp-rel, con etiqueta «Nuevo». Decreto 4500 agregado a las fuentes del capítulo. Lecciones 465 a 466; preguntas 1.069 a 1.077.
POR QUE: religión era el último área delgada de la lista; Claudia aprobó con «publica».
COMO SE HIZO: sobre la tanda 6 publicada. Citas validadas contra el PDF oficial del Decreto 4500 bajado de mineducacion.gov.co (falla si el fragmento no está). br-ddoc regenerada, CE-PUB 33440978; resto idéntico. Prueba a 400 px sin errores.
INSTRUCCIONES PARA OTRA IA: tras editar d-doc/s-doc regenerar br-* y recalcular CE-PUB; contenido nuevo con etiqueta «Nuevo» al final del capítulo; no reordenar lo existente (rompe el avance guardado); no citar normas de memoria.
QUE FALTA: no hay citas de la Ley 133 de 1994 (no se pudo abrir el texto oficial; agregar cuando haya PDF o enlace). El archivo del decreto trae el pie con fecha en blanco: no se contrastó con el Diario Oficial. Pendiente: simulacro en casos de 3 preguntas, Mi cargo numerado, Plazos, glosario y quiz por lección, fusión de lecciones cortas (decide Claudia), preguntas antiguas de 4 a 3 opciones.

## 13 nov 2026 - cartilla.enc (Docentes, tanda 8: simulacro en casos de 3 preguntas; cambia el motor s-doc)
QUE SE HIZO: (1) Datos: 13 casos con 3 preguntas cada uno (39 preguntas, etiqueta «Nuevo»): fun-aula 4 casos, fun-ori 3, esp-frec 3, esp-fcoo 3. Cada pregunta lleva el campo `caso` con el mismo texto del caso; las 3 preguntas de un caso se reconocen porque comparten ese texto. Preguntas 1.077 a 1.116. (2) Motor s-doc, cuatro cambios: el simulacro con cronómetro agrupa las preguntas por `caso`, pone primero los casos completos (en orden al azar) y luego completa con preguntas sueltas; la práctica por capítulo baraja por casos sin partirlos; el recuadro dice «Caso · pregunta k de 3»; las preguntas con `caso` no entran a las fichas de repaso; texto de la tarjeta del simulacro actualizado.
POR QUE: regla de Claudia: los simulacros de todos los concursos van en casos con 3 preguntas, solo de funciones y misionalidad, como DIAN. Aprobó con «publica».
COMO SE HIZO: sobre la tanda 7 publicada (3f19060). Cada explicación cita la función del manual (Res. MEN 3842 de 2022) validada contra el texto (falla si el fragmento no está). Opciones de largo parejo, respuesta repartida por igual entre A, B y C. Se regeneraron br-doc y br-ddoc, CE-PUB 33478243. Prueba a 400 px: simulacro de 15 con docente de aula, orientador, rector y coordinador; casos completos y en orden, sin errores ni desbordes.
INSTRUCCIONES PARA OTRA IA: para agregar un caso, añadir al final del capítulo 3 preguntas con el MISMO texto en `caso` (idéntico carácter por carácter) y `nuevo:true`; no intercalar otras preguntas entre ellas. Tras editar s-doc o d-doc regenerar br-doc/br-ddoc y recalcular CE-PUB. No reordenar preguntas existentes.
QUE FALTA: hay pocos casos por cargo (3 o 4): quien repite el simulacro ve los mismos; escribir más. Preescolar, primaria y director rural usan los casos generales (aula o rector), sin casos propios. Luego: Mi cargo numerado, Plazos, glosario y quiz por lección, fusión de lecciones cortas (decide Claudia), preguntas antiguas de 4 a 3 opciones, citas de la Ley 133 de 1994 en religión.

## 14 nov 2026 - cartilla.enc y sitio.pak (Docentes: título de derecho y pruebas de 10 preguntas)
QUE SE HIZO: (1) Cartilla Docentes: se quita que el título de derecho habilita docente de aula. Cambian 4 textos: Ciencias sociales y Ciencias económicas y políticas ("por medida cautelar del Consejo de Estado (inclusión provisional), derecho") y el ejemplo general de títulos por área, que ahora dicen que derecho ya no habilita docente de aula; y el caso del profesional no licenciado, que ya no cita al abogado. (2) Sitio: se quitan las menciones a la prueba de 10 preguntas: el bloque de la portada ahora dice «Empieza gratis» (cuenta gratis y simulacro), el botón del recorrido dice «Crear mi cuenta gratis» y lleva a #gratis, y la descripción de 322 páginas de cargos de la Procuraduría dice «Empieza gratis con un simulacro.».
POR QUE: simulador de la CNSC (9 nov 2026): desde la decisión del Consejo de Estado del 27 ago 2026, ejecutada el 13 oct, derecho no habilita docente de aula ni orientador (sí rector, coordinador y director rural). Y Ariel indicó que las pruebas de 10 preguntas ya no sirven.
COMO SE HIZO: sobre cartilla.enc y sitio.pak publicados. d-doc editado con 4 reemplazos exactos (aserciones de una sola coincidencia); br-ddoc regenerada (brotli 11, comprobada contra d-doc) y CE-PUB recalculado (33367319, apunta a pub-data); las otras cinco copias br-* sin cambio. Descifrado de ida y vuelta verificado, firma del paquete verificada, carga en Chrome a 400 px sin errores (70 bloques de Docentes).
QUE FALTA: confirmar cuántas preguntas tiene el simulacro gratis de Procuraduría y CAR; la página /guias/prueba-el-metodo sigue publicada (revisar si se quita). Las preguntas de práctica de Docentes no se revisaron una a una.

## 14 nov 2026 - cartilla.enc (Docentes: 28 preguntas nuevas de razonamiento cuantitativo y lectura crítica)
QUE SE HIZO: «Razonamiento cuantitativo en el aula» pasa de 19 a 35 preguntas (+16) y «Lectura crítica en el contexto escolar» de 18 a 30 (+12). Cuantitativo: edades, fracciones del día, rendimiento de marcadores, proporción inversa, descuentos sucesivos, escala de un plano, probabilidad simple, mediana, asistencia promedio, conversión de unidades, porcentaje de porcentaje, presupuesto, horario de jornada, aumento y disminución, nota mínima necesaria y combinaciones. Lectura: ordenar frases, vocabulario en contexto, función del texto, inferencias válidas, tesis, lectura de tabla con variación porcentual, ambigüedad, ironía, razonamiento con premisas y conectores.
POR QUE: la prueba de aptitudes y competencias básicas pesa 55 % y es eliminatoria (mínimo 60 docentes y 70 directivos); evalúa lectura crítica y razonamiento cuantitativo, y esos dos capítulos eran los más delgados. El material de Drive «Material de estudio concurso docente MEN» (100 preguntas, 2021) se usó solo como referente de formato; ninguna pregunta se copió: son originales, con contextos de colegio.
COMO SE HIZO: sobre cartilla.enc publicado (commit 967b313). Cada resultado numérico se comprobó por código antes de escribir la explicación; opciones barajadas con semilla fija para repartir la respuesta correcta (0: 7, 1: 6, 2: 6, 3: 9). d-doc reserializado sin diferencias (comprobado: idéntico al original antes de agregar), br-ddoc regenerada y CE-PUB recalculado (33492971); otras cinco copias br-* sin cambio. Descifrado de ida y vuelta verificado y carga en Chrome a 400 px sin errores.
QUE FALTA: ninguna pregunta verifica norma, por diseño (son de la parte de aptitud). Pendiente: «competencias blandas» ya cubierta en «Ética y ciudadanía»; revisar las preguntas de práctica de los demás capítulos una a una.

## 14 nov 2026 - cartilla.enc (Docentes: capítulos reorganizados, de 70 a 41 bloques)
QUE SE HIZO: se fusionan 29 capítulos en sus afines, sin perder lecciones ni preguntas. Aptitudes (lectura crítica + razonamiento cuantitativo); Competencias comportamentales + ética y ciudadanía + psicotécnica y entrevista; Estatuto docente + sistema escolar (Ley 715) + evaluación de desempeño; Convivencia + inclusión + evaluar para aprender + talleres de casos; las tres gestiones (administrativa, comunitaria) dentro de la gestión académica del docente de aula y del orientador, y las cuatro del directivo en una; manual de secundaria + títulos por área; manual de orientador y de directivos + sus antecedentes; Ciencias naturales (física, química, biología y práctica) y Educación artística (música, danzas, escénicas, plásticas) en un solo capítulo; práctica de aula dentro de matemáticas, lengua e inglés. Docente de secundaria pasa de 47 a 12 capítulos aprox., primaria 11, orientador 9, directivo 9.
POR QUE: Ariel pidió que los capítulos que van juntos queden en uno solo.
COMO SE HIZO: en d-doc cada bloque absorbido se agrega al final del que sobrevive (mismo id), con prefijo en el título de cada lección y marca "mg"; se unen preguntas y fuentes. En la app (DOCAPP): listas NV, ESP y ORDER con los ids nuevos; build() calcula los índices y dmigr() migra el avance guardado (lecciones estudiadas, mejor puntaje por capítulo y "continuar") una sola vez por bloque (marca S.mig3); un enlace viejo #/c/<id absorbido> redirige al capítulo nuevo. br-ddoc regenerada y CE-PUB recalculado (33463583). Probado en Chromium a 400 px con los 5 niveles y 6 convocatorias: 0 errores y avance migrado bien.
QUE FALTA: pra-soc se queda aparte (la comparte primaria con secundaria). Si alguien tenía progreso con otra convocatoria distinta a la activa al abrir, esas lecciones no se migran.

## 14 nov 2026 - cartilla.enc (Docentes: casos más complejos, tanda 1)
QUE SE HIZO: 41 preguntas situacionales básicas se reescriben como casos completos (45 apariciones, porque varias estaban repetidas en fa-ga, fo-ga y fd-gd). Aula: 16 (comprensión lectora, plan de área, emergencia, evaluación y reclamos, datos de salud, maltrato, ideas de hacerse daño). Orientador: 11 (vocacional, reserva con la familia, saque de clase, riesgo suicida, violencia intrafamiliar, discriminación, remisión a salud y comisaría). Directivos: 14 (consejo directivo, proveedor, ausencias y llegadas tarde, queja, vacante, redes sociales, rendición de cuentas, director rural, situación tipo I).
POR QUE: Ariel dijo que los casos de todos los cargos estaban muy básicos. Antes eran de una línea con tres opciones obvias; ahora traen contexto (grado, cifras, actores, presión), cuatro opciones todas plausibles y una explicación que dice por qué fallan las tentadoras.
COMO SE HIZO: se reemplazan q, o, a y e por coincidencia exacta del enunciado viejo; se conservan niv, nuevo y caso. Correctas barajadas con semilla fija (pos. 0:11, 1:11, 2:14, 3:9) y distractores alargados con una razón tentadora para que la correcta no sea siempre la más larga. Normas solo las que ya citaba el capítulo (Ley 1620/2013, Decreto 1965/2013, Ley 1098/2006, Decreto 1075/2015, Ley 715/2001, Ley 1581/2012, Ley 1616/2013, Constitución art. 29). d-doc comprobado idéntico al reserializar; br-ddoc regenerada; CE-PUB 33503544. Chromium 400 px, 5 niveles, 0 errores.
QUE FALTA: quedan unas 800 preguntas por subir de nivel (cc, gestión académica de primaria, áreas, normas, preescolar y primaria, fun-aula, fun-ori). Revisar los artículos exactos de Ley 1098 y Ley 2025 con un abogado/educador antes de la próxima tanda.

## 14 nov 2026 - cartilla.enc (Docentes: casos más complejos, tanda 2)
QUE SE HIZO: 37 preguntas situacionales básicas pasan a casos completos. Competencias comportamentales (16: liderazgo con equipo desmotivado, docente nuevo, crítica pública, acoso, padre molesto, compañero que no entrega, enfoques distintos, plazos, mediación, regalo por una nota, cambio de horario, error en una nota, materiales, estudiantes sin desayuno, resultados bajos); ciencias sociales (5); ética (4); economía y política (4); ciencias naturales (6: sin laboratorio, salpicadura, circuito, residuos, microescala, evolución); lengua (1) e inglés (1).
POR QUE: continúa el pedido de Ariel de subir el nivel de los casos de todos los cargos.
COMO SE HIZO: igual que la tanda 1 (reemplazo por enunciado exacto, se conservan niv/nuevo/caso, correctas barajadas con semilla 15112026). Como las correctas salían siempre más largas, se agregó a una incorrecta por ítem una cola plausible para que la más larga no delate la respuesta. d-doc idéntico al reserializar; br-ddoc regenerada; CE-PUB 33529971. Chromium 400 px 5 niveles, 0 errores.
QUE FALTA: ~760 preguntas por subir (gestión académica de primaria, esp-len/ing/mat restantes, normas 1278/1620, fun-aula/fun-ori, preescolar y primaria, psicotécnica). Las preguntas de definición pura (art. 4, 5, 6 del Decreto Ley 1278) no se convierten en caso.

## 14 nov 2026 - cartilla.enc (Docentes: casos más complejos, tanda 3, primaria y preescolar)
QUE SE HIZO: 21 preguntas de gestión académica de docente de aula (preescolar y primaria) pasan a casos completos: confusión b/d, comprensión lectora en 1.°, niña de transición que se aísla, suma con llevada, aula multigrado, lectura no fluida en 3.°, familia que dice «solo juegan», pensamiento científico, estudiante aislado, baja visión, discapacidad auditiva, PIAR, repartir en partes iguales, ritmos distintos, fracciones, huerta escolar, retroalimentación de cuaderno, evaluación formativa, rúbrica y madre molesta.
POR QUE: continúa el pedido de Ariel de subir el nivel de los casos de todos los cargos.
COMO SE HIZO: reemplazo por enunciado exacto, se conservan niv/nuevo/caso, correctas barajadas (semilla 15112026); la opción más larga queda repartida entre correcta e incorrectas. d-doc idéntico al reserializar; br-ddoc regenerada; CE-PUB 33543194. Chromium 400 px, 5 niveles, 0 errores.
QUE FALTA: ~740 preguntas (normas 1278 y 1620, fun-aula, fun-ori, esp-fpre/fpri/fare, pra-soc, esp-prim/pre, lengua, inglés y matemáticas restantes, fa-gad/gco, fo-gad/gco, fd-ga/gad/gco).

## 14 nov 2026 - cartilla.enc (Docentes: casos más complejos, tanda 4, funciones de aula y orientador)
QUE SE HIZO: 24 preguntas cortas de «Tus funciones» pasan a casos completos: 16 de docente de aula (referentes del MEN, Escuela Nueva, maltrato en casa, barreras de aprendizaje, reclamo de nota, PAE, personero, inasistencia, proporcionalidad en zona cafetera, contabilidad del Fondo, plan de área, DUA, diagnóstico, daño de un equipo) y 8 de orientador (sanción pedida por el rector, carpeta de un estudiante, proceso socio-ocupacional, salud mental, alertas de deserción, crisis con ideas de hacerse daño, docente que humilla a un estudiante).
POR QUE: continúa el pedido de Ariel de subir el nivel de los casos de todos los cargos.
COMO SE HIZO: igual que las tandas anteriores; para evitar que la correcta sea siempre la más larga se alarga una incorrecta cuando hacía falta (queda la correcta más larga en 1 de 24). d-doc idéntico al reserializar; br-ddoc regenerada; CE-PUB 33559524. Chromium 400 px, 5 niveles, 0 errores.
QUE FALTA: ~715 preguntas (fun-aula 16–35 y fun-ori 10–18 ya eran largas; faltan esp-fpre/fpri/fare, esp-prim/pre, pra-soc, lengua, inglés y matemáticas restantes, fa-gad/gco, fo-gad/gco, fd-ga/gad/gco, nor-dir, fun-norm).

## 14 nov 2026 - cartilla.enc (Procuraduría: lección nueva del MIPG según Función Pública v7)
QUE SE HIZO: lección nueva con la marca NUEVO al final del capítulo «Sistemas de gestión y control interno» (SG) de la cartilla de Procuraduría: «MIPG según Función Pública (Manual Operativo versión 7, 2026): 6 dimensiones y 20 políticas». Trae términos clave, la definición literal del Manual (cap. 2), las 6 dimensiones con las políticas de cada una (sec. 1.4 a 6.4 del Manual), el Decreto 995 de 2026 (política 20, Gestión ambiental institucional; expedido el 4 de agosto y publicado el 5 de agosto de 2026, D.O. 53.578), un cuadro MIPG frente al MiPGN de la Procuraduría (11 dimensiones y 26 políticas; Resolución 239 de 2024, art. 2: preside el Secretario General), un caso y la fuente.
POR QUE: Función Pública pasó el MIPG de 7 dimensiones y 19 políticas a 6 y 20 (Manual v7, 28 de agosto de 2026). La cartilla solo enseñaba la versión anterior. La Procuraduría no ha publicado cambios a su MiPGN (sigue con 7 operacionales), por eso no se borra nada: se enseñan las dos versiones con su fuente.
COMO SE HIZO: se agrega un bloque en el script s-pgn justo antes de add("USU",...), con la 4.ª posición de la tupla en 1 (muestra NUEVO en la lista y el encabezado) y b.nuevo=1. Va al final del capítulo, así que no cambian los índices del avance guardado (S.temas). No se tocaron los textos «siete dimensiones» ni «19 políticas» ya existentes. CE-PUB recalculado en bytes (33566298). Control: node --check del script s-pgn sin errores; prueba del bloque aislado (la lección se arma con 3 tablas); la página carga sin errores de script. No se probó la pantalla del alumno de Procuraduría porque exige código de acceso.
QUE FALTA: decidir si se actualizan o se anotan los textos que dicen «siete dimensiones» o «19 políticas» (≈137 sitios en DIAN, Procuraduría, CAR y Docentes); agregar la sentencia C-030 de 2023 (función disciplinaria de la Procuraduría, administrativa, con revisión del Consejo de Estado); abrir la Resolución 124 de 2020 y su anexo para confirmar cifras; revisar el peso 70 % del cargo 1AS y la Resolución 298 de 2026. Notas de verificación guardadas en Drive: CONCURSOS / «MIPG - Procuraduría vs Función Pública».

## 14 nov 2026 - cartilla.enc (Docentes: casos más complejos, tanda 5, rector y coordinador)
QUE SE HIZO: 37 preguntas cortas de directivos pasan a casos completos (45 apariciones, porque algunas se repiten en varios capítulos): gestión directiva (rector nuevo con baja asistencia, autoevaluación por las cuatro áreas de la Guía 34, indicador de deserción, tipo II con ciberacoso, coordinador que asume disciplina, órdenes que chocan, delegar jornadas, manual de convivencia, PIAR, plan de área, reclamo de nota con el SIEE, observación de aula, Saber 11.°, lectura en 3.°, aprendizaje por proyectos, presupuesto del Fondo, obsequio de proveedor, evaluación de una docente antigua, conflicto de horarios, consejo de padres), funciones frecuentes del rector (26 horas, informe a los seis meses, evaluación con mala relación, cupos de diplomado, media técnica, Consejo Académico, descuento sin cotizaciones) y del coordinador (inducción, planeaciones, reuniones de área, estudiante con bajo rendimiento y peleas, mallas de 5.° y 6.°).
POR QUE: continúa el pedido de Ariel de subir el nivel de los casos de todos los cargos.
COMO SE HIZO: reemplazo por enunciado exacto, se conservan niv/nuevo/caso; correctas barajadas (semilla 15112026); para que la correcta no sea siempre la más larga se amplían dos incorrectas con una aclaración entre paréntesis (queda la más larga en 6 de 45). Explicaciones con las normas ya usadas en los capítulos (Res. MEN 3842 de 2022, Decreto Ley 1278 de 2002 arts. 6 y 32, Ley 115 arts. 87 y 145, Ley 715 art. 10, Decreto 1965 arts. 40 y 43, Decreto 1421, Decreto 1075, Decreto 1286). d-doc idéntico al reserializar y el resto del archivo idéntico (control byte a byte fuera de d-doc, br-ddoc y CE-PUB); br-ddoc regenerada; CE-PUB 33588405. Chromium 400 px, 5 niveles, 0 errores.
QUE FALTA: ~680 preguntas (nor-1278 y nor-conv restantes, nor-dir, esp-fpre/fpri/fare, esp-prim/pre, pra-soc, lengua, inglés y matemáticas restantes, fa-gad/gco, fo-gad/gco, fd-ga/gad/gco, fun-norm).

## 14 nov 2026 - cartilla.enc (Docentes: directivos, tanda A de contenido nuevo)
QUE SE HIZO: 9 lecciones nuevas con marca NUEVO, 23 preguntas situacionales nuevas y el primer glosario de Docentes (bloque «Conceptos y normas» con definiciones literales). Rector: Fondo de Servicios Educativos (quién aprueba, quién ordena, en qué se puede gastar y prohibiciones); el año del Fondo (presupuesto, flujo de caja, adiciones, traslados, informes, informe al alcalde en municipios no certificados); horario, 40 semanas, intensidades mínimas y jornada laboral. Coordinador: asignación académica (20/25/22) y número de coordinadores por matrícula; SIEE, promoción, promoción anticipada, cupo garantizado y reclamaciones; las 5 semanas de desarrollo institucional. Director rural: centro educativo frente a institución (Ley 715 art. 9) y director rural (150 estudiantes); Escuela Nueva (qué es rural, cinco componentes); el Fondo en un centro rural (salidas, semovientes, lo que no se paga).
POR QUE: primera tanda del plan de la auditoría de Docentes (directivos), pedida por Ariel.
COMO SE HIZO: textos literales copiados del Gestor Normativo de Función Pública el 14-nov-2026: Decreto 1075 de 2015 arts. 2.3.1.6.3.2 a 2.3.1.6.3.6, 2.3.1.6.3.11 a 2.3.1.6.3.14, 2.4.3.1.2, 2.4.3.2.1 (con la remisión al Decreto 277 de 2025), 2.4.3.2.4, 2.4.3.3.3, 2.3.3.3.3.4, 2.3.3.3.3.6, 2.3.3.3.3.7, 2.3.3.3.3.11, 2.3.3.5.7.1, 2.3.3.5.7.2, 2.4.6.1.2.1 a 2.4.6.1.2.3; Ley 715 de 2001 art. 9. Lecciones con términos clave, norma literal, explicación, caso y «Cómo te lo preguntan». Lecciones al final de esp-rec, esp-coo y esp-dru, más el campo conceptos (genera la lección «Conceptos y normas» y alimenta el glosario). Ojo: la lección «Fuentes y normas del capítulo» de esos tres capítulos cambia de posición; si alguien la había marcado como estudiada, la marca queda en otra lección. Opciones barajadas (semilla 14112026) y dos incorrectas ampliadas con una aclaración entre paréntesis (la correcta es la más larga en 1 de 21 revisadas). Control: resto del archivo idéntico byte a byte fuera de d-doc, br-ddoc y CE-PUB (33649385); Chromium 400 px en los 5 niveles sin errores; capítulo del director rural revisado con las 5 lecciones nuevas y su glosario.
QUE FALTA (tanda B de directivos): Guía 34 completa; matrícula y SIMAT; PAE; evaluación anual y período de prueba del personal; situaciones administrativas; control de asistencia y novedades. Faltan unas 130 preguntas para llegar a la meta de los tres cargos.

## 14 nov 2026 - cartilla.enc (Docentes: directivos, tanda B1, Guía 34)
QUE SE HIZO: 4 lecciones nuevas con marca NUEVO en «Competencias funcionales del directivo docente» (fd-gd, que ven rector, coordinador y director rural): las cuatro áreas de gestión y sus procesos; la ruta del mejoramiento en tres etapas y sus pasos (horizonte de tres años); metas e indicadores de proceso y de resultado con su ficha; la escala existencia, pertinencia, apropiación y mejoramiento continuo. 14 preguntas situacionales nuevas y 5 conceptos al glosario del capítulo.
POR QUE: tanda B del plan de directivos; Ariel subió el PDF de la Guía 34 del MEN.
COMO SE HIZO: lectura del PDF (Guía para el mejoramiento institucional, Cuadros 3 y 4, num. 1.11, etapa 2 pasos 2 y 3, Anexo 1). Cuadros y explicaciones son síntesis propia; las citas textuales son breves y llevan la fuente. Lecciones al final de fd-gd y campo conceptos (la lección «Fuentes y normas del capítulo» de fd-gd cambia de posición). Opciones barajadas (semilla 14112027), con aclaraciones entre paréntesis en incorrectas cuando hacía falta (la correcta no es la más larga en ninguna de las 14). Control: resto del archivo idéntico byte a byte fuera de d-doc, br-ddoc y CE-PUB (33675248); Chromium 400 px, 5 niveles, 0 errores; fd-gd revisado con director rural.
QUE FALTA (tanda B2): matrícula y SIMAT; PAE; evaluación anual y período de prueba del personal; situaciones administrativas; control de asistencia y novedades.

## 14 nov 2026 - cartilla.enc (Docentes: directivos, tanda B2, matrícula, PAE y evaluación de desempeño)
QUE SE HIZO: 4 lecciones nuevas con marca NUEVO y 15 preguntas situacionales. En «Tus funciones como rector o director rural» (esp-frec, que ven rector y director rural): matrícula y SIMAT (competencias del rector, cinco etapas, orden de prioridad de cupos, retiro sin exigir constancia, reserva de datos); el PAE en el establecimiento (priorización por la entidad territorial, ajustes del rector con el CAE con soporte en SIMAT, CAE presidido por padres); evaluación anual de desempeño (tres meses, quién evalúa, 70/30, escala 1-100, reposición y apelación, impedimentos, consecuencias para docentes y directivos). En esp-coo: el papel del coordinador en la evaluación (apoya con evidencias; evalúa el rector). 4 conceptos al glosario de esp-frec. Se corrige la explicación de la pregunta de tanda 5 sobre evaluar a un docente con relación tensa: ahora menciona la vía del impedimento si hay causal legal.
POR QUE: tanda B del plan de directivos; Ariel subió la Res. 7797 de 2015, la Res. 335 de 2021 y la Guía 31.
COMO SE HIZO: textos literales de los PDF subidos (Res. MEN 7797 de 2015 arts. 3, 6, 10, 11, 12, 13, 23, 25, 31; Res. UApA 00335 de 2021 arts. 3, 4, 5, 10, 11) y del Gestor Normativo (Decreto 1075 de 2015 arts. 2.4.1.5.1.5, 2.4.1.5.1.6, 2.4.1.5.2.1, 2.4.1.5.2.6, 2.4.1.5.2.7, 2.4.1.5.3.2 a 2.4.1.5.3.4, que compilan el Decreto 3782 de 2007), más la Guía 31 del MEN para el ejemplo de ponderación. Opciones barajadas (semilla 14112028). Control: resto del archivo idéntico byte a byte fuera de d-doc, br-ddoc y CE-PUB (33707473); Chromium 400 px, 5 niveles, 0 errores; esp-frec revisado con rector.
ALERTA PARA REVISAR (no se cambió): las 5 lecciones «Evaluación de desempeño» de nor-1278 citan el «Manual de la evaluación de desempeño (MEN)» anterior (escala de 1 a 6 por aspecto, 60 % de 84 o de 90 puntos, Formatos A y B). La norma vigente (Decreto 1075 de 2015, cap. 2.4.1.5, Decreto 3782 de 2007) usa competencias 70/30 y escala de 1 a 100. Hay que decidir si se reescriben.
QUE FALTA (tanda B3): situaciones administrativas del personal (permisos, licencias, comisiones, encargos, vacaciones) y novedades; período de prueba.

## 15 nov 2026 - cartilla.enc (copias comprimidas br-pgn y br-doc regeneradas)
QUE SE HIZO: se regeneraron br-pgn y br-doc desde su fuente (s-pgn y s-doc). Las otras cuatro copias ya estaban al día.
POR QUE: error de las sesiones del 14 nov: se editaron s-pgn (lección «MIPG según Función Pública», commit a51b10a) y s-doc (migración de avance de la fusión de capítulos, commit af48be5) sin regenerar su copia Brotli, que es la que el servidor entrega a los clientes. Resultado: a los clientes de Procuraduría no les llegaba la lección del MIPG v7, y a los de Docentes no les llegaban la migración del avance guardado ni la redirección de enlaces de capítulos fusionados. Los datos de Docentes (d-doc y br-ddoc) sí estaban al día, así que las lecciones y casos nuevos sí llegaban. Con la copia vieja, la cartilla de Docentes cargaba sin errores en los 5 niveles (comprobado).
COMO SE HIZO: cada copia se verificó descomprimiéndola contra su fuente; CE-PUB 33707473 sin cambio; Chromium 400 px, 5 niveles, 0 errores.
QUE FALTA: nada de esto. Recordatorio: aplicar siempre la regla de regenerar br-* tras editar s-* o d-*.

## 15 nov 2026 - sitio.pak, php.pak, cartilla.enc (página Material de estudio Procuraduría, títulos en Public Sans, enlace en el menú)
QUE SE HIZO: (1) Página nueva /guias/material-de-estudio-procuraduria-2026 para posicionar «material de estudio concurso Procuraduría 2026»: documentos oficiales en línea de tiempo (Res. 076, 108 y 133 de 2026, manual de funciones, diccionario de competencias), pesos por nivel con pestañas, barras y calculadora de puntaje ponderado (70/20/10 y 60/20/20, mínimo 65 eliminatorio), 12 ejes en tarjetas que se voltean, material gratis, la cartilla por cargo (desde $40.000 hasta $55.000), preguntas frecuentes; datos estructurados Article, BreadcrumbList y FAQPage; agregada al sitemap. (2) Menú «Concursos» de las 901 páginas: nueva línea «↳ Material de estudio concurso Procuraduría» bajo Procuraduría 2026. (3) /procuraduria: título «Prueba gratis: diez preguntas…», textos en tú («Pide tu acceso», «Escríbenos y te indicamos…», «de tu concurso»), recuadro que enlaza a la página nueva, la guía de primera en «Guías de estudio sin costo», respuesta de «¿Puedo probar antes de pagar?» (también en el JSON-LD) con la prueba, el simulacro y el material. (4) Títulos h1-h3 de todo el sitio y de la cartilla en Public Sans 600/700 (OFL, servida desde api.php?a=font&f=ps6/ps7) y sin resaltado de color en h1; el logo no cambia. Regla en api.php (fcss) con selector :is(h1,h2,h3):not(#ce-z) para ganar a los estilos de cada página. Versión de la hoja de fuentes cambiada a ?a=fcss&v=2 en las 901 páginas, la nueva y el encabezado de la cartilla, porque la anterior se guardaba un año en caché.
POR QUE: pedido de Ariel (página para Google, títulos más serios, diseño más interactivo); aprobó las maquetas y dijo «Publica».
COMO SE HIZO: plantilla de guias/ebook-gratis; Playwright 400 y 1280 px con servidor local: 0 errores, sin desborde; 12 enlaces internos verificados; HMAC y zip verificados al empacar. Para revertir la fuente: quitar las 4 líneas de Public Sans en fcss (api.php). CE-PUB 33707481 (el enlace de la cartilla está fuera de los scripts s-*, así que las copias br no cambian).
QUE FALTA: menú igual en todos los anchos de pantalla (hoy Noticias, Precio y Preguntas se ocultan por debajo de ~1.300 px), sacar «Volver a la búsqueda» de la barra en las páginas de cargo y poner el encabezado normal en pagar.html (maqueta pendiente). Pedir indexación en Search Console. Confirmar cuántas preguntas tiene el simulacro gratis de Procuraduría.

## 15 nov 2026 - sitio.pak, php.pak (menú superior igual en todas las páginas)
QUE SE HIZO: (1) Desde 641 px de ancho, todas las páginas muestran las mismas opciones del menú: Inicio, Concursos, Noticias, Precio y Preguntas (antes Noticias, Precio y Preguntas se ocultaban por debajo de 1.340 px y por debajo de 1.280 px quedaba solo Inicio). Para que quepan, los botones de la derecha se retiran en este orden cuando falta espacio: Facebook y modo oscuro (≤1.340 px), Suscríbete y WhatsApp (≤1.260 px; WhatsApp sigue en el botón flotante), nombre del logo (≤1.000 px, queda el ícono). En celular (≤640 px) sigue la barra inferior. (2) «← Volver a la búsqueda» sale de la barra en las 837 páginas de cargo y listados de cargos y pasa justo debajo de la franja del concurso (conserva id="back" donde lo tenía). (3) pagar.html usa ahora el mismo encabezado, menú desplegable, barra inferior móvil y scripts que el resto (copiados de terminos.html); los estilos genéricos «header» propios de pagar se limitaron a header.pghd para que no pisen el encabezado nuevo; carga la hoja de fuentes v=2.
POR QUE: Ariel pidió que el contenido del menú sea igual en todas las páginas («Todos deben ser iguales»), también en la de pago.
COMO SE HIZO: reglas en api.php (fcss) con :not(#ce-z) para ganar a los estilos de cada página; prueba con Playwright en 19 anchos entre 641 y 1.440 px en inicio y una página de cargo (ninguna opción se corta ni desborda); pagar.html probado en 400, 900 y 1.440 px sin errores de script, con el desplegable funcionando y el formulario de pago visible; encabezado comparado contra terminos.html (idéntico). Para revertir: quitar las líneas del bloque «menu igual» en fcss.
QUE FALTA: nada de esto.

## 16 nov 2026, 10:55 — Noticia DIAN 2676 (resultados) y botón para compartir en todas las noticias
- QUÉ SE HIZO: nueva noticia guias/noticia-dian-2676-resultados-prueba-escrita-noviembre (resultados iniciales esperados entre el 21 y el 30 de noviembre, reclamaciones y definitivos), aclarando que no es aviso oficial de la CNSC. Pasa a ser la principal en guias/noticias-concursos (la anterior de DIAN baja a "Últimas noticias") y entra al sitemap. Las 5 noticias tienen ahora el bloque "Compartir esta noticia" (Facebook, WhatsApp, X, LinkedIn, Telegram, Copiar resumen).
- POR QUÉ: Ariel pidió que al compartir cualquier noticia se copie solo un resumen con el enlace y al final "✍️ concursosdelestado.com", para que la persona solo pegue en su publicación.
- CÓMO SE HIZO: cada noticia lleva su resumen en <script type="text/plain" id="ce-copy">. El script ce-share-js copia resumen + enlace (?f=red, para medir de dónde llegan) + firma y abre la red. También hace que el botón flotante "Compartir" copie el resumen en las noticias (antes solo copiaba el enlace). Probado en navegador: el portapapeles termina en la firma en las 5 noticias, sin errores.
- QUÉ FALTA: toda noticia nueva debe salir con su bloque y su resumen.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 11:10 — Tarjeta propia para redes en cada noticia + instrucciones para la IA
- QUÉ SE HIZO: cada una de las 5 noticias tiene ahora su tarjeta de 1200x630 (og-<slug>.png en la raíz) en vez de la genérica og-guias.png (en X salía og-tips-examen-dian.png). Se actualizaron og:image, og:image:alt, twitter:image (+ twitter:image:alt) y la imagen del NewsArticle en el JSON-LD. Se escribió README.md con las instrucciones para la IA y la "Regla de las noticias", y se guardaron los generadores en herramientas/noticias/ (share.py, mkog.py, logo.svg).
- POR QUÉ: Ariel pidió que cada noticia se cree con su tarjeta, para que al compartirla no salga la tarjeta general de la página. También pidió dejar siempre en el commit las instrucciones y comentarios para la otra IA.
- CÓMO SE HIZO: tarjetas en HTML renderizadas con Playwright (fuentes Public Sans, Source Serif, IBM Plex Mono); maqueta aprobada por Ariel. Verificado: 0 referencias a la tarjeta genérica en las noticias.
- QUÉ FALTA: Ariel debe pasar los 5 enlaces por el depurador de Facebook (Volver a extraer) para que olvide la tarjeta vieja. REGLA PERMANENTE: toda noticia nueva sale con tarjeta propia, bloque Compartir y resumen (ver README.md).
- Para volver atrás: revertir este commit.

## 16 nov 2026, 12:30 — Cuarto ebook gratis: Guía de estudio del concurso docente 2026
- QUÉ SE HIZO: nuevo ebook "Guía de estudio: concurso docente 2026" (24 páginas ilustradas: los cuatro componentes de la prueba de aptitudes, normas citadas al pie de la letra —DL 1278 arts. 4 y 5, Ley 115 art. 73, Decreto 1965 art. 40, Decreto 1421, Res. MEN 3842—, SIEE, convivencia, inclusión/PIAR, competencias por cargo, psicotécnica, 7 casos con respuesta razonada, plan y glosario). Página /guias/ebook-guia-estudio-docente (mismo formulario y entrega por correo que el ebook docente), tarjeta en /guias, sitemap e imágenes og-ebook-gdoc*. Servidor (php.pak): id "gdoc" en _suscripcion.php, descargar.php (Drive 1UWA_P8dZuWOv0AsS9WWZWAlEbqO_X2zN, compartido con enlace), confirmar.php (solo correo, igual que "doc"), acceso/lib.php (marcador {enlace_ebook_gdoc}) y acceso/chat_core.php (el bot ahora dice que hay CUATRO ebooks).
- POR QUÉ: Ariel pidió un ebook con la guía de estudio del concurso docente, muy pedagógico e ilustrado, publicado en la web y en el Drive, con imagen y copy para promocionarlo.
- CÓMO SE HIZO: contenido tomado de las lecciones ya verificadas de la cartilla Docentes, del Anexo técnico 2026 y de la Res. 3842 de 2022; HTML con ilustraciones SVG propias renderizado a PDF con Playwright. Fuentes en herramientas/ebook-guia-docente/ (build.py, content.py, ill.py, promo.py). Formulario probado en navegador: envía ebook "gdoc" y muestra el mensaje de envío al correo. Sintaxis PHP verificada (php -l).
- QUÉ FALTA: Ariel debe pedir indexación de la página nueva en Search Console. No se incluyen preguntas sobre etapas del concurso (regla del 6 nov). Cuando la CNSC publique la Guía de orientación, revisar el ebook.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 13:10 — Docentes, tanda E1: lecciones más completas para primaria y preescolar
- QUÉ SE HIZO: revisión del concurso Docente: de 483 lecciones, 276 tienen menos de 1.500 caracteres (las más cortas: esp-nat, esp-art, esp-ing, esp-mat, esp-len, man-sec, prueba y los bloques esp-* de cada área). Se reescribieron en el sitio (mismo título y posición, marcadas "nuevo") las 6 lecciones más cortas de "Tu cargo: docente de primaria" y las 4 de "Tu cargo: docente de preescolar": pasan de 500 a 900 caracteres a entre 1.700 y 3.300, con caso inicial, tablas, norma, explicación simple, errores frecuentes y "Para el examen". Temas nuevos dentro de ellas: las nueve áreas del art. 23 de la Ley 115, referentes de calidad (lineamientos, estándares, DBA, mallas), proyectos transversales del art. 14, cinco componentes de la lectura, momentos de la escritura, cinco pensamientos y procesos matemáticos, concreto-pictórico-abstracto, problemas aditivos, DUA, Escuela Nueva, planeación hacia atrás, tipos de evaluación, actividades rectoras, propósitos de las Bases Curriculares, alfabetización emergente, transiciones y cuidado. Se agregan 16 preguntas de casos (9 primaria, 7 preescolar) y 12 conceptos al glosario.
- POR QUÉ: Ariel pidió revisar el concurso docente y hacer lecciones más completas, con contenido de estudio.
- CÓMO SE HIZO: /tmp/cce/fix7/enr_a.py (REPL por título, Q, C) y patch13.py (mismo patrón de patch12: reemplaza l['p'], agrega preguntas con distractores equilibrados, regenera br-ddoc y CE-PUB). Verificado: las 6 copias br coinciden con su fuente, CE-PUB correcto, todo lo anterior a d-doc queda idéntico, HTML de las lecciones balanceado. No cambian índices de lecciones (el avance guardado de los clientes no se mueve).
- QUÉ FALTA: seguir la misma mejora, en este orden: esp-nat (40 cortas), esp-art (23), man-sec (16), esp-ing (16), esp-mat (15), esp-len (15), y luego ética, económicas, filosofía, tecnología, ed. física, religiosa, sociales, pra-soc. El bloque "prueba" (25 lecciones cortas sobre el concurso) se deja corto a propósito. Los conceptos sin texto literal de norma llevan n vacío.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 13:50 — Docentes, tanda E2: ciencias naturales con contenido de estudio
- QUÉ SE HIZO: en "Tu área: ciencias naturales" se reescribieron en el sitio (mismo título y posición, marcadas "nuevo") 17 lecciones cortas: 5 de la base común (tres grupos de estándares, seguridad, indagación, ideas previas, CTS y PRAE), 4 de física (cinemática con ejemplos resueltos, mapa de la disciplina con relaciones y unidades SI, leyes de Newton e ideas previas, lectura de gráficas y energía), 4 de química (mezclas, soluciones, molaridad y pH; mapa de la disciplina, mol y leyes de los gases; los tres niveles con la combustión del metano; seguridad, SGA y química verde) y 4 de biología (niveles de organización y compromisos; célula, fotosíntesis/respiración, mitosis/meiosis; selección natural, genética y regla del 10 %; educación ambiental con datos y salida de campo). Pasan de 350-800 caracteres a 2.000-3.300. Se agregan 20 preguntas de casos (aula + aplicación del saber) y 10 conceptos al glosario. El capítulo queda con 64 preguntas.
- POR QUÉ: Ariel pidió seguir con lecciones más completas, con contenido de estudio; ciencias naturales era el capítulo más corto (40 de 43 lecciones cortas).
- CÓMO SE HIZO: /tmp/cce/fix7/enr_b.py y patch14.py (mismo patrón de patch13). Normas citadas: Decreto 1743 de 1994 y Ley 1549 de 2012 (PRAE y educación ambiental), Decreto 1496 de 2018 (SGA), Ley 115 art. 14. Cálculos de los ejemplos revisados a mano. Verificado: 6 copias br al día, CE-PUB correcto, contenido anterior a d-doc idéntico, HTML balanceado, índices sin cambios.
- QUÉ FALTA: en esp-nat quedan cortas las 4 lecciones "La norma que crea tu cargo" (repetidas a propósito) y los 6 casos de "Práctica de aula". Siguen: esp-art (23), man-sec (16), esp-ing (16), esp-mat (15), esp-len (15) y las demás áreas. El contenido disciplinar se escribió sin contrastar hoy contra los PDF de estándares; cuando salga la Guía de orientación, ajustar el temario.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 14:20 — Docentes, tanda E3: educación artística con contenido de estudio
- QUÉ SE HIZO: en "Tu área: educación artística" se reescribieron en el sitio (mismo título y posición, marcadas "nuevo") 16 lecciones cortas: 4 de la base común (las tres competencias en los cuatro lenguajes, secuencia percibir-analizar-crear-mostrar-reflexionar y patrimonio, proyecto artístico frente a decorar, evaluación con rúbrica y bitácora) y 3 por cada lenguaje: música (elementos, figuras y compases, escala y acordes, familias de instrumentos, músicas por región, métodos Orff, Kodály, Dalcroze, Suzuki y Willems), danzas (cinco elementos, estructura de clase, danzas por región, vocabulario de composición, proceso de creación, inclusión), artes escénicas (elementos del hecho teatral, géneros, Stanislavski, Brecht, Boal, creación colectiva, secuencia de enseñanza, teatro foro, cuidado ético) y artes plásticas (lenguaje visual, color, composición, perspectiva, técnicas, lectura de imagen, etapas del dibujo, proyecto y bitácora). Pasan de 230-800 caracteres a 1.900-3.000. Se agregan 20 preguntas de casos y 10 conceptos. El capítulo queda con 85 preguntas.
- POR QUÉ: Ariel pidió seguir con lecciones más completas; artes era el segundo capítulo más corto (23 de 25 lecciones cortas).
- CÓMO SE HIZO: /tmp/cce/fix7/enr_c.py y patch15.py (mismo patrón). Verificado: 6 copias br al día, CE-PUB correcto, contenido anterior a d-doc idéntico, HTML balanceado, índices sin cambios.
- QUÉ FALTA: en esp-art quedan cortas las 5 lecciones "La norma que crea tu cargo" (repetidas a propósito), "Lo que te exige el manual" y dos más. Siguen: man-sec (16), esp-ing (16), esp-mat (15), esp-len (15) y las demás áreas. Contenido escrito sin contrastar hoy contra el Documento 16 del MEN.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 14:50 — Docentes, tanda E4: inglés, matemáticas y lengua castellana
- QUÉ SE HIZO: se reescribieron en el sitio (mismo título y posición, marcadas "nuevo") 18 lecciones cortas, 6 por área. Inglés: escala de la Guía 22 por grupos de grados y competencia comunicativa; principios y técnicas de aula (input comprensible, TPR, vacío de información, tareas, AICLE); referentes y niveles del MCER; enfoque comunicativo y aprendizaje basado en tareas; interlengua, fluidez/precisión y técnicas de corrección; evaluación por habilidad con rúbrica. Matemáticas: cinco pensamientos y cinco procesos con ejemplos; el error como información; referentes (Lineamientos, Estándares, DBA, Mallas, Saber, Van Hiele); contenidos por pensamiento con ejemplos resueltos; origen de los errores y obstáculos de Brousseau; evaluación con Polya y rúbrica. Lengua: cinco factores; tipologías textuales y secuencia didáctica; referentes y competencias de los Lineamientos; tres niveles de lectura, conectores, hecho y opinión; escritura como proceso y texto argumentativo; géneros, figuras literarias, literatura colombiana, medios y ética. Pasan de 190-900 caracteres a 1.900-2.900. Se agregan 18 preguntas de casos (6 por área) y 12 conceptos.
- POR QUÉ: Ariel pidió seguir con lecciones más completas.
- CÓMO SE HIZO: /tmp/cce/fix7/enr_d.py y patch16.py (patrón generalizado para varios bloques). Verificado: 6 copias br al día, CE-PUB correcto, contenido anterior a d-doc idéntico, HTML balanceado, índices sin cambios. Cálculos de los ejemplos de matemáticas revisados a mano.
- QUÉ FALTA: man-sec (16 cortas), ética, económicas, filosofía, tecnología, ed. física, religiosa, sociales, pra-soc, y los casos de "Práctica de aula" de cada área (700-1.000 caracteres). Contenido escrito sin contrastar hoy contra los PDF del MEN.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 15:10 — Directivos, tanda B3: Guía 34 nueva (Ruta de Mejoramiento Institucional, MEN 2026)
- QUÉ SE HIZO: en el capítulo de directivos (bloque fd-gd) se reescribieron las 4 lecciones de Guía 34 (mismo título y posición) y se agregaron 2 al final: "Objetivo del plan y factores críticos: urgencia, tendencia e impacto" y "Presupuesto, cronograma y seguimiento del plan: cerrar el ciclo anual". Se retiraron las 14 preguntas y 5 conceptos basados en la Guía 34 de 2008 y se pusieron 20 preguntas de casos y 7 conceptos con la versión 2026. El bloque queda con 16 lecciones y 107 preguntas.
- POR QUÉ: el MEN publicó la Guía 34 actualizada (2026). Cambios que dejaban mal lo anterior: el plan de mejoramiento ahora es ANUAL (antes "horizonte de tres años"); 15 procesos y 45 componentes (antes 93); áreas renombradas (directiva y estratégica, académica y pedagógica); procesos nuevos (acompañamiento y seguimiento académico, accesibilidad, estrategias para el bienestar y la permanencia, apoyo a la gestión de la cobertura); el plan anual tiene 7 pasos y el seguimiento 3; la priorización usa urgencia + tendencia + impacto (1 a 5).
- CÓMO SE HIZO: Ariel subió el PDF oficial a su Drive (articles-430002_recurso_3.pdf, 189 págs.). Texto extraído con pdftotext; contenido en /tmp/cce/fix7/enr_e.py (copia en /tmp/cce/privado/lecciones-directivos/, fuera del repo) y aplicación con patch17.py (patrón de patch16 + retiro de preguntas/conceptos viejos por texto). Citas textuales cortas verificadas contra el PDF. Verificado: br-ddoc igual a d-doc, CE-PUB correcto, contenido anterior a d-doc idéntico, HTML balanceado. Distribución de respuestas: posiciones 7/2/5/6; correcta más larga en 2 de 20 y más corta en 4 de 20.
- QUÉ FALTA: Guía 10 (período de prueba) y Guía del Fondo de Servicios Educativos (ya están en el Drive de Ariel); revisar que otras lecciones de directivos no citen la Guía 34 vieja (p. ej. menciones a "seguimiento académico" o "tres años" en lecciones de gestión académica/administrativa). Ariel subió además 8 PDF "articles-385321" para revisar.
- Para volver atrás: revertir este commit.

## 16 nov 2026, 15:40 — Corrección: se quitan del repo los scripts de lecciones de directivos
- QUÉ SE HIZO: se borró herramientas/lecciones-directivos/ (enr_e.py y patch17.py), que el commit a1e0e09 había subido por error. Contienen el texto de lecciones de pago y el repo es público. La cartilla.enc sigue cifrada y no cambia.
- REGLA PARA LA IA: nunca subir al repo scripts ni textos de lecciones/preguntas (enr_*.py, patch*.py de contenido). Guardarlos fuera del repo (por ejemplo /tmp/cce/privado/) o en el Drive de Ariel. El historial de git todavía conserva esos dos archivos en a1e0e09; limpiarlo requiere reescribir la historia y lo decide Ariel.
- Para volver atrás: no aplica.

## 16 nov 2026 — Menú superior más empresarial y elegante (todas las páginas)
**QUE SE HIZO:** el encabezado (menú) de todo el sitio cambia de aspecto: línea superior azul marino, fondo limpio con sombra suave, enlaces en gris azulado con subrayado dorado al pasar, botones más sobrios (Cuenta gratis azul marino, Mi cartilla con borde, Suscríbete dorado, WhatsApp con borde verde e ícono), botón de modo claro/oscuro con ícono luna/sol. Los textos y enlaces no cambian. Mismo menú en las 904 páginas.
**POR QUE:** pedido de Ariel: "más empresarial y elegante"; maqueta aprobada.
**COMO SE HIZO:** bloque CSS nuevo (CSSMENU) al final del CSS compartido que genera acceso/api.php?a=fcss (php.pak). Como ese CSS se guarda 1 año en el navegador, en sitio.pak los enlaces pasan de v=2 a v=3 para que todos vean el cambio. Probado en 9 páginas, 7 anchos, claro y oscuro: sin cortes ni desbordes.
**QUE FALTA:** nada; revisar en el celular real.
**Para volver atrás:** borrar el bloque CSSMENU de acceso/api.php y volver a v=2 (o revertir este commit).
Nota para la otra IA: el estilo de la luna va solo en button.thm (el enlace de Facebook comparte la clase .thm; no tocar esa regla).

## 16 nov 2026 — Docentes: Educación ética y valores humanos con el lineamiento 2026
**QUE SE HIZO:** en la cartilla de Docentes, bloque de Educación ética y valores humanos (esp-eti): 5 lecciones cortas reescritas y 6 lecciones nuevas (los cuatro ejes del modelo concéntrico, las 14 competencias ciudadanas y socioemocionales, progresión por niveles, evaluación formativa, marco normativo y adaptación en el PEI), 7 conceptos y 20 preguntas de caso nuevas (quedan 15 lecciones y 27 preguntas). Todo marcado como "nuevo".
**POR QUE:** el bloque era corto y no recogía los Lineamientos de formación ciudadana y desarrollo socioemocional del MEN (junio 2026), el documento más actualizado del tema.
**COMO SE HIZO:** se reescriben lecciones conservando título y posición (el progreso guardado no se mueve) y las nuevas van al final; se regeneran br-ddoc y CE-PUB. Verificado: firma, br-ddoc igual a d-doc, resto de la cartilla idéntico.
**QUE FALTA:** seguir con Ciencias Sociales (lineamiento 2026), económicas, filosofía, tecnología, ed. física y religiosa. Los scripts de lecciones NO van en este repo (contenido de pago).
**Para volver atrás:** revertir este commit (restaura cartilla.enc anterior).

## 16 nov 2026 — Portada: simulacro gratis como entrada principal y testimonios
**QUE SE HIZO:** en la portada (index.html) el botón principal del héroe pasa a "Haz el simulacro gratis" (cuenta gratis); "Ver precios" y WhatsApp quedan como enlaces secundarios. Nueva franja de confianza bajo el héroe: simulacros gratis, pago seguro con Wompi, pago único por concurso y 3 testimonios reales de clientes, sin nombre ("Aspirante · compró DIAN y Procuraduría"), con la nota "No garantizamos resultados".
**POR QUE:** auditoría del 16 nov: faltaba prueba social, la portada repartía la atención entre 11 botones y la mejor puerta de entrada (lo gratis) estaba escondida.
**COMO SE HIZO:** solo index.html dentro de sitio.pak; estilos en línea (clase m2trust, m2cta). Probado en 1440 y 390 px, claro y oscuro, sin desbordes.
**QUE FALTA:** (el retracto NO va en la portada por decisión de Ariel; solo en Términos y política) número real de aspirantes, Google Analytics (necesita ID G-), pantalla de diagnóstico al terminar el simulacro y seguimiento por correo/WhatsApp a 0, 1, 3 y 7 días.
**Para volver atrás:** revertir este commit. Nota para la otra IA: los testimonios son reales y anónimos a propósito; no agregar nombres ni inventar otros.

## 16 nov 2026 — Portada: tarjeta de pago más pequeña y buscador de cargos más amplio
**QUE SE HIZO:** en escritorio (1000 px o más) la tarjeta "Activa tu cartilla en minutos" pasa de 24 rem a 15 rem de ancho (letras más compactas, mismo contenido) y el buscador de cargos gana espacio (campo de unos 168 a 252 px, buscador de 664 a 826 px). Los desplegables ya no se cortan. En celular no cambia nada.
**POR QUE:** pedido de Ariel: la tarjeta ocupaba demasiado y dejaba el buscador apretado.
**COMO SE HIZO:** bloque <style id="m4"> al final del head de index.html. Ojo: el CSS compartido (fcss) fuerza tamaños de .hpay con !important, por eso las reglas nuevas usan html body .hero aside.hpay y !important.
**QUE FALTA:** (opcional) acortar el placeholder del campo a "Cargo, código u OPEC"; bloque "Prueba un caso" (tarjetas que voltean) pendiente de aprobación y de preguntas del banco de la cartilla.
**Para volver atrás:** borrar el bloque <style id="m4"> de index.html (o revertir este commit).

## 16 nov 2026 — Portada: secciones institucionales en tarjetas que voltean
**QUE SE HIZO:** cinco secciones de la portada pasan a tarjetas con imagen y título al frente que se voltean para mostrar el texto: Quiénes somos (aspirante), Misión visión y valores, Compromiso social (principios), Una startup nacida en Tunja y Cómo activar tu cartilla (4 pasos). 21 tarjetas con 21 íconos SVG propios. El párrafo de "Quiénes somos" baja de tamaño. Las cinco secciones suman unos 2.130 px de alto, antes unos 3.230 px. Los textos son los mismos de antes; "Precio al alcance" y el paso 2 ocupan dos columnas por su texto largo. Dos títulos de la sección de Tunja salen de sus propios párrafos y las tres etiquetas pasan a una línea de texto.
**POR QUE:** pedido de Ariel: las secciones se veían exageradas, quería tarjetas con imagen que se voltean al pasar el mouse y menos espacio en blanco.
**COMO SE HIZO:** bloque style#fx y un script de clic en el head de index.html, y markup nuevo con clase .fx (ids de sección intactos: nosotros, mision, compromiso, quienes-somos, como). El volteo por hover va en el contenedor fijo .fx (no gira) para que no parpadee; en celular se voltea al tocar; también con teclado. Probado con 42 caras (frente y reverso) en 21 anchos de 280 a 1920 px: sin desbordes de texto ni palabras partidas en escritorio. Ojo: en #compromiso el fondo es oscuro y las reglas llevan !important para que los títulos del frente se lean.
**QUE FALTA:** "Contenido de la cartilla" y "Antes de pagar, verifica" siguen con el formato anterior (pendiente si Ariel los quiere así); bloque "Prueba un caso" pendiente de aprobación y de preguntas del banco.
**Para volver atrás:** revertir este commit (restaura sitio.pak anterior).

## 16 nov 2026 — Portada: "Antes de pagar, verifica por ti mismo" con raya lateral
**QUE SE HIZO:** los cuatro temas (Empieza gratis, La norma citada, Pago único y claro, Una persona responde) pasan de cajas a texto con una raya de color a la izquierda (teal, dorado, azul y verde). La sección baja de unos 548 px a unos 370 px; la columna del pago es más ancha por su texto largo. Los textos no cambian.
**POR QUE:** pedido de Ariel: las tarjetas eran muy grandes (la del pago quedaba altísima); quería una raya en columna al lado izquierdo por tema.
**COMO SE HIZO:** solo se cambió el CSS del bloque .trb en index.html (border-left de 4px con --k por columna; grid 1fr 1fr 2fr 1fr desde 1000 px).
**QUE FALTA:** "Contenido de la cartilla" sigue con el formato anterior (se ofreció usar la misma raya); bloque "Prueba un caso" pendiente.
**Para volver atrás:** revertir este commit.

## 2026-11-16 · Portada con secciones alternadas y menu azul oscuro
- Portada: inicio (buscador) en blanco; secciones alternadas blanco / color degradado por tema (azul, verde azulado, indigo); precio en blanco.
- Menu superior en todas las paginas: azul oscuro unico, logo en bloque blanco desde el borde izquierdo, separacion pareja entre enlaces e iconos (CSS en api.php fcss, bloque CSSMENU; enlaces fcss pasan a v=4).

## 2026-11-16 · Corrige parpadeo del enlace "Saltar al contenido" al recargar
**QUE SE HIZO:** en 4 paginas (inicio, procuraduria, docentes, corporaciones autonomas) el enlace a la hoja de estilos compartida estaba en el body, despues del enlace "Saltar al contenido"; se movio al final del head (mismo orden de cascada).
**POR QUE:** el navegador pintaba un instante el enlace sin estilo antes de cargar la hoja.
**Para volver atras:** revertir este commit.

## 2026-11-16 · Procuraduria y DIAN con el mismo diseno de la portada
**QUE SE HIZO:** paginas procuraduria.html y dian.html: secciones alternadas blanco/color por tema (azul, verde azulado, indigo), "Como activar" como tarjetas que voltean; inicio claro en todas las paginas con hero (CSS compartido en api.php, bloque CSSMENU; fcss pasa a v=5). La pagina del quiz y su tarjeta se mantienen legibles.
**POR QUE:** pedido de Ariel: que todo el sitio quede igual y elegante.
**QUE FALTA:** paginas de cargos (691), concursos (180), guias (33) y legales conservan su diseno con el menu nuevo.
**Para volver atras:** revertir este commit.

## 2026-11-16 · Rocky busca cargos igual que las barras de busqueda
**QUE SE HIZO:** en acceso/chat_core.php (chat de la pagina y WhatsApp) Rocky ahora recibe, para cada mensaje con un numero o codigo, un bloque "RESULTADOS DE LA BUSQUEDA" con la misma logica de las barras del sitio: convocatoria/empleo de la Procuraduria (234-2026, "empleo 234"), OPEC de CAR y Docentes (basta una parte del numero), codigos (3PU-17) y numeros que aparecen en cargos DIAN/Procuraduria. Se agrego al indice de Rocky los 690 cargos DIAN/Procuraduria y 3.692 OPEC (CAR y Docentes) con nivel, vacantes y precio. Si no hay coincidencias, el bloque se lo dice y Rocky pide el nombre del cargo y la entidad o pasa a una persona. El prompt explica los formatos de busqueda.
**POR QUE:** Ariel probo "2000" y "234-2026" y Rocky no encontro el cargo (el indice anterior no tenia empleos ni OPEC).
**NOTA:** "2000" no existe como OPEC, codigo ni empleo en la lista; la barra del sitio tampoco lo encuentra. "234-2026" es el Empleo 234 de la Procuraduria (Sustanciador 4SU-11, tecnico, $45.000).
**QUE FALTA:** los cargos DIAN solo se encuentran por nombre/codigo (Cod. 101) y no por numero de convocatoria.
**Para volver atras:** revertir este commit (restaura php.pak anterior).

## 2026-11-16 · Concurso CAR (y paginas de concurso): inicio mas ancho y buscador amplio
**QUE SE HIZO:** en las paginas de concurso (CAR, docentes, Procuraduria, DIAN) el inicio ocupa todo su ancho: el buscador de cargos es mas ancho (el campo de texto pasa de ~106 px a ~300 px) y el texto ya no queda pegado a la izquierda (CSS compartido; fcss v=6).
**POR QUE:** en la pagina CAR el inicio reservaba una columna vacia para la tarjeta de pago que ya se muestra a un lado.
**Para volver atras:** revertir este commit.

## 16 nov 2026 - sitio.pak (Google Analytics 4 con consentimiento)
QUE SE HIZO: se creó la propiedad GA4 "Concursos del Estado" (flujo web www.concursosdelestado.com, ID de medición G-6ZR7H6EC6M, cuenta armandoavilacely@gmail.com) y se instaló gtag en todas las páginas, solo después de aceptar cookies (dentro de la función px() del aviso de cookies, junto al píxel de Meta). No carga en /admin. La política de privacidad (sección 6 y párrafo de píxeles) ahora menciona Google Analytics.
POR QUE: Ariel pidió configurar Google Analytics.
COMO SE HIZO: reemplazo exacto tras fbq('track','PageView') en las páginas con el aviso; anonymize_ip activado.
QUE FALTA: GA tarda hasta 48 h en mostrar datos; verificar en Informes > Tiempo real tras aceptar cookies; la cartilla (cartilla.enc) no lleva gtag.

## 16 nov 2026 - sitio.pak (Analytics: eventos del embudo)
QUE SE HIZO: los eventos propios del sitio (wa, sub, precio, ebook, cargo, entrar, guia, quiz) ahora también se envían a Google Analytics 4 con los nombres whatsapp_click, generate_lead, view_pricing, ebook_click, cargo_click, login_click, guia_click, quiz_start. Solo si el visitante aceptó cookies (gtag existe).
POR QUE: medir el embudo (visita, precio, WhatsApp, suscripción) para el plan de marketing 360 que pidió Ariel.
COMO SE HIZO: función ev() del script /*visitas*/ ampliada con un mapa GM; 904 páginas.
QUE FALTA: en GA4 (Administrar > Eventos) marcar generate_lead y whatsapp_click como "evento clave" cuando aparezcan; precio visible en la portada ("Desde $40.000 ... hasta $55.000") no coincide con la escala 35/40/45/50 mil decidida: revisar antes de agregar esquema Offer. Siguientes etapas propuestas: ventana de salida con ebook, secuencia de correos por concurso, esquema Course/Offer, contenidos SEO.

## 16 nov 2026 - sitio.pak (ventana de salida con ebook gratis)
QUE SE HIZO: ventana "Antes de irte: ebook gratis" en computador (puntero fino y ancho >= 900 px): aparece una sola vez por sesión cuando el mouse sale por arriba de la página, pasados 15 s y nunca encima del aviso de cookies. Las páginas de Docentes ofrecen el ebook docente; las demás, el de Procuraduría. Se cierra con Escape, la X o "No, gracias". Eventos GA4: exit_offer_view y exit_offer_click.
POR QUE: captar leads de visitantes que se van (plan de marketing 360 de Ariel). No sale en /admin, /acceso, pagar, privacidad, términos, páginas de ebook ni 404; no aparece en celular.
COMO SE HIZO: <script id="ce-exit"> antes del script /*visitas*/ en 904 páginas (fuente /tmp/cce/fix9/mkt.js). Probado con Playwright (abre y cierra con Escape).
QUE FALTA: medir exit_offer_click vs exit_offer_view en GA4; si molesta, quitar el script con id ce-exit. Barra con fecha de prueba y secuencia de correos pendientes.

## 16 nov 2026 - sitio.pak + php.pak (buscadores más grandes, fcss v=7)
QUE SE HIZO: en computador (>= 861 px) el buscador de cargos de la portada y de los concursos (DIAN, Procuraduría, CAR, Docentes) ocupa una fila completa (antes ~300 px, ahora 800-900 px) y los filtros van debajo; en /concursos el buscador ocupa todo el ancho; en pagar el campo "Verifica tu nivel" va a ancho completo. Celular no cambia.
POR QUE: Ariel pidió que ninguna barra de búsqueda sea pequeña.
COMO SE HIZO: reglas nuevas al final del bloque CSSMENU de acceso/api.php (?a=fcss) y enlace subido a v=7 en todas las páginas.
QUE FALTA: probar en el sitio publicado #mnQ (buscador del menú), #dpEmpQ (docentes) y la búsqueda de glosario; la cartilla (cartilla.enc) no se tocó.

## 16 nov 2026 - sitio.pak + php.pak (Rocky: el índice de cargos sale de chat_core.php a un archivo aparte)
QUE SE HIZO: Rocky seguía sin encontrar «234-2026» ni «Sustanciador 4SU-11» en el sitio publicado (probado con el chat real). El índice de cargos (386 KB) se movió de chat_core.php (que había pasado de 311 KB a 704 KB) al archivo rocky-idx.json en la raíz del sitio; ce_bot_idx() ahora lo lee con dirname(__DIR__).'/rocky-idx.json'. chat_core.php vuelve a ~314 KB.
POR QUE: sospecha: el actualizador del servidor no estaba instalando el chat_core.php de 704 KB (el resto de acceso/api.php sí se actualizó); no se pudo confirmar sin ver el servidor.
COMO SE HIZO: mismo contenido del índice, ahora en site/rocky-idx.json (sitio.pak) y chat_core_v2.php (php.pak). Probado en local con las mismas consultas.
QUE FALTA: verificar en el chat real «234-2026» y que /rocky-idx.json se sirva (si el actualizador no instala .json, usar otra extensión o ce_data). Si sigue fallando, mirar ce_data/update.log en el servidor.

## 16 nov 2026 - php.pak (Rocky: el índice vuelve dentro de chat_core.php, comprimido)
QUE SE HIZO: rocky-idx.json no se podía leer desde PHP en el servidor (el chat decía "no encuentro coincidencias" para «234-2026»). El índice de cargos va ahora dentro de chat_core.php, comprimido con gzcompress y base64 (47 KB; el archivo queda en 361 KB). ce_bot_idx() lo descomprime. rocky-idx.json queda sin uso (el servidor lo bloquea con 403); se puede borrar de sitio.pak.
POR QUE: pruebas contra el chat real (POST a /acceso/chat.php con ok=1): el servidor tarda unos 8 a 10 minutos en instalar los cambios de php.pak.
COMO SE HIZO: mismo índice; verificado en local con las mismas consultas.
QUE FALTA: probar de nuevo «234-2026», «2000» y «246054» en el chat real cuando el servidor instale este paquete.

## 17 nov 2026 - sitio.pak (espacio del canal de WhatsApp en todas las páginas)
QUE SE HIZO: en el pie de las 904 páginas con footer (todas las públicas) hay una tarjeta "Únete a nuestro canal de WhatsApp" con el botón "Unirme al canal" (https://whatsapp.com/channel/0029VbECnRe8qJ02MemQ2246, se abre en pestaña nueva) y un enlace "Canal de WhatsApp" en la fila de enlaces del pie. Evento GA4 channel_click al pulsar el botón (solo si hay consentimiento).
POR QUE: Ariel pidió un espacio para el canal de WhatsApp en todas las páginas de la web.
COMO SE HIZO: bloque <div class="chn" id="canalwa"> al inicio de footer .fi, CSS al final del <style> de footer.cefoot, reemplazo exacto en cada página (probado en escritorio y celular, sin desbordes).
QUE FALTA: no se tocó la cartilla (cartilla.enc) ni el panel de acceso (sin footer). Si se agrega otra variante de footer, copiar el bloque #canalwa.

## 17 nov 2026 - sitio.pak (noticia DIAN 2676: resultados el 20 de noviembre y reclamaciones del 23 al 27)
QUE SE HIZO: nueva noticia guias/noticia-dian-2676-resultados-20-noviembre-reclamaciones (NewsArticle, tarjeta social og propia, botones de compartir con resumen + "✍️ concursosdelestado.com"). Es la noticia principal de /guias/noticias-concursos. La nota del 16 de nov lleva aviso de actualización enlazando a la nueva. Sitemap actualizado.
POR QUE: aviso oficial de la CNSC y la Fundación Universitaria del Área Andina (publicado el 12 de nov 2026): resultados de la prueba escrita el 20 de noviembre; reclamaciones solo por SIMO del 23 al 27 de noviembre hasta las 23:59. El texto original traía erratas ("2667", "2025"); se usó 2676 y 2026.
COMO SE HIZO: /tmp/cce/fix9/pack26.py (pack2 con archivos extra).
QUE FALTA: fecha de respuesta a reclamaciones (la CNSC la informará); actualizar el 20 de noviembre con los resultados.

## 17 nov 2026 - php.pak (bot de WhatsApp: enlaces con https y respuestas más cortas)
QUE SE HIZO: en acceso/chat_core.php el enlace de privacidad del prompt pasa de "www.concursosdelestado.com/privacidad" a "https://www.concursosdelestado.com/privacidad.html"; y en las reglas del canal WhatsApp se agregan: enlaces siempre con https://, respuesta corta sin repetir datos ya dados, un solo enlace principal por mensaje, sin rayas largas.
POR QUE: en una conversación real el bot mandó http://www.concursosdelestado.com/privacidad (WhatsApp completa con http los www sin esquema) y un mensaje largo cortado con "Leer más" que escondía la pregunta por el correo.
COMO SE HIZO: reemplazo exacto en chat_core.php (pack27.py); php -l y chat_prompt('wa') verificados en local.
QUE FALTA: si la respuesta del screenshot vino de la IA de WhatsApp Business (etiqueta "IA") y no de este bot, hay que ajustar sus instrucciones en la app de WhatsApp Business.

## 18 nov 2026, 19:00 — Cartilla ESE 2 (Empresas Sociales del Estado), nivel asistencial, solo para revisión del administrador
- Nuevo concurso "ESE" con el mismo entorno de CAR y Procuraduría: 475 OPEC asistenciales, ficha del manual de funciones, temas ordenados por la OPEC elegida, 13 capítulos (prueba + 12 de salud), quiz, simulacro y fichas.
- Servidor (php.pak): acceso por código `ese-asi` / `ese-tec` / `ese-pro` / `ese-todos`; módulos s-ese y d-ese servidos solo a quien los pagó; avance sincronizado por código (claves `ese-env-ese-*-v1`); entrada en Mi panel; precios 40.000 / 45.000 / 50.000.
- Aún sin página pública, sin enlace en el sitio ni pago en línea: solo el administrador ve la tarjeta ESE en el selector.
- Pendiente: capítulos de segunda ola, niveles técnico y profesional, página pública y pago.
- Para volver atrás: revertir este commit.

## 18 nov 2026, 20:20 — cartilla.enc (CAR, tanda 1: simulacro en casos por funciones; cambia el motor s-car)
QUE SE HIZO
- CAR: 8 casos nuevos de 3 preguntas (24 preguntas, 3 opciones, etiqueta NUEVO), escritos con funciones reales de las ofertas OPEC y la misión de la CAR. Cada caso quedó dentro de su capítulo temático: ambiental (Ley 1333 flagrancia; visitas técnicas Ley 99), contratacion (supervisión Ley 1474), mipg (peticiones Ley 1437 art. 14), documental (archivos de gestión; entrega por traslado, Ley 594), transparencia (Ley 1712), institucional (misión, Ley 99 art. 31).
- Lección nueva en "prueba": "Las funciones que más se repiten en la oferta de las CAR" (tabla con el número de empleos por función).
- Motor s-car: el simulacro con cronómetro usa solo preguntas con sim:1, por casos completos, de los capítulos que prio() marca para el empleo del cliente (primero A, luego M). Muestra "Caso · pregunta 1 de 3". Las preguntas sim no salen en fichas. Soporta NUEVO en lecciones, preguntas y capítulos. Filtro de nivel por pregunta (campo nv). Al cambiar de convocatoria se reconstruye.
POR QUE
- Claudia pidió que el simulacro de todos los concursos sea solo sobre funciones del empleo y misionalidad, en casos de 3 preguntas, con el mismo sistema de DIAN y Procuraduría: los casos viven en su capítulo y se ven según la ruta del empleo.
COMO SE HIZO
- Parche sobre la cartilla.enc publicada: inserción de texto en d-car (NO re-serializar: mezcla escapes) con comprobación de igualdad contra el JSON original; regeneradas br-car y br-dcar y CE-PUB (regla: sin copia br los clientes no reciben el cambio). Probado en celular con 5 empleos, sin errores.
INSTRUCCIONES PARA OTRA IA
- No muevas los casos de capítulo: el simulacro depende de que cada caso esté en el capítulo de su tema. Para añadir casos: agrégalos a b.preguntas del capítulo con caso, sim:1, nuevo:true y nv si es de un nivel. Si editas s-car o d-car, regenera su br-* y CE-PUB.
QUE FALTA
- Pocos casos: algunos empleos profesionales quedan con 2 casos (6 preguntas). Tanda 2: más casos en ambiental, biodiversidad, residuos-aire, planeación, talento humano, TIC y SST; lecciones de los 5 capítulos sin ellas; preguntas de 4 a 3 opciones; avance en servidor; plan de estudio con el aplazamiento.

## 18 nov 2026, 20:45 — sitio.pak (página del concurso CAR: datos de la CNSC, simulacro gratis de 30 y fecha de actualización)
QUE SE HIZO
- concursos/corporaciones-autonomas-regionales.html: "Última actualización: 18 de noviembre de 2026" (visible) y dateModified del JSON-LD; sitemap lastmod de esa página.
- Datos tomados del micrositio oficial de la CNSC (avisos del 8 y 16 de septiembre): OPEC publicada el 8 sept con 1.383 empleos y 1.832 vacantes (se deja también el 1.389 de SIMO al 20 oct); derechos de participación 2026 $87.550 profesional y $58.400 técnico y asistencial; el aplazamiento rige hasta que se levanten las medidas del Decreto Legislativo 1384, vigencia hasta el 31 dic 2026; sin nueva fecha de inscripción; Guía de Orientación sin publicar (sección Guías vacía).
- La sección "Evaluación de muestra: diez preguntas" pasa a "Simulacro gratis: 30 preguntas de CAR" con botón a /acceso/?registro=1&c=car (el catálogo gratis ya dice 30 preguntas); se corrige también la pregunta frecuente y su JSON-LD. El contenedor #qcard queda oculto porque el script de la página lo usa.
- "Qué incluye" suma Simulacro en casos, Mi cargo y Plan de estudio. Sección nueva "Cómo practicas la prueba funcional en la cartilla" (casos de 3 preguntas, funciones del empleo, razón de cada respuesta).
POR QUE
- Claudia pidió revisar la página de CAR contra la CNSC, ofrecer el simulacro gratis de 30 (no 10 preguntas), reflejar lo nuevo de la cartilla (tanda 1 CAR) y mostrar la fecha de la última actualización.
COMO SE HIZO
- Parche sobre el sitio.pak vigente (/tmp/work/car/pg/edit.py, reemplazos exactos con asserts), solo cambian esa página y sitemap.xml; paquete firmado con HMAC (site) y verificado. Probado en celular (400 px) sin desbordes ni errores.
QUE FALTA
- Las páginas de DIAN y Procuraduría siguen con "diez preguntas" de muestra; llevan la misma regla del simulacro gratis. La imagen/maqueta no se mostró antes (cambio de texto y una sección). Si la CNSC publica nueva fecha de inscripción o la Guía de Orientación, actualizar aquí.

## 18 nov 2026, 21:10 — cartilla.enc (CAR, tanda 2: 15 casos nuevos para el simulacro)
QUE SE HIZO
- CAR: 15 casos nuevos de 3 preguntas (45 preguntas, 3 opciones, etiqueta NUEVO, sim:1) en los capítulos de su tema: control-interno, transparencia, planeacion, contratacion, documental, participacion, gobierno-digital, ambiental-fondo, biodiversidad, residuos-aire, riesgo-clima, mipg y ambiental. Los casos de normas citan articulos reales (Ley 87, 1437, 1474, 1712, 152, 80, 1150, 594, 1757, 1581); los ambientales se apoyan en las lecciones de la cartilla.
- Opciones balanceadas en longitud (maximo/minimo <= 1,45) para que la correcta no sea la mas larga.
- Sin cambios de motor: solo datos d-car (br-dcar y CE-PUB regenerados).
POR QUE
- En la tanda 1 algunos empleos quedaban con 6 preguntas en el simulacro; Claudia pidio llegar a 10 o mas casos por empleo con el mismo sistema de DIAN/Procuraduria.
COMO SE HIZO
- Parche sobre la cartilla.enc publicada (/tmp/work/car/t2/apply2.py): insercion de texto en d-car con put()/arr_end y comprobacion de igualdad contra el JSON original. Probado con 36 empleos reales de la OPEC a 400 px, sin errores.
INSTRUCCIONES PARA OTRA IA
- Igual que la tanda 1: no muevas los casos de capitulo ni re-serialices d-car; tras editar regenera br-dcar y CE-PUB.
QUE FALTA
- Con la tanda 2 el simulacro trae hasta 15 preguntas; algunos empleos (profesional administrativo/juridico, asistencial de contratacion y talento humano) quedan con 9. Falta tanda 3 en capitulos juridico, administrativo y asistencial.

## 18 nov 2026, 22:00 — cartilla.enc (CAR, tanda 3: 6 casos mas para el simulacro)
QUE SE HIZO
- CAR: 6 casos nuevos de 3 preguntas (18 preguntas, 3 opciones, NUEVO, sim:1) en los capitulos disciplinario, talento-humano, transparencia (terminos de peticiones), sst, contratacion (supervision, Ley 1474) y participacion (terminos de tutela, Decreto 2591). Solo datos d-car; br-dcar y CE-PUB regenerados.
POR QUE
- Cuatro perfiles (profesional administrativo y juridico, asistencial de contratacion y de talento humano) quedaban con 9 preguntas en el simulacro.
COMO SE HIZO
- Igual que la tanda 2 (/tmp/work/car/t2/apply3.py): insercion de texto con put()/arr_end y comprobacion de igualdad. Los capitulos n-* no existen en d-car (solo en las listas de niveles): los casos van en capitulos reales. Probado con 36 empleos a 400 px: entre 12 y 15 preguntas, sin errores.
INSTRUCCIONES PARA OTRA IA
- No muevas los casos de capitulo ni re-serialices d-car; tras editar regenera br-dcar y CE-PUB.
QUE FALTA
- Cotejar con los textos las normas citadas de memoria (Decretos 1083/2015, 1045/1978, 2591/1991, Ley 1755/2015, Res. 1401/2007). El simulacro muestra maximo 15 preguntas.

## 18 nov 2026, 22:15 — php.pak + cartilla.enc (admin: simulacros y cursos gratis que hizo cada cuenta gratuita)
QUE SE HIZO
- php.pak (acceso/lib.php, op crm_actividad): ademas de 'act' devuelve 'gr': por cada cuenta con accesos_admin[fp].gr, la lista de {s slug, n nombre del catalogo gratis, a abrio, f/k veces terminado, p mejor %, t ultimo}. 'act' no cambia (crm_nivel_auto sigue igual).
- cartilla.enc (panel admin, llenarAct): debajo del cargo muestra "🧪 <simulacro>: terminó N veces · mejor X %" o "lo abrió, sin terminar" (hasta 4 lineas). Si la cuenta solo tiene simulacros no sale "Aún no ha elegido cargo". Variable GRA (GR ya existe en ese script).
POR QUE
- Claudia necesita saber, en la fila de cada codigo gratuito del admin, que simulacros hicieron los clientes.
COMO SE HIZO
- Parche de texto sobre lib.php dentro de php.pak (firma 'php', magic CP1) y sobre el panel de cartilla.enc con asserts de reemplazo unico; CE-PUB recalculado. JS verificado con node --check; sin prueba con datos reales.
INSTRUCCIONES PARA OTRA IA
- Los datos vienen de ce_gratis_visto (la pagina gratis avisa abre/fin con el % del simulacro). Solo se guarda mejor % y numero de terminaciones, no cada intento.
QUE FALTA
- Historial por intento (fecha y nota) si Claudia lo pide: guardarlo en accesos_admin[fp].gr[slug].h.

## 18 nov 2026, 22:20 — cartilla.enc (admin: ESE en la ventana "Concursos activos")
QUE SE HIZO
- Panel admin, accion cc ("Concursos activos"): la lista OP suma ESE · asistencial, técnico y profesional (ese-asi, ese-tec, ese-pro). PC/FC/CL, CONCS, el selector de crear códigos y ce_niv_concursos ya soportaban ese-*; solo faltaba la lista de la ventana.
POR QUE
- Claudia vio que al administrar un usuario no se podia marcar ESE como concurso pagado.
COMO SE HIZO
- Reemplazo unico con assert sobre la cartilla.enc publicada; CE-PUB recalculado; JS con node --check.
QUE FALTA
- Probar con una cuenta real. El curso de concejales aun no es un concurso del sistema.

## 18 nov 2026, 22:30 — php.pak + cartilla.enc (admin: seccion "Avance y animo" de los clientes)
QUE SE HIZO
- php.pak (acceso/lib.php): op nueva crm_avance. Por cada cliente de pago activo (no gratis, no fusionado) devuelve, por concurso (dian, pgn, car, ese, doc): temas hechos/total, % (misma formula del panel del cliente: plan2676-resumen + temas), simulacros y mejor %, ultima actividad (t de progreso), nivel; ademas minutos de estudio de 7 dias (ce_tiempo_de), visitas e ingreso. Solo lectura.
- cartilla.enc (panel admin): funcion avanceCli, SEC.avc y menu Clientes → "📈 Avance y ánimo". Tabla con filtros Estancados (7+ dias sin estudiar) / Sin empezar / Avanzando / Todos, busqueda y marcas. Redactor con 3 plantillas (tuteo, "Hola {nombre}, te escribo de Concursos del Estado...") y marcadores {nombre} {concurso} {avance} {lecciones} {dias}; vista previa (msg_previa), prueba (msg_enviar prueba) y envio por tandas por msg_enviar con lista (no comercial: respeta bajas, limite diario y tanda).
POR QUE
- Claudia necesita ver el avance de los clientes en sus cursos para animarlos por correo a que avancen.
COMO SE HIZO
- Parche de texto sobre lib.php en php.pak (firma 'php', CP1) y sobre el panel de cartilla.enc con asserts de reemplazo unico; CE-PUB recalculado. JS con node --check y prueba en navegador con servidor simulado (filtros, marcas, items enviados, plantillas). No probado con datos reales.
INSTRUCCIONES PARA OTRA IA
- No se tocan las plantillas del email marketing existente; esta seccion usa la via de lista de msg_enviar. El remitente es el de smtp.json (se muestra en pantalla); la preferencia es envios@concursosdelestado.com.
QUE FALTA
- Revisar vista previa y enviar prueba antes del primer envio masivo. Posible: historial de correos de animo por cliente para no repetir en pocos dias, y envio programado.

## 18 nov 2026, 22:40 — php.pak + cartilla.enc (ranking anonimo por concurso y nivel; textos "se guarda en tu cuenta")
QUE SE HIZO
- php.pak (acceso/lib.php): ce_rank_def/ce_rank_pct/ce_rank_tabla/ce_rank_de. Para cada cliente de pago activo con avance (>=1 leccion) calcula el % por concurso (dian, pgn, car, ese, doc) con la misma formula del panel (plan2676-resumen + temas) y agrupa por concurso|nivel (accesos_admin.niveles). Tabla en cache 10 min (ce_data/ranking.json); el % del propio cliente se calcula al momento. Minimo CE_RANK_MIN=20 aspirantes con avance: si hay menos, estado "pronto". Cambio semanal guardado en accesos_admin[fp].rk[concurso] {p,t,d}. Nunca se devuelven nombres ni codigos de otros.
- php.pak (acceso/api.php): ops de cliente rank, rank_off y rank_on (accesos_admin[fp].rk_off; excluye del ranking y oculta el puesto; borra el cache).
- php.pak (panel Mi panel, barra .cb): chip #cbk "Puesto P de N · concurso nivel · X % superior ▲d" y popover #rkp (promedio del grupo, lecciones para superar, enlace "No quiero aparecer"/"Volver a aparecer"). Se pinta con textContent.
- cartilla.enc: textos que decian "se guarda en este navegador" pasan a "se guarda en tu cuenta" (DIAN, Procuraduria, CAR, ESE, Docentes, plan de estudio, correo de acceso); br-dian/br-pgn/br-car regenerados y CE-PUB recalculado. Se dejo "el codigo queda guardado en este navegador" (es cierto).
POR QUE
- Claudia quiere que cada cliente vea su posicion anonima frente a otros aspirantes de SU concurso para motivarlos, y exige que el avance de todos los concursos este en el servidor (ya se sincroniza por codigo con op sync; la lista blanca incluye los cinco concursos y plan2676-*).
COMO SE HIZO
- Parches de texto con asserts sobre lib.php/api.php dentro de php.pak (firma 'php', CP1) y sobre cartilla.enc. Logica PHP probada con 25 aspirantes simulados (puesto, off, gratis=nada) y JS del chip con node --check; cartilla cargada sin errores. No probado con clientes reales.
INSTRUCCIONES PARA OTRA IA
- El ranking solo usa avance en servidor (progreso). Si se agrega un concurso nuevo: sumarlo a ce_rank_def, a la lista blanca de claves de op sync (api.php) y al regex del chip (rank() en la barra), y asegurar que su cartilla escribe plan2676-resumen {d,n}.
- Abogados (examen de Estado) aun no guarda avance por lecciones: no entra al ranking.
QUE FALTA
- Agregar a la politica de privacidad una linea sobre el ranking anonimo (usa avance de estudio); Claudia debe aprobar la redaccion.
- Revisar con clientes reales que el chip se vea bien en celular y que el grupo minimo de 20 sea el adecuado.

## 18 nov 2026, 22:50 — cartilla.enc + sitio.pak (filtro por concurso en Avance y animo; politica de privacidad con avance y ranking)
QUE SE HIZO
- cartilla.enc (panel admin, avanceCli): desplegable "Todos los concursos" en Avance y animo. Al elegir un concurso solo salen los clientes de ese concurso; los grupos Estancados/Sin empezar/Avanzando se recalculan con la actividad de ese concurso (no la general) y los correos usan el % y las lecciones de ese concurso. Probado en navegador con servidor simulado.
- sitio.pak (privacidad.html): se agrega el avance de estudio a "Que datos tratamos" y, en "Para que los usamos", guardar el avance, escribir para animar y mostrar un ranking anonimo (sin nombre ni codigo, con opcion de salirse). Fecha "Ultima actualizacion: 18 de noviembre de 2026".
POR QUE
- Claudia necesita filtrar por concurso al animar clientes; y el ranking anonimo usa el avance de estudio, por lo que la politica debe decirlo (Ley 1581).
COMO SE HIZO
- Reemplazos exactos con asserts sobre la cartilla.enc y el sitio.pak vigentes (firma 'site'); CE-PUB recalculado.
INSTRUCCIONES PARA OTRA IA
- Si se cambia el ranking o se guardan mas datos de estudio, actualizar privacidad.html.
QUE FALTA
- Nada nuevo; ver pendientes de la entrada del ranking (probar con clientes reales).

## 2026-11-18 · Ranking y avance en todos los concursos (Abogados)
- Qué: el curso de Abogados (Examen de Estado) ahora guarda su avance en el servidor (clave ce_abog_v1, entra al sync permitido) y participa en el ranking anónimo y en "Avance y ánimo".
- Por qué: el ranking y el avance debían aparecer a todos los concursantes de todos los concursos y cargos; Abogados era el único que guardaba solo en el navegador.
- Detalle: porcentaje = lecciones hechas / total (_n); chip del panel incluye abog; al abrir el curso se recupera lo guardado en la cuenta.

## 2026-11-18 · Panel: CAR/ESE/Docentes abrian el selector "Elige tu cartilla"
- Qué: la cartilla ahora respeta la ruta (#/car-..., #/ese-..., #/doc-...) que manda "Abrir curso" del panel tambien en cuentas que combinan concursos (antes solo si la cuenta no tenia DIAN/PGN); el boton de ESE ahora manda su ruta.
- Regla: solo se abre el nivel que el cliente pago (se toma de sus niveles); si pide un nivel que no tiene, abre el suyo. Nada se muestra sin pago de ese concurso y nivel.
- Por qué: con DIAN/PGN + CAR/ESE el cliente veia el selector en vez de su curso.

## 2026-11-18 · Ranking sin minimo y vista previa del administrador
- Qué: CE_RANK_MIN pasa de 20 a 1 (el puesto sale desde el primer aspirante con avance, siempre anonimo); el admin ve el chip del ranking en cada concurso (vista de ejemplo con el tamano real del grupo).
- Por qué: Claudia pidio que el ranking aparezca aunque no haya 20 personas; como admin no veia nada porque la operacion solo respondia a clientes con codigo.

## 2026-11-18 · Admin, tanda 1: menu nuevo en la barra azul
- Que: el menu del admin pasa de barra lateral (7 grupos) a la misma barra azul de arriba con 5 grupos: Hoy, Clientes, Ventas, Comunicacion y Sistema. Cada grupo abre su lista debajo del boton. Se agrega el buscador "Buscar pantalla". En celular se conserva la barra inferior (ahora con 5 botones).
- Orden: Clientes (Codigos, Avance y animo, Respuestas, Revision y respaldo); Ventas (Embudo, Pagos, Contabilidad); Comunicacion (Email marketing, Marketing, Publicidad, Anuncios); Sistema (Estadisticas, Pegar datos, Base de datos, Migracion, Cumplimiento normativo, Entornos de prueba).
- Por que: ordenar el panel y que se vea mas serio. Solo cambia el lugar de los botones: las 18 pantallas existentes siguen llamando a las mismas funciones.
- Verificacion: se abrio cada uno de los 18 enlaces del menu y el buscador en una prueba; el resto del archivo es identico al publicado. Los contadores se conservan en Clientes (por vencer) y Ventas (seguimientos).
- Pendiente (tandas siguientes): rediseno de pantallas de Clientes/Ventas y luego Comunicacion/Sistema; pantalla Marketing con decisiones; seguimiento por campana (utm_campaign).

## 2026-11-18 · Admin, tanda 2: tema sobrio
- Que: nueva apariencia de todo el panel de administracion (tablas con encabezado en mayuscula pequena, tarjetas de cifras, botones con borde fino y boton principal azul oscuro, etiquetas cuadradas, titulos). Solo CSS dentro de .acc-ov; no toca la pagina del cliente.
- Por que: darle al panel una imagen mas seria, como en las maquetas aprobadas.
- No cambia funciones ni datos. El resto del archivo es identico al publicado (verificado).
- Pendiente: Codigos con pestanas por estado, menu por fila y ficha lateral (conservando correo, celular y vencimiento editables); pantalla Marketing con decisiones; seguimiento por campana.
