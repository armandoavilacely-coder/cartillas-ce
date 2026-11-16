# -*- coding: utf-8 -*-
# Contenido del ebook. Se ejecuta dentro de build.py (usa page, T, NO, SI, EX, lg).

# 1. Portada
page('', '''<div class="br"><div class="ic">%s</div><div><b>CONCURSOS</b><em>DEL ESTADO</em></div></div>
<div class="badge">EBOOK GRATIS</div>
<h1>Guía de estudio<br><span>Concurso docente 2026</span></h1>
<p class="sub">Qué estudiar para la prueba que decide: los cuatro componentes, las normas que todo docente debe dominar y casos resueltos paso a paso.</p>
<div class="chips"><span>Docentes de aula</span><span>Docente orientador</span><span>Rector</span><span>Coordinador</span><span>Director rural</span></div>
<div class="cart">%s</div>
<div class="stats"><div><b>4</b>componentes de la prueba explicados</div><div><b>10</b>textos de norma citados al pie de la letra</div><div><b>7</b>casos resueltos con su porqué</div></div>
<div class="foot"><div class="u">concursosdelestado<span>.com</span></div><div class="d">Edición de noviembre de 2026<br>Con el Anexo técnico de la CNSC</div></div>''' % (lg(70,66),cover_scene()), 'cover')

# 2. Antes de empezar
page('Antes de empezar', ic='libro', body='''<p class="kick">Antes de empezar</p>
<h1>Cómo usar esta guía</h1>
<p class="lead">Esta guía es para quienes se preparan para el concurso de docentes y directivos docentes 2026 de la Comisión Nacional del Servicio Civil (CNSC). Te muestra qué se evalúa y cómo estudiarlo con criterio, sin perder tiempo en lo que no suma.</p>
<p>Cada tema viene con la misma estructura, para que sepas siempre dónde mirar:</p>
<div class="grid2">
<div class="box term" style="margin:0"><span class="lbl">Término</span>La palabra clave, definida en lenguaje claro.</div>
<div class="box norma" style="margin:0"><span class="src">La norma</span>El texto de la ley o del decreto, citado al pie de la letra.</div>
<div class="box simple" style="margin:0"><span class="lbl">En palabras simples</span>Qué significa la norma para tu trabajo en el colegio.</div>
<div class="box exam" style="margin:0"><span class="lbl">Para la prueba</span>Lo que más se pregunta y cómo reconocerlo.</div>
</div>
<h2>Lo que vas a encontrar</h2>
<table><tr><th>Tema</th><th style="width:20mm">Página</th></tr>
<tr><td>La prueba que decide: cuánto pesa cada prueba</td><td>{p:o1}</td></tr>
<tr><td>Los cuatro componentes de la prueba de aptitudes</td><td>{p:o2}</td></tr>
<tr><td>Lectura crítica y razonamiento cuantitativo</td><td>{p:lec} y {p:cua}</td></tr>
<tr><td>Competencias blandas: ética y ciudadanía</td><td>{p:bla}</td></tr>
<tr><td>Normas que todo docente debe dominar: función docente, PEI, evaluación, convivencia e inclusión</td><td>{p:o3} a {p:inc}</td></tr>
<tr><td>Tu cargo según el Manual de Funciones</td><td>{p:o4}</td></tr>
<tr><td>Psicotécnica y entrevista</td><td>{p:psi}</td></tr>
<tr><td>Siete casos para practicar y sus respuestas razonadas</td><td>{p:o5} a {p:resp}</td></tr>
<tr><td>Plan de estudio y glosario</td><td>{p:plan} y {p:glo}</td></tr></table>
<p class="tip">Basada en el Anexo técnico de la CNSC y las normas vigentes a noviembre de 2026.</p>''')

# 3. Pesos
page('', opener('Capítulo 1','La prueba que decide','Cuatro pruebas forman tu puntaje final, pero una sola decide si sigues: la de aptitudes y competencias básicas. Así se reparte el puntaje.',['Cuánto pesa cada prueba para docentes y directivos','Qué significa que una prueba sea eliminatoria','El puntaje mínimo que debes alcanzar'],pesos_chart(),'#2A6FC4'),'op',key='o1')
page('La prueba que decide', ic='cargo', body='''<p class="kick">Capítulo 1</p>
<h1>La prueba que decide</h1>
<p class="lead">No todas las pruebas pesan igual. Saber cuánto vale cada una te dice dónde poner el esfuerzo.</p>
<table><tr><th>Prueba</th><th>Carácter</th><th>Docentes</th><th>Directivos</th></tr>
<tr><td><b>Aptitudes y competencias básicas</b></td><td>Eliminatoria</td><td><b>55 %</b></td><td><b>55 %</b></td></tr>
<tr><td>Psicotécnica</td><td>Clasificatoria</td><td>5 %</td><td>10 %</td></tr>
<tr><td>Valoración de antecedentes</td><td>Clasificatoria</td><td>30 %</td><td>25 %</td></tr>
<tr><td>Entrevista</td><td>Clasificatoria</td><td>10 %</td><td>10 %</td></tr></table>
''' + T('Prueba eliminatoria', 'La que debes aprobar con un puntaje mínimo para seguir en el concurso. Si no lo alcanzas, sales del proceso.') +
T('Prueba clasificatoria', 'La que no te saca del concurso, pero suma puntos y define tu puesto en la lista de elegibles.') +
NO('Anexo técnico 2026 de la CNSC, numeral 2.2, nota 1', 'Los aspirantes que no superen el mínimo aprobatorio (70.00 puntos) para Directivos Docentes y (60.00) para Docentes, en las Pruebas de Aptitudes y Competencias Básicas […] no continuarán en el proceso de selección por tratarse de una prueba de carácter eliminatorio.') +
SI('La prueba de aptitudes es la puerta: pesa más de la mitad y, si no llegas a <b>60 puntos (docentes)</b> o <b>70 (directivos)</b>, nada de lo demás cuenta. Los puntajes se toman con dos decimales <b>truncados</b>, sin redondear: 59,99 no pasa.') +
EX('Tu prioridad número uno es aprobar la eliminatoria. La psicotécnica y la prueba de aptitudes se presentan <b>el mismo día y en la misma sesión</b>.'))

# 4. Cuatro componentes
page('', opener('Capítulo 2','La prueba de aptitudes, componente por componente','La prueba eliminatoria tiene cuatro componentes. Los tres primeros son iguales para todos los cargos; el cuarto cambia según tu cargo.',['Lectura crítica: lo que el texto sostiene','Razonamiento cuantitativo sin calculadora','Competencias blandas: cómo razonar un dilema','Las normas que todo docente debe dominar'],'<div class="i4">'+''.join('<div>%s<b>%s</b></div>'%(icon(k,90),t) for k,t in [('leer','Lectura crítica'),('num','Razonamiento cuantitativo'),('eti','Competencias blandas'),('ped','Disciplinar y pedagógico')])+'</div>','#12A05A'),'op',key='o2')
page('Prueba de aptitudes', ic='ped', body='''<p class="kick">Capítulo 2</p>
<h1>Los cuatro componentes de la prueba de aptitudes</h1>
''' + NO('Anexo técnico 2026, numeral 2.1. Prueba de aptitudes y competencias básicas', 'Tiene por objeto valorar los niveles de conocimientos de la disciplina, habilidades, destrezas, aptitudes que demuestren los aspirantes […] y contendrá los componentes de: 1. Lectura crítica; 2. Razonamiento cuantitativo; 3. Valoración de competencias blandas como liderazgo, ética, trabajo en equipo y ciudadanía; 4. Conocimientos disciplinares de la formación requerida para el empleo, y las competencias pedagógicas para evaluar, formar y enseñar.') + '''
<div class="grid2">
<div class="card"><h3><span class="num">1</span>Lectura crítica</h3><p>Entender, interpretar y evaluar textos del trabajo escolar: circulares, actas, informes y normas.</p></div>
<div class="card"><h3><span class="num">2</span>Razonamiento cuantitativo</h3><p>Promedios, porcentajes, proporciones y tablas de un colegio, resueltos a mano: no se permite calculadora.</p></div>
<div class="card"><h3><span class="num">3</span>Competencias blandas</h3><p>Liderazgo, ética, trabajo en equipo y ciudadanía, evaluados con dilemas y situaciones del colegio.</p></div>
<div class="card"><h3><span class="num">4</span>Disciplinar y pedagógico</h3><p>El saber de tu área o cargo y las normas para evaluar, formar y enseñar: evaluación, convivencia, inclusión, PEI.</p></div>
</div>
''' + SI('Los componentes 1 a 3 son comunes a todos los cargos: es la base que todos deben dominar. El componente 4 cambia según tu cargo: no estudia lo mismo un docente de matemáticas que un rector.') +
EX('La prueba está <b>«orientada a la aplicación de saberes»</b>: no te preguntan de memoria qué dice un artículo, sino qué haces en una situación del colegio aplicando la norma. Por eso, en esta guía todos los ejemplos son casos.'))

# 5. Lectura crítica
page('Componente 1', key='lec', ic='leer', body='''<p class="kick">Componente 1</p>
<h1>Lectura crítica: lo que el texto sostiene</h1>
<h2>Los tres niveles de lectura</h2>
<div class="art" style="width:82%">''' + niveles_lectura() + '''</div><p class="tip"><b>Literal:</b> lo que dice con esas palabras. <b>Inferencial:</b> lo que se deduce con lógica. <b>Crítico:</b> si el argumento es sólido y qué evidencia falta.</p>
<h2>Ejemplo resuelto</h2>
<div class="card"><p><i>«La rectora informa que, desde el lunes, la jornada de grado 9.º terminará a la 1:00 p. m. porque el transporte rural sale a las 2:00 p. m. y los estudiantes llegan a casa de noche».</i></p>
<ul><li><b>Literal:</b> ¿a qué hora termina 9.º? A la 1:00 p. m. Está escrito.</li>
<li><b>Inferencial:</b> ¿qué motivó el cambio? La seguridad de los estudiantes rurales al regresar. Se deduce de «llegan a casa de noche».</li>
<li><b>Crítico:</b> ¿es suficiente la medida? Solo cubre 9.º; el texto no dice qué pasa con los demás grados ni con el tiempo de clase perdido.</li></ul></div>
<h2>Cuatro trampas frecuentes</h2>
<ol><li>Opciones que repiten palabras del texto pero cambian el sentido con «solo», «siempre», «todos» o «nunca».</li>
<li>Opciones que exageran lo que dice el texto.</li>
<li>Opciones verdaderas en la vida real que no responden la pregunta.</li>
<li>Opciones que mezclan una idea correcta con otra que el texto no sostiene.</li></ol>
''' + EX('Regla de oro: la respuesta correcta <b>se apoya en el texto</b>. Antes de marcar, pregúntate: ¿esto está escrito, se deduce o es opinión mía?'))

# 6. Razonamiento cuantitativo
page('Componente 2', key='cua', ic='num', body='''<p class="kick">Componente 2</p>
<h1>Razonamiento cuantitativo sin calculadora</h1>
<p class="lead">En el salón no se permiten calculadoras ni celulares: todo se resuelve a mano. Los problemas son de colegio: notas, matrícula, asistencia, presupuesto.</p>
<h2>Promedio ponderado</h2>
<p>Cada nota se multiplica por su peso y se suman los resultados. Los pesos deben sumar 100 %.</p>
<div class="card"><p>Parcial 30 %, taller 20 % y proyecto 50 %, con notas 3,0, 4,0 y 4,5:</p>
<p class="big" style="font-size:15pt">3,0×0,30 + 4,0×0,20 + 4,5×0,50 = 0,90 + 0,80 + 2,25 = 3,95</p>
<p class="tip" style="margin:0">El promedio simple (3,83) engaña porque no respeta los pesos.</p></div>
<h2>Promedio de grupos de distinto tamaño</h2>
<div class="card"><p>El grupo A tiene 30 estudiantes con promedio 3,6 y el B tiene 20 con promedio 4,1.</p>
<p class="big" style="font-size:15pt">(30×3,6 + 20×4,1) ÷ 50 = 190 ÷ 50 = 3,80</p>
<p class="tip" style="margin:0">El promedio de los promedios (3,85) es un error frecuente: ignora que A es más grande.</p></div>
<h2>Variación porcentual</h2>
<p>(nuevo − anterior) ÷ anterior × 100. Si la matrícula pasa de 400 a 460: 60 ÷ 400 = 0,15, un <b>aumento de 15 %</b>. Subir 10 % y luego bajar 10 % no te devuelve al inicio: 100 → 110 → 99.</p>
''' + EX('Verifica siempre: un promedio ponderado queda entre la nota menor y la mayor, más cerca de la que más pesa. Si tu resultado se sale de ese rango, hay un error.'))

# 7. Competencias blandas
page('Componente 3', key='bla', ic='eti', body='''<p class="kick">Componente 3</p>
<h1>Competencias blandas: cómo razonar un dilema</h1>
<p class="lead">En un dilema no gana la opción más amable ni la más severa: gana la que protege el derecho en juego y sigue el orden correcto.</p>
<h2>Cuatro preguntas para filtrar cualquier caso</h2>
<div class="flow"><div><b>1.</b> ¿Qué derecho o valor está en juego, y de quién? Si hay un menor de edad, sus derechos prevalecen (Ley 1098 de 2006, arts. 8 y 9).</div><i>↓</i>
<div><b>2.</b> ¿La norma impone un deber o una prohibición? Un deber se cumple aunque incomode; una prohibición no se negocia aunque haya buena intención.</div><i>↓</i>
<div><b>3.</b> ¿Quién es competente? El docente identifica, protege y reporta. No investiga ni sanciona por fuera del manual de convivencia.</div><i>↓</i>
<div><b>4.</b> ¿Cuál es el orden? Primero proteger a la persona afectada, luego informar por el canal oficial y después corregir o reparar con debido proceso.</div></div>
<h2>Los cuatro distractores típicos</h2>
<table><tr><th>Distractor</th><th>Cómo se ve en la opción</th></tr>
<tr><td><b>El héroe solitario</b></td><td>Resuelve todo por su cuenta: investiga, cita al agresor.</td></tr>
<tr><td><b>El que mira a otro lado</b></td><td>«Eso le toca a coordinación», «no es mi función».</td></tr>
<tr><td><b>El castigador</b></td><td>Sanción ejemplar, pública o colectiva: confunde autoridad con humillación.</td></tr>
<tr><td><b>El complaciente</b></td><td>Deja pasar por gratitud o amistad: un regalo, un favor, una nota «de más».</td></tr></table>
''' + EX('Elige la opción que <b>protege</b>, <b>reporta</b> y <b>no se salta</b> la competencia de otros.'))

# 8. Función docente y PEI
page('', opener('Componente 4','Normas que todo docente debe dominar','El componente disciplinar y pedagógico pregunta cómo aplicas las normas del colegio en situaciones reales. Estas son las que más se preguntan.',['Quién es docente y qué es la función docente','El PEI y el manual de convivencia','El SIEE, la escala nacional y la promoción','Situaciones de convivencia Tipo I, II y III','Educación inclusiva y PIAR'],escuela(),'#C23A4B'),'op',key='o3')
page('Componente 4 · Normas', key='nor', ic='ley', body='''<p class="kick">Componente 4 · Normas que todo docente debe dominar</p>
<h1>Quién es quién y qué es el PEI</h1>
''' + T('Función docente', 'El trabajo profesional de enseñar, que va más allá de dictar clase.') +
NO('Decreto Ley 1278 de 2002, artículo 4. Función docente', 'La función docente es aquella de carácter profesional que implica la realización directa de los procesos sistemáticos de enseñanza - aprendizaje, lo cual incluye el diagnóstico, la planificación, la ejecución y la evaluación de los mismos procesos y sus resultados') +
NO('Decreto Ley 1278 de 2002, artículo 5. Docentes', 'Las personas que desarrollan labores académicas directa y personalmente con los alumnos de los establecimientos educativos en su proceso enseñanza aprendizaje se denominan docentes.') +
SI('Enseñar incluye <b>diagnosticar, planificar, ejecutar y evaluar</b>. Los directivos docentes son tres: <b>rector, coordinador y director rural</b> (art. 6).') +
T('PEI (Proyecto Educativo Institucional)', 'El proyecto de cada colegio: qué es, qué busca y cómo enseña.') +
NO('Ley 115 de 1994, artículo 73. Proyecto educativo institucional', 'Con el fin de lograr la formación integral del educando, cada establecimiento educativo deberá elaborar y poner en práctica un Proyecto Educativo Institucional en el que se especifiquen entre otros aspectos, los principios y fines del establecimiento, los recursos docentes y didácticos disponibles y necesarios, la estrategia pedagógica, el reglamento para docentes y estudiantes y el sistema de gestión […]') +
EX('«Concreto, factible y evaluable» describe al PEI. «Se acepta al firmar la matrícula» describe al manual de convivencia (Ley 115, art. 87).'))

# 9. Evaluación
page('Componente 4 · Evaluación', key='eva', ic='eval', body='''<p class="kick">Componente 4 · Evaluar para aprender</p>
<h1>El SIEE y la escala nacional</h1>
''' + T('SIEE (Sistema Institucional de Evaluación de los Estudiantes)', 'Las reglas de evaluación y promoción de cada colegio. Hace parte del PEI.') + '''
<h2>Qué contiene el SIEE</h2>
<ul><li>Criterios de evaluación y promoción.</li><li>Escala de valoración institucional y su equivalencia con la nacional.</li>
<li>Periodicidad y estructura de los informes a las familias.</li><li>Instancias y procedimientos para resolver reclamaciones.</li>
<li>Mecanismos de participación de la comunidad educativa.</li></ul>
<p class="tip">Decreto 1075 de 2015, art. 2.3.3.3.3.4 (antes Decreto 1290 de 2009). Lo adopta el consejo directivo (art. 2.3.3.3.3.8).</p>
<h2>La escala nacional</h2>
<div class="art" style="width:86%">''' + termometro() + '''</div>
''' + SI('Cada colegio define su escala (de 1 a 5, de 0 a 100…), pero debe expresar su equivalencia con estos cuatro niveles. El <b>básico</b> es la superación de los desempeños necesarios en las áreas obligatorias y fundamentales; el <b>bajo</b>, la no superación (art. 2.3.3.3.3.5).') + '''
<h2>Promoción anticipada</h2>
<p>Durante el <b>primer período</b>, para quien muestra un desempeño superior persistente: el <b>consejo académico</b> recomienda, con <b>consentimiento de los padres</b>, y el <b>consejo directivo</b> decide (art. 2.3.3.3.3.7).</p>
''' + EX('El docente aplica el SIEE tal como fue adoptado, no «a su manera».'))

# 10. Convivencia
page('Componente 4 · Convivencia', key='con', ic='conv', body='''<p class="kick">Componente 4 · Convivencia escolar</p>
<h1>Situaciones Tipo I, Tipo II y Tipo III</h1>
''' + NO('Decreto 1965 de 2013, artículo 40 (hoy en el Decreto 1075 de 2015)', '1. Situaciones Tipo I. Corresponden a este tipo los conflictos manejados inadecuadamente y aquellas situaciones esporádicas que inciden negativamente en el clima escolar, y que en ningún caso generan daños al cuerpo o a la salud. 2. Situaciones Tipo II. Corresponden a este tipo las situaciones de agresión escolar, acoso escolar (bullying) y ciberacoso (Ciberbullying), que no revistan las características de la comisión de un delito y que cumplan con cualquiera de las siguientes características: a) Que se presenten de manera repetida o sistemática; b) Que causen daños al cuerpo o a la salud sin generar incapacidad alguna para cualquiera de los involucrados. 3. Situaciones Tipo III. Corresponden a este tipo las situaciones de agresión escolar que sean constitutivas de presuntos delitos contra la libertad, integridad y formación sexual […] o cuando constituyen cualquier otro delito establecido en la ley penal colombiana vigente.') + '''
<h2>El semáforo de la convivencia</h2><div class="art" style="width:82%">''' + semaforo() + '''</div>
''' + SI('<b>Tipo I:</b> conflictos esporádicos sin daño. <b>Tipo II:</b> agresión, acoso o ciberacoso que no son delito y se repiten o causan daño sin incapacidad. <b>Tipo III:</b> presuntos delitos, incluida la violencia sexual. La norma de base es la Ley 1620 de 2013, que crea el Sistema Nacional de Convivencia Escolar.') +
EX('La pregunta típica es «¿qué tipo es?». Busca primero si hay delito; luego, si se repite o si hubo daño.'))

# 11. Inclusión
page('Componente 4 · Inclusión', key='inc', ic='inc', body='''<p class="kick">Componente 4 · Educación inclusiva</p>
<h1>Inclusión y PIAR</h1>
''' + NO('Decreto 1421 de 2017 (en el Decreto 1075 de 2015), artículo 2.3.3.5.1.4, numeral 7', 'Educación inclusiva: es un proceso permanente que reconoce, valora y responde de manera pertinente a la diversidad de características, intereses, posibilidades y expectativas de los niñas, niños, adolescentes, jóvenes y adultos, cuyo objetivo es promover su desarrollo, aprendizaje y participación, con pares de su misma edad, en un ambiente de aprendizaje común, sin discriminación o exclusión alguna') +
T('PIAR (Plan Individual de Ajustes Razonables)', 'El plan de apoyos y ajustes que necesita un estudiante con discapacidad para aprender y participar durante el año.') +
NO('Decreto 1421 de 2017 (en el Decreto 1075 de 2015), artículo 2.3.3.5.2.3.5', 'El diseño de los PIAR lo liderarán el o los docentes de aula con el docente de apoyo, la familia y el estudiante. Se deberá elaborar durante el primer trimestre del año escolar, se actualizará anualmente y facilitará la entrega pedagógica entre grados.') + '''
<div class="art" style="width:70%">''' + piar() + '''</div><p class="tip">Al terminar se firma un <b>acta de acuerdo</b>: acudiente, directivo, docente de apoyo y docentes a cargo (art. 2.3.3.5.2.3.6).</p>
''' + EX('La inclusión no es un aula aparte: es aprender <b>con pares de la misma edad, en un ambiente común</b>. Los seis principios: calidad, diversidad, pertinencia, participación, equidad e interculturalidad.'))

# 12. Manual de funciones
page('', opener('Capítulo 3','Tu cargo y tus competencias','El Manual de Funciones dice qué hace cada cargo y qué competencias debe mostrar. Esas competencias son la base de la prueba, la psicotécnica y la entrevista.',['Competencias funcionales de cada cargo','Qué estudiar en el componente disciplinar','La psicotécnica y la entrevista','Las siete competencias comportamentales'],rueda7(),'#2DD4BF'),'op',key='o4')
page('Tu cargo', key='car', ic='cargo', body='''<p class="kick">Capítulo 3</p>
<h1>Tu cargo según el Manual de Funciones</h1>
<p class="lead">La Resolución 3842 de 2022 del Ministerio de Educación es el Manual de Funciones, Requisitos y Competencias. Sus competencias son la base del diseño de las pruebas del concurso.</p>
<table><tr><th>Cargo</th><th>Competencias funcionales</th></tr>
<tr><td><b>Docente de aula</b><br><span class="tip">Preescolar, primaria y áreas</span></td><td>Tres gestiones: <b>académica</b> (dominio curricular, planeación, pedagogía y didáctica, evaluación del aprendizaje), <b>administrativa</b> (uso de recursos, seguimiento de procesos) y <b>comunitaria</b> (comunicación institucional, interacción con la comunidad).</td></tr>
<tr><td><b>Docente orientador</b></td><td>Tres gestiones: <b>académica</b> (proyectos de orientación psicosocial, saberes de convivencia y prevención, atención a estudiantes y familias, protocolos de atención integral), <b>administrativa</b> y <b>comunitaria</b>.</td></tr>
<tr><td><b>Rector, coordinador y director rural</b></td><td>Cuatro gestiones: <b>directiva</b> (planeación y organización, ejecución), <b>académica</b> (pedagogía y didáctica, innovación y direccionamiento académico), <b>administrativa</b> (administración de recursos, talento humano) y <b>comunitaria</b>.</td></tr></table>
''' + NO('Resolución MEN 3842 de 2022, numeral 1.1.1', 'Estas competencias funcionales y comportamentales serán la base para el diseño de las pruebas de los concursos públicos que se adelanten para la selección por mérito […]') + '''
<h2>Qué estudiar en el componente disciplinar</h2>
<ul><li><b>Docentes de área:</b> el saber de tu disciplina y su didáctica, con los referentes de calidad del Ministerio para tu área.</li>
<li><b>Preescolar y primaria:</b> desarrollo infantil, lectura y escritura iniciales, trabajo interdisciplinario y el SIEE del ciclo.</li>
<li><b>Orientador:</b> convivencia, rutas de atención, prevención de riesgos y orientación socio-ocupacional.</li>
<li><b>Directivos:</b> gestión escolar, gobierno escolar, Fondo de Servicios Educativos, evaluación institucional y de desempeño.</li></ul>''')

# 13. Psicotécnica y entrevista
page('Psicotécnica y entrevista', key='psi', ic='mente', body='''<p class="kick">Capítulo 4</p>
<h1>Psicotécnica y entrevista</h1>
''' + NO('Anexo técnico 2026, numeral 2.2. Prueba psicotécnica', 'Valora las actitudes, habilidades, motivaciones e intereses profesionales de los aspirantes en la realización directa de los procesos pedagógicos o de gestión institucional y frente a las funciones del empleo […]') + '''
<div class="grid2">
<div class="card"><h3>Psicotécnica</h3><p>Clasificatoria, de 0 a 100. Pesa <b>5 %</b> para docentes y <b>10 %</b> para directivos. Se basa en los artículos 4, 5 y 6 del Decreto Ley 1278 y en el Manual de Funciones.</p></div>
<div class="card"><h3>Entrevista</h3><p>Clasificatoria, pesa <b>10 %</b>. Evalúa competencias comportamentales con un protocolo y una rúbrica de conductas observables.</p></div></div>
<h2>Las siete competencias comportamentales</h2>
<p>Son las mismas para todos los cargos (Decreto 1075 de 2015, art. 2.4.1.5.2.5):</p>
<table><tr><td><b>1.</b> Liderazgo</td><td><b>2.</b> Comunicación y relaciones interpersonales</td></tr>
<tr><td><b>3.</b> Trabajo en equipo</td><td><b>4.</b> Negociación y mediación</td></tr>
<tr><td><b>5.</b> Compromiso social e institucional</td><td><b>6.</b> Iniciativa</td></tr>
<tr><td><b>7.</b> Orientación al logro</td><td></td></tr></table>
<h2>Cuatro pasos para una respuesta coherente</h2>
<ol><li>Ubica tu rol: docente de aula, orientador, coordinador o rector.</li>
<li>Identifica la función que está en juego: enseñar, evaluar, orientar, convivir, dirigir.</li>
<li>Elige la reacción que cumple la función con respeto: escucha, informa por el canal oficial, trabaja con otros.</li>
<li>Descarta los extremos: ni pasividad («no me corresponde») ni exceso («lo resuelvo yo solo»).</li></ol>
''' + EX('No busques la respuesta «perfecta» que no es creíble: responde con coherencia. Los instrumentos repiten ideas con otras palabras para verificar consistencia.'))

# 14. Casos
page('', opener('Capítulo 4','Practica y planea tu estudio','Lo que no se practica no se aprende. Resuelve los casos, revisa el porqué de cada respuesta y organiza tu estudio por etapas hasta el día de la prueba.',['Siete casos del colegio para practicar','Respuestas razonadas con la norma','Tu plan de estudio por etapas','Glosario de palabras clave'],camino(),'#F6C445'),'op',key='o5')
page('Practica', ic='lapiz', body='''<p class="kick">Practica</p>
<h1>Siete casos para practicar</h1>
<p>Resuélvelos antes de mirar las respuestas de la página siguiente.</p>
<div class="case"><div class="q">1. Tres estudiantes de séptimo publican cada semana memes para burlarse de un compañero en el grupo de WhatsApp del curso. No hay lesiones ni delito. ¿Qué tipo de situación es?</div><ol><li>Tipo I, porque no hubo daño al cuerpo.</li><li>Tipo II, porque es ciberacoso repetido que no constituye delito.</li><li>Tipo III, porque ocurre en redes sociales.</li></ol></div>
<div class="case"><div class="q">2. Un docente nuevo quiere calificar de 1 a 10 porque así lo hacía en su colegio anterior, aunque el SIEE adoptado usa de 1 a 5. ¿Qué debe hacer?</div><ol><li>Aplicar el SIEE adoptado y, si cree que debe cambiar, proponerlo por los canales de participación.</li><li>Usar su escala y convertir las notas al final del período.</li><li>Pedir permiso a sus estudiantes para usar su escala.</li></ol></div>
<div class="case"><div class="q">3. En marzo, una estudiante de tercero muestra desempeño superior persistente en todas las áreas. ¿Quién decide su promoción anticipada?</div><ol><li>Su docente, con un informe a la familia.</li><li>El rector, al finalizar el año escolar.</li><li>El consejo directivo, por recomendación del consejo académico y con consentimiento de los padres.</li></ol></div>
<div class="case"><div class="q">4. En febrero llega a tu grupo un estudiante con discapacidad auditiva. ¿Qué corresponde frente al PIAR?</div><ol><li>Elaborarlo en el primer trimestre, liderado por los docentes de aula con el docente de apoyo, la familia y el estudiante.</li><li>Esperar el diagnóstico médico para empezar.</li><li>Remitirlo a una institución especializada.</li></ol></div>
''')
page('Practica', ic='lapiz', body='''<p class="kick">Practica</p>
<h1>Siete casos para practicar (continuación)</h1>
<div class="case"><div class="q">5. Quices 25 %, trabajo en clase 25 % y examen final 50 %. Una estudiante saca 4,0, 3,2 y 3,0. ¿Cuál es su nota final?</div><ol><li>3,07</li><li>3,40</li><li>3,30</li></ol></div>
<div class="case"><div class="q">6. «Los reportes de conflicto bajaron de 40 a 28 en el segundo período, después de iniciar las jornadas de mediación». ¿Qué se concluye con seguridad?</div><ol><li>La mediación causó la baja.</li><li>Los reportes bajaron después de iniciar las jornadas.</li><li>La mediación debe extenderse a todos los grados.</li></ol></div>
<div class="case"><div class="q">7. Una estudiante te cuenta que en su casa la golpean y te pide no decirle a nadie. ¿Qué haces?</div><ol><li>Le prometes guardar el secreto para no perder su confianza.</li><li>Llamas a sus padres para pedirles explicaciones.</li><li>La escuchas sin juzgar, le explicas que no puedes prometer silencio y reportas ese mismo día por el canal institucional para activar la ruta de protección.</li></ol></div>''')

# 15. Respuestas
page('Respuestas razonadas', key='resp', ic='eval', body='''<p class="kick">Respuestas razonadas</p>
<h1>Así se razona cada caso</h1>
<table><tr><th style="width:12mm">#</th><th style="width:16mm">Clave</th><th>Por qué</th></tr>
<tr><td>1</td><td><b>B</b></td><td>Es ciberacoso, se repite cada semana y no hay delito: cumple las condiciones de la situación Tipo II (Decreto 1965 de 2013, art. 40). Que ocurra en redes no lo vuelve Tipo III; lo que define el Tipo III es el presunto delito.</td></tr>
<tr><td>2</td><td><b>A</b></td><td>El SIEE lo adopta el consejo directivo y hace parte del PEI (Decreto 1075 de 2015, arts. 2.3.3.3.3.4 y 2.3.3.3.3.8). El docente lo aplica tal como fue adoptado; sus propuestas van por los canales de participación.</td></tr>
<tr><td>3</td><td><b>C</b></td><td>La promoción anticipada ocurre en el primer período: el consejo académico recomienda, con consentimiento de los padres, y el consejo directivo decide (art. 2.3.3.3.3.7). El docente informa, no promueve.</td></tr>
<tr><td>4</td><td><b>A</b></td><td>El PIAR lo lideran los docentes de aula con el docente de apoyo, la familia y el estudiante, y se elabora en el primer trimestre (art. 2.3.3.5.2.3.5). Los ajustes no dependen de un diagnóstico médico, y la inclusión es en el aula común.</td></tr>
<tr><td>5</td><td><b>C</b></td><td>4,0×0,25 = 1,00; 3,2×0,25 = 0,80; 3,0×0,50 = 1,50. Suma: 3,30. La opción A es el promedio simple, que ignora los pesos.</td></tr>
<tr><td>6</td><td><b>B</b></td><td>Es lo único que el texto afirma. A supone una causa que el texto no prueba; C es una recomendación que el texto no hace.</td></tr>
<tr><td>7</td><td><b>C</b></td><td>Prevalecen los derechos de la niña y su interés superior (Ley 1098 de 2006, arts. 8 y 9). El docente identifica, protege y reporta (Ley 1620 de 2013, art. 19): no promete secreto ni investiga por su cuenta.</td></tr></table>
<div class="box simple"><span class="lbl">Fíjate en el patrón</span>Las opciones incorrectas repiten los mismos errores: el docente que decide solo, el que se salta la norma por costumbre, el que promete lo que no puede cumplir y el que confunde una idea del texto con una causa. Si los reconoces, descartas rápido.</div>''')

# 16. Plan de estudio
page('Plan de estudio', key='plan', ic='ruta', body='''<p class="kick">Capítulo 5</p>
<h1>Tu plan de estudio</h1>
<p class="lead">Según la CNSC, las pruebas escritas se aplicarían en el segundo semestre de 2027. Tienes tiempo de sobra si empiezas ya y estudias con orden.</p>
<table><tr><th style="width:42mm">Etapa</th><th>Qué estudiar</th></tr>
<tr><td><b>1. La base común</b><br><span class="tip">Desde hoy</span></td><td>Lectura crítica y razonamiento cuantitativo: 20 minutos diarios de práctica a mano. Son la mitad de la prueba eliminatoria para todos los cargos.</td></tr>
<tr><td><b>2. Las normas de todos</b></td><td>Función docente, PEI, SIEE, convivencia (Tipo I, II y III) e inclusión (PIAR). Estudia cada norma con un caso del colegio.</td></tr>
<tr><td><b>3. Tu cargo</b></td><td>Las competencias funcionales de tu cargo en el Manual de Funciones y el saber de tu área o de la gestión directiva.</td></tr>
<tr><td><b>4. Competencias blandas</b></td><td>Dilemas éticos y las siete competencias comportamentales, que sirven para la prueba, la psicotécnica y la entrevista.</td></tr>
<tr><td><b>5. Simulacros</b><br><span class="tip">Los últimos meses</span></td><td>Pruebas completas con tiempo, sin calculadora, revisando el porqué de cada error.</td></tr></table>
<h2>Una semana tipo</h2>
<table><tr><th>Lunes</th><th>Martes</th><th>Miércoles</th><th>Jueves</th><th>Viernes</th><th>Sábado</th></tr>
<tr><td>Lectura crítica</td><td>Normas</td><td>Cuantitativo</td><td>Tu cargo</td><td>Dilemas éticos</td><td>Repaso con preguntas</td></tr></table>
''' + EX('Estudia con casos, no de memoria. Después de cada pregunta que falles, escribe en una línea <b>por qué</b> la opción correcta era la correcta: ahí está el aprendizaje.'))

# 17. Glosario
page('Glosario', key='glo', ic='libro', body='''<p class="kick">Glosario</p>
<h1>Palabras que debes dominar</h1>
<table>
<tr><td style="width:52mm"><b>Ajustes razonables</b></td><td>Acciones, apoyos o modificaciones que necesita un estudiante para aprender y participar, según sus necesidades.</td></tr>
<tr><td><b>Ciberacoso</b></td><td>Acoso escolar mediante redes sociales o medios digitales. Si no es delito, es situación Tipo II.</td></tr>
<tr><td><b>Comité Escolar de Convivencia</b></td><td>Instancia del colegio que atiende las situaciones de convivencia (Ley 1620 de 2013).</td></tr>
<tr><td><b>Competencias comportamentales</b></td><td>Actitudes, valores, intereses y motivaciones que muestra el educador en su trabajo. Son siete.</td></tr>
<tr><td><b>Consejo académico</b></td><td>Órgano del gobierno escolar que orienta lo pedagógico. Recomienda la promoción anticipada.</td></tr>
<tr><td><b>Consejo directivo</b></td><td>Máxima instancia del gobierno escolar. Adopta el SIEE y decide la promoción anticipada.</td></tr>
<tr><td><b>Interés superior</b></td><td>Criterio que obliga a decidir en favor de los derechos del niño, niña o adolescente (Ley 1098 de 2006, art. 8).</td></tr>
<tr><td><b>Manual de convivencia</b></td><td>Reglamento con los derechos y obligaciones de los estudiantes. Se acepta al firmar la matrícula.</td></tr>
<tr><td><b>Manual de Funciones</b></td><td>Resolución MEN 3842 de 2022: funciones, requisitos y competencias de docentes y directivos docentes.</td></tr>
<tr><td><b>PEI</b></td><td>Proyecto Educativo Institucional: principios, estrategia pedagógica, reglamento y sistema de gestión del colegio.</td></tr>
<tr><td><b>PIAR</b></td><td>Plan Individual de Ajustes Razonables del estudiante con discapacidad. Se elabora en el primer trimestre.</td></tr>
<tr><td><b>SIEE</b></td><td>Sistema Institucional de Evaluación de los Estudiantes. Lo adopta el consejo directivo.</td></tr>
<tr><td><b>Truncar</b></td><td>Cortar los decimales sin redondear: 59,999 queda en 59,99.</td></tr>
</table>''')

# 18. Cierre
page('', '''<div class="br" style="display:flex;align-items:center;gap:4mm"><div style="width:20mm;height:19mm;background:#fff;border-radius:4mm;display:grid;place-items:center">%s</div><div><b style="font:700 17pt/1 S;letter-spacing:.03em;display:block">CONCURSOS</b><em style="font:600 9pt M;letter-spacing:.42em;color:#2DD4BF;font-style:normal;display:block;margin-top:2mm">DEL ESTADO</em></div></div>
<p class="kick" style="color:#F6C445;margin-top:14mm">Sigue estudiando</p>
<h1>Esto fue una muestra del método</h1>
<p class="lead">La cartilla interactiva Docentes desarrolla cada tema de esta guía con lecciones completas, la norma explicada al pie y cientos de preguntas de casos con su porqué. Se arma según tu cargo y la estudias en el celular o en el computador.</p>
<table><tr><th>Lo que trae la cartilla</th></tr>
<tr><td>Lectura crítica y razonamiento cuantitativo con práctica guiada</td></tr>
<tr><td>Normas del docente: estatuto, PEI, evaluación, convivencia e inclusión</td></tr>
<tr><td>Tu cargo según el Manual de Funciones, con el saber de tu área</td></tr>
<tr><td>Competencias comportamentales, ética, psicotécnica y entrevista</td></tr>
<tr><td>Simulacros con la explicación de cada respuesta</td></tr></table>
<div class="cta">Pago único según tu cargo, desde $40.000.<br>Escríbenos por WhatsApp al 316 698 2472</div>
<p style="color:#C9D4EA">Busca tu cargo y paga en línea en concursosdelestado.com</p>
<p class="legal">Aviso legal. Concursos del Estado es un proyecto independiente. No está afiliado a la CNSC ni al Ministerio de Educación Nacional; sus nombres se usan solo para indicar el concurso. Este material es de apoyo académico y no garantiza resultados. Verifica siempre la norma vigente y las fechas en la fuente oficial (SIMO y cnsc.gov.co).</p>''' % lg(60,56), 'end')
