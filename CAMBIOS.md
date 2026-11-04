
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
