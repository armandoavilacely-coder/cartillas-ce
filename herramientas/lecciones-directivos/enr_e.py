# -*- coding: utf-8 -*-
# Tanda B3 de directivos (16-nov-2026): Guía 34 NUEVA del MEN ("Ruta de Mejoramiento Institucional", Bogotá, 2026, 189 págs.).
# Reemplaza las lecciones/preguntas/conceptos que se hicieron con la Guía 34 de 2008 (dir_b.py).
# Las 4 lecciones conservan título y posición (el progreso guardado de los usuarios no se mueve); se añaden 2 al final.
# Citas textuales cortas, con fuente. Todo lo demás es síntesis propia de Concursos del Estado.
import sys
sys.path.insert(0, '/tmp/cce/fix7')
from dir_a import TAB

def CITA(ref, txt):
    return '<blockquote class="norma"><b>%s</b><i>“%s”</i></blockquote>' % (ref, txt)

G = "MEN, Guía 34 (Ruta de Mejoramiento Institucional, 2026)"

REPL = {'fd-gd': {}}
R = REPL['fd-gd']

# ---------------------------------------------------------------- 1
R["Guía 34: las cuatro áreas de gestión y sus procesos"] = [
 "<b>Qué evalúa.</b> Que ubiques cualquier situación del colegio en su área, su proceso y su componente, con la <b>versión 2026</b> de la Guía 34. Es el lenguaje de la autoevaluación y del plan de mejoramiento, que lideras como directivo (función 5 del rector y función 12 del coordinador, Res. MEN 3842 de 2022).",
 "<b>Qué cambió frente a la Guía 34 de 2008.</b> Si estudiaste con la versión vieja, ojo: la actualización mantiene las cuatro áreas, pero cambia nombres, reorganiza los procesos y reduce los componentes de 93 a 45.",
 CITA(G + ", Introducción", "reduciendo de 93 a 45 los componentes que estructuran los procesos de las cuatro áreas de gestión"),
 "<b>Términos clave.</b>" + TAB(["Término", "Qué significa"], [
   ["Área de gestión", "Cada una de las cuatro grandes partes del trabajo institucional: directiva y estratégica, académica y pedagógica, administrativa y financiera, y de la comunidad."],
   ["Proceso", "Lo que se hace dentro de un área para lograr un propósito (por ejemplo, gobierno escolar o acompañamiento y seguimiento académico)."],
   ["Componente", "Cada aspecto concreto que se valora dentro de un proceso (por ejemplo, el Comité Escolar de Convivencia dentro de ambiente y clima escolar)."]]),
 "<b>Las 4 áreas, sus 15 procesos y sus 45 componentes (Guía 34, Anexo 2).</b>" + TAB(["Área y proceso", "Componentes"], [
   ["<b>Directiva y estratégica</b> · 1. Direccionamiento y gestión estratégica", "Construcción del PEI; misión, visión y metas; liderazgo y articulación institucional; gestión integral de riesgos"],
   ["Directiva · 2. Gobierno escolar, instancias y otros mecanismos de participación", "Consejo directivo; consejo académico; participación de estudiantes (consejo de estudiantes, personería, contraloría, representantes al consejo directivo); instancias de participación de las familias"],
   ["Directiva · 3. Cultura institucional", "Comunicación y trabajo en equipo; buenas prácticas, experiencias significativas y fomento de CTEI lideradas por docentes"],
   ["Directiva · 4. Ambiente y clima escolar", "Inducción a nuevos estudiantes; manual de convivencia; Comité Escolar de Convivencia; motivación, sentido de pertenencia y participación de estudiantes"],
   ["Directiva · 5. Estrategias para el bienestar y la permanencia de estudiantes", "Gestión de la jornada escolar para la formación integral; servicios complementarios para el bienestar y la permanencia"],
   ["<b>Académica y pedagógica</b> · 1. Diseño pedagógico", "Enfoque pedagógico y propósitos formativos; plan de estudios; tiempo para el aprendizaje; planeación; evaluación para y del aprendizaje"],
   ["Académica · 2. Prácticas pedagógicas y gestión de aula", "Estrategias pedagógicas; mediación pedagógica con recursos; gestión pedagógica del aula"],
   ["Académica · 3. Acompañamiento y seguimiento académico", "Uso pedagógico de la información; apoyo pedagógico a todas las personas sin excepción; seguimiento a los aprendizajes y trayectorias educativas"],
   ["<b>Administrativa y financiera</b> · 1. Apoyo al proceso de gestión de la cobertura educativa", "Promoción, matrícula y novedades; gestión documental y archivo académico"],
   ["Administrativa · 2. Administración de la planta física y de los recursos", "Seguimiento al plan de mantenimiento y uso de los espacios; administración y aprovechamiento de equipos y recursos para el aprendizaje"],
   ["Administrativa · 3. Talento humano", "Apoyo a la gestión de la planta de personal; mecanismos de seguimiento y evaluación de desempeño; desarrollo de capacidades; bienestar"],
   ["Administrativa · 4. Apoyo financiero y contable", "Gestión financiera y ejecución del Fondo de Servicios Educativos; rendición de cuentas"],
   ["<b>De la comunidad</b> · 1. Accesibilidad", "Lectura de contexto con base en problemas socialmente relevantes; atención a grupos poblacionales diversos y de especial atención constitucional; relaciones con el sector productivo, autoridades y otras instituciones"],
   ["Comunidad · 2. Proyección a la comunidad", "Alianza e interacción entre familias y escuela; uso de la planta física y de los medios"],
   ["Comunidad · 3. Participación y convivencia", "Participación de estudiantes; conocimiento y apropiación de la identidad institucional; participación de egresados"]]),
 "<b>Componentes que más confunden.</b>" + TAB(["Situación", "Área y proceso (versión 2026)"], [
   ["Comité Escolar de Convivencia, manual de convivencia, inducción a estudiantes nuevos", "Directiva · ambiente y clima escolar"],
   ["Consejo directivo, consejo académico, personería, instancias de las familias", "Directiva · gobierno escolar, instancias y otros mecanismos de participación"],
   ["Jornada escolar, restaurante, transporte y otros servicios complementarios", "Directiva · estrategias para el bienestar y la permanencia"],
   ["Resultados de pruebas externas, asistencia, repitencia, ajustes razonables, trayectorias", "Académica · acompañamiento y seguimiento académico"],
   ["Matrícula, novedades, archivo académico", "Administrativa y financiera · apoyo al proceso de gestión de la cobertura"],
   ["Asignación académica, evaluación de desempeño, inducción y bienestar del personal", "Administrativa y financiera · talento humano"],
   ["Ejecución del Fondo de Servicios Educativos y rendición de cuentas", "Administrativa y financiera · apoyo financiero y contable"],
   ["Estudiantes víctimas, con discapacidad o de grupos étnicos; lectura del contexto del territorio", "De la comunidad · accesibilidad"],
   ["Escuela de padres, uso de la planta física por la comunidad, egresados", "De la comunidad · proyección a la comunidad o participación y convivencia (egresados)"]]),
 "<b>Caso.</b> En la autoevaluación, un docente propone poner el bajo uso de los resultados del ICFES en «gestión directiva». Tú lo ubicas en gestión académica y pedagógica, proceso de acompañamiento y seguimiento académico, componente «uso pedagógico de la información», porque trata de usar los resultados para decidir apoyos a los estudiantes.",
 "<b>Cómo te lo preguntan.</b> Te dan un problema concreto y cuatro áreas o procesos. Busca el componente: matrícula y archivo son administrativos; resultados, asistencia y trayectorias son académicos; comités y consejos son directivos; estudiantes con especial atención constitucional son de la comunidad (accesibilidad).",
 "<b>Fuente.</b> " + G + ", Anexo 1 y Anexo 2, y Introducción. Síntesis propia de Concursos del Estado."]

# ---------------------------------------------------------------- 2
R["La ruta del mejoramiento: tres etapas y sus pasos"] = [
 "<b>Qué evalúa.</b> Que sepas en qué orden se hace el mejoramiento institucional, quién lo hace, cada cuánto y qué producto sale de cada etapa. La versión 2026 lo vuelve un ciclo <b>anual</b>.",
 CITA(G + ", Ruta de mejoramiento institucional", "Estas tres etapas conforman un ciclo de mejoramiento anual y continuo"),
 "<b>Las tres etapas y sus pasos (Guía 34, 2026).</b>" + TAB(["Etapa", "Pasos", "Producto"], [
   ["1. Autoevaluación institucional anual (AEI)", "1) Lectura de contexto; 2) evaluación de las áreas de gestión; 3) perfil institucional; 4) fortalezas y oportunidades de mejoramiento", "Fortalezas y oportunidades, para iniciar el plan"],
   ["2. Plan de mejoramiento institucional (PMI) anual", "1) Objetivo a partir de factores críticos; 2) metas; 3) indicadores; 4) acciones y responsabilidades; 5) programación anual; 6) gestión de recursos; 7) socialización y apropiación comunitaria", "Plan anual con presupuesto y cronograma, conocido por la comunidad"],
   ["3. Seguimiento de avances y resultados del PMI", "1) Ruta participativa de seguimiento; 2) qué aprendimos y comunicación de resultados; 3) qué cambiaremos: retroalimentar la gestión y proyectar el nuevo ciclo", "Aprendizajes y decisiones que alimentan la siguiente autoevaluación"]]),
 "<b>Quién hace qué.</b>" + TAB(["Pregunta", "Respuesta de la Guía"], [
   ["¿Quién realiza la autoevaluación?", "El consejo directivo (art. 84, Ley 115 de 1994), con participación de todos los estamentos."],
   ["¿Quién la lidera?", "El rector o director: dirige el proceso, coordina recursos y equipos, y responde por su calidad (Ley 715 de 2001)."],
   ["¿Cuándo?", "Cada año, «preferiblemente al comienzo del año escolar»."],
   ["¿Dónde se incorpora el PMI?", "En el Plan Anual de Acción o Plan Operativo Anual del establecimiento, para que oriente la asignación de recursos."],
   ["¿Con qué recursos?", "Los del Fondo de Servicios Educativos pueden financiar acciones del PMI."]]),
 "<b>Siete principios de la autoevaluación.</b> Veracidad, corresponsabilidad, participación, equidad, continuidad, coherencia y legitimidad. Los más preguntados en situaciones: veracidad (decisiones con evidencias, no con opiniones), participación (toda la comunidad) y legitimidad (los resultados se conocen públicamente).",
 "<b>Lo esencial.</b> La ruta es un ciclo que se repite cada año: los resultados del seguimiento retroalimentan la autoevaluación del año siguiente. El plan <b>ya no tiene horizonte de tres años</b> como en la versión 2008: es un instrumento anual.",
 "<b>Caso.</b> Asumes la rectoría en febrero y el consejo directivo te pide «el plan de mejoramiento ya». Propones primero la autoevaluación con los estamentos, porque el objetivo y las metas del plan salen de las fortalezas y oportunidades que ella identifique, y luego llevar el plan al Plan Operativo Anual.",
 "<b>Cómo te lo preguntan.</b> «¿Qué va primero?», «¿quién realiza la autoevaluación?» o «¿qué vigencia tiene el plan?». Recuerda: diagnosticar (autoevaluación), planear (PMI anual), aprender (seguimiento); la realiza el consejo directivo y la lidera el rector.",
 "<b>Fuente.</b> " + G + ", «Ruta de mejoramiento institucional», primera etapa, etapa 2 (pasos 1 a 7) y etapa 3 (pasos 1 a 3). Síntesis propia de Concursos del Estado."]

# ---------------------------------------------------------------- 3
R["Metas e indicadores del plan de mejoramiento: cómo se escriben"] = [
 "<b>Qué evalúa.</b> Que distingas un objetivo, una meta, una acción y un indicador, y que reconozcas cuándo están bien escritos según la Guía 34 de 2026.",
 "<b>Términos clave.</b>" + TAB(["Término", "Qué significa"], [
   ["Objetivo del plan", "Horizonte del plan: concreto, realista y realizable en un año. No incluye el porqué ni las estrategias; eso va en el plan de acción."],
   ["Meta", "Enunciado de lo que el colegio espera alcanzar y en qué tiempo, con expresión cuantitativa de la magnitud. Es medible."],
   ["Indicador de proceso", "Informa durante la ejecución y permite ajustar. Ejemplo de la Guía: porcentaje de docentes que han acordado mecanismos de seguimiento durante el primer período."],
   ["Indicador de resultado", "Mide los efectos. Ejemplo de la Guía: porcentaje de estrategias de evaluación revisadas y ajustadas."],
   ["Hoja de ruta del indicador", "Ficha con nombre, tipo, qué busca, unidad de medida, variables, fórmula, fuentes de datos, aspectos metodológicos, periodicidad y responsable."]]),
 CITA(G + ", etapa 2, paso 2", "Las metas son enunciados que definen con precisión lo que el establecimiento educativo espera alcanzar y en qué tiempo. Su principal característica es que son medibles"),
 "<b>Cinco criterios para escribir metas.</b> Claras y detalladas; medibles; posibles con los recursos y el tiempo disponibles; alineadas con el objetivo; con plazo de cumplimiento (dentro del año).",
 "<b>Meta bien y mal escrita.</b>" + TAB(["Así no", "Así sí"], [
   ["«Mejorar la evaluación de los docentes»", "«Al iniciar el segundo período, con el 70 % de docentes se acordarán mecanismos de seguimiento y retroalimentación a sus labores» (ejemplo de la Guía)"],
   ["«Realizar talleres de evaluación»", "«Al finalizar el tercer período, se analizará el 100 % de las estrategias de evaluación y se ajustarán según la evaluación formativa» (ejemplo de la Guía)"]]),
 "<b>Seis rasgos de un buen indicador.</b> Relevante y pertinente; exacto y consistente (lo calcula igual cualquier persona); objetivo (hechos, no impresiones); mensurable; fácil de interpretar; viable (datos disponibles a costo manejable). Debe guardar relación con las metas y con acciones en las que el colegio tiene competencia directa.",
 "<b>Relación entre pasos.</b> Cada acción del paso 4 debe corresponder a un indicador del paso 3, y los responsables de las acciones amplían al responsable técnico que ya trae la hoja de ruta.",
 "<b>Caso.</b> Un docente te entrega el indicador «porcentaje de estrategias de evaluación revisadas y ajustadas» solo con el nombre. Le pides la hoja de ruta completa: unidad (porcentaje), fórmula (estrategias evaluadas ÷ estrategias reconocidas × 100), fuentes de datos, periodicidad (por ejemplo, bimensual) y responsable (coordinación académica y docentes).",
 "<b>Cómo te lo preguntan.</b> Te dan cuatro enunciados y preguntan cuál es una meta: busca el que tiene cifra y plazo. O describen una medición: si se hace durante la ejecución y sirve para corregir, es de proceso; si mide el efecto final, es de resultado.",
 "<b>Fuente.</b> " + G + ", etapa 2, pasos 1 a 4. Síntesis propia de Concursos del Estado; las citas y ejemplos entre comillas se toman de la Guía."]

# ---------------------------------------------------------------- 4
R["La escala de la autoevaluación: existencia, pertinencia, apropiación y mejoramiento continuo"] = [
 "<b>Qué evalúa.</b> Que ubiques un proceso o componente en el nivel correcto de la escala de cuatro niveles de la Guía 34 y que sepas cómo se registra el resultado.",
 "<b>Los cuatro niveles (Guía 34, paso 2 de la autoevaluación).</b>" + TAB(["Nivel", "Qué significa", "Señal típica"], [
   ["1. Existencia", "Desarrollo inicial, parcial o poco articulado; las acciones se realizan de manera aislada.", "La inducción de estudiantes nuevos se hace solo en algunas sedes, sin plan ni registro."],
   ["2. Pertinencia", "Hay avances en la planeación y articulación de acciones orientadas a los propósitos institucionales.", "La inducción tiene plan y responsables, pero aún no la conoce toda la comunidad."],
   ["3. Apropiación", "Las acciones están más articuladas, son conocidas y apropiadas por la comunidad educativa y favorecen los procesos institucionales.", "Todos conocen y aplican el manual de convivencia; nadie ha evaluado si reduce los conflictos."],
   ["4. Mejoramiento continuo", "Los procesos están consolidados y son objeto de seguimiento, evaluación y fortalecimiento permanente.", "El manual se revisa cada año con datos de convivencia y se ajusta."]]),
 CITA(G + ", etapa 1, paso 2", "Mejoramiento continuo: los procesos se encuentran consolidados y son objeto de seguimiento, evaluación y fortalecimiento permanente."),
 "<b>Cómo se registra.</b> En la matriz del Anexo 2 se marca con una «x» el nivel asignado a cada componente; se suman las «x» por proceso y por área. Esa tendencia permite comparar las áreas y establecer prioridades para el plan. Cada valoración se apoya en evidencias (Anexo 3: actas, informes, encuestas, planes, registros).",
 "<b>Después de valorar: el perfil institucional.</b> Es el resumen del estado de todos los procesos y componentes. Se compara año tras año para identificar avances, estancamientos y retrocesos, y es la base para reconocer fortalezas y oportunidades de mejoramiento.",
 "<b>Lo esencial.</b> La valoración se hace con evidencias y se acuerda en equipo, bajo el principio de veracidad; no es una opinión individual ni un puntaje para quedar bien. Las categorías no se calculan por «buenos resultados»: «apropiación» exige que la comunidad conozca y use la acción; «mejoramiento continuo», que además se evalúe y ajuste.",
 "<b>Caso.</b> El comité de convivencia se reúne, la comunidad conoce la ruta y los casos se atienden, pero nunca se ha revisado si las acciones reducen los conflictos. La categoría es apropiación: falta el seguimiento y la evaluación permanentes para llegar a mejoramiento continuo.",
 "<b>Cómo te lo preguntan.</b> Describen un proceso y piden el nivel. Pregúntate en orden: ¿es aislado y parcial? (existencia) ¿está planeado y articulado? (pertinencia) ¿lo conoce y lo usa la comunidad? (apropiación) ¿se evalúa y se ajusta de forma permanente? (mejoramiento continuo).",
 "<b>Fuente.</b> " + G + ", etapa 1, pasos 2 y 3, y Anexos 2 y 3. Síntesis propia de Concursos del Estado."]

# ---------------------------------------------------------------- 5 (nueva)
R["Objetivo del plan y factores críticos: urgencia, tendencia e impacto"] = [
 "<b>Qué evalúa.</b> Que sepas cómo se pasa de las oportunidades de mejoramiento al objetivo del plan: qué es un factor crítico y cómo se priorizan.",
 "<b>Términos clave.</b>" + TAB(["Término", "Qué significa"], [
   ["Oportunidad de mejoramiento", "Aspecto de un proceso o componente que la autoevaluación muestra que puede fortalecerse."],
   ["Factor crítico", "Circunstancia, suceso, práctica o actividad, interna o externa, que impide al colegio desarrollar su horizonte institucional y ofrecer una educación de calidad."],
   ["Urgencia", "Qué tan apremiante es superar el factor crítico."],
   ["Tendencia", "Qué tanto se agravaría la situación si no se elimina el factor."],
   ["Impacto", "Cuál es la incidencia del factor en el logro de resultados concretos."]]),
 CITA(G + ", etapa 2, paso 1", "Urgencia: qué tan apremiante es la necesidad de que el establecimiento educativo supere un determinado factor crítico."),
 "<b>Cómo se prioriza, paso a paso.</b>" + TAB(["Paso", "Qué se hace"], [
   ["1", "El equipo retoma la matriz de fortalezas y oportunidades de las cuatro áreas y elige <b>una oportunidad prioritaria por cada área</b>."],
   ["2", "Identifica los factores críticos de cada una, internos y externos. Analiza con más énfasis los internos, porque el colegio tiene más control sobre ellos."],
   ["3", "Valora cada factor de 1 a 5 en urgencia, tendencia e impacto (1 es poco urgente, tendencia constante o menor impacto; 5 es muy urgente, con tendencia a agravarse o de mayor impacto)."],
   ["4", "Suma los tres puntajes (U + T + I) y ordena de mayor a menor: el de mayor total es el más prioritario."],
   ["5", "Formula el objetivo del plan, articulado con las cuatro áreas y con consenso de la comunidad."]]),
 "<b>Los factores externos no se descartan.</b> Aunque el colegio no los controla, se gestionan con acciones: visibilizarlos ante las autoridades, pedir apoyo formal a las entidades competentes y hacer alianzas interinstitucionales.",
 CITA(G + ", etapa 2, paso 1", "El objetivo del Plan de mejoramiento institucional debe ser concreto, realista y realizable en el lapso de un año"),
 "<b>Lo esencial.</b> El objetivo pone en el centro la formación integral de los estudiantes, considera los recursos disponibles y se redacta sin el porqué ni las estrategias. La autonomía escolar permite ampliar el número de objetivos según las necesidades del territorio.",
 "<b>Caso.</b> El equipo tiene tres factores críticos con estas valoraciones (U/T/I): matrícula tardía 5/3/3, bajo uso de resultados 4/5/4 y falta de dotación de laboratorio 2/3/5. Sumas 11, 13 y 10. Priorizas el uso de resultados, aunque la matrícula tardía sea la más urgente: el total de los tres criterios es el que decide.",
 "<b>Cómo te lo preguntan.</b> Te dan una tabla con puntajes y piden cuál priorizas (suma los tres), o varios enunciados y piden cuál está bien escrito como objetivo (concreto, de un año, sin porqué ni estrategias).",
 "<b>Fuente.</b> " + G + ", etapa 2, paso 1. Síntesis propia de Concursos del Estado; los números del caso son un ejemplo inventado para practicar."]

# ---------------------------------------------------------------- 6 (nueva)
R["Presupuesto, cronograma y seguimiento del plan: cerrar el ciclo anual"] = [
 "<b>Qué evalúa.</b> Que sepas qué falta después de formular objetivo, metas e indicadores: programar el año, presupuestar, socializar y hacer seguimiento colectivo para aprender y ajustar.",
 "<b>Pasos 4 a 7 del plan anual.</b>" + TAB(["Paso", "Qué se hace", "Claves de la Guía"], [
   ["4. Acciones y responsables", "Mesas de trabajo, talleres o grupos focales formulan las acciones; se definen responsables y equipos.", "Cada acción corresponde a un indicador; responsabilidades equilibradas, sin sobrecargas."],
   ["5. Programación anual", "Cronograma por meses con actividades, responsables y tiempos.", "Considera la secuencia lógica, la interdependencia y los períodos en que no se puede avanzar: recesos, semanas culturales, jornadas pedagógicas."],
   ["6. Gestión de recursos", "Presupuesto anual del plan con costo y fuente de financiación de cada acción.", "Se basa en costos reales, se construye colectivamente y se socializa para validar. Las acciones del PMI pueden financiarse con el Fondo de Servicios Educativos."],
   ["7. Socialización y apropiación", "Se presenta el plan a todos los estamentos, en reunión general o por estamentos.", "Carteleras, boletines y plataformas; resolver inquietudes y actualizar avances periódicamente."]]),
 "<b>La tercera etapa: seguimiento para aprender.</b> No es solo verificar si las actividades se cumplieron. El colegio organiza espacios colectivos durante el año (puede usar las semanas de desarrollo institucional y las reuniones de las áreas de gestión), valora las evidencias en conjunto, construye aprendizajes y decide ajustes.",
 "<b>Cuatro tipos de evidencias de seguimiento.</b>" + TAB(["Tipo", "Qué muestra"], [
   ["De proceso", "Cómo se implementan las acciones."],
   ["De resultados", "Qué cambios se han logrado."],
   ["De percepción", "Cómo valoran los actores los cambios."],
   ["De aprendizaje", "Qué ha aprendido el establecimiento durante el proceso."]]),
 "<b>Decisiones posibles tras el análisis.</b> Continuar, ajustar, reorientar o incorporar nuevas acciones, y redefinir metas, responsables, tiempos o estrategias si el contexto lo exige. Las decisiones se documentan en actas y en una versión actualizada del plan.",
 "<b>Cierre del ciclo.</b> Al final del año se comunican los resultados y se proyecta el siguiente ciclo, sin repetir acciones del año anterior sin reflexión crítica sobre su pertinencia. Esa información alimenta la nueva autoevaluación.",
 "<b>Caso.</b> En la semana de desarrollo institucional de junio, el equipo revisa el plan. En vez de contar actividades cumplidas, analizan evidencias de proceso, resultados, percepción y aprendizaje; descubren que el indicador de lectura no avanza porque las sesiones se cruzan con el cronograma de actos culturales y deciden reprogramarlas y ajustar el plan.",
 "<b>Cómo te lo preguntan.</b> «¿Qué considera el cronograma?», «¿cómo se hace el presupuesto?», «¿qué se hace en un espacio de seguimiento?». La respuesta siempre es participativa, con evidencias, y termina en decisiones documentadas.",
 "<b>Fuente.</b> " + G + ", etapa 2 (pasos 4 a 7) y etapa 3 (pasos 1 a 3). Síntesis propia de Concursos del Estado."]

# ---------------------------------------------------------------- conceptos (reemplazan los de la Guía 2008)
C = {'fd-gd': [
 {"t": "Áreas de gestión (Guía 34, 2026)", "d": "Directiva y estratégica, académica y pedagógica, administrativa y financiera, y de la comunidad; 15 procesos y 45 componentes.", "c": G + ", Anexo 2", "n": ""},
 {"t": "Ruta del mejoramiento", "d": "Ciclo anual de tres etapas: autoevaluación institucional, plan de mejoramiento anual y seguimiento de sus avances.", "c": G + ", Ruta de mejoramiento institucional", "n": "Estas tres etapas conforman un ciclo de mejoramiento anual y continuo"},
 {"t": "Autoevaluación institucional anual", "d": "La realiza el consejo directivo con los estamentos (art. 84, Ley 115 de 1994), la lidera el rector y conviene hacerla al comienzo del año escolar.", "c": G + ", etapa 1", "n": ""},
 {"t": "Factor crítico", "d": "Circunstancia o práctica, interna o externa, que impide al colegio desarrollar su horizonte; se prioriza por urgencia, tendencia e impacto.", "c": G + ", etapa 2, paso 1", "n": "Urgencia: qué tan apremiante es la necesidad de que el establecimiento educativo supere un determinado factor crítico."},
 {"t": "Meta", "d": "Lo que el colegio espera alcanzar y en qué tiempo (dentro del año); siempre medible.", "c": G + ", etapa 2, paso 2", "n": "Las metas son enunciados que definen con precisión lo que el establecimiento educativo espera alcanzar y en qué tiempo. Su principal característica es que son medibles"},
 {"t": "Indicador de proceso y de resultado", "d": "El de proceso informa durante la ejecución; el de resultado mide los efectos de los procesos. Cada uno tiene su hoja de ruta.", "c": G + ", etapa 2, paso 3", "n": ""},
 {"t": "Escala de autoevaluación", "d": "Existencia, pertinencia, apropiación y mejoramiento continuo; se valora con evidencias y se registra en la matriz del Anexo 2.", "c": G + ", etapa 1, paso 2", "n": "Mejoramiento continuo: los procesos se encuentran consolidados y son objeto de seguimiento, evaluación y fortalecimiento permanente."},
]}
# Textos de conceptos antiguos (Guía 2008) que se deben retirar
OLD_C_T = ["Áreas de gestión (Guía 34)", "Ruta del mejoramiento", "Meta", "Indicador de proceso y de resultado", "Escala de autoevaluación"]

# ---------------------------------------------------------------- preguntas nuevas (reemplazan las de la Guía 2008)
Q = [
('fd-gd', "En la autoevaluación del área directiva, el equipo ve que los estudiantes nuevos llegan sin inducción y que el manual de convivencia lleva años sin revisarse. ¿Dónde lo registras según la Guía 34 de 2026?",
 "En gestión directiva y estratégica, proceso de ambiente y clima escolar, donde están la inducción y el manual",
 ["En gestión de la comunidad, proceso de participación y convivencia, porque el manual de convivencia involucra a las familias",
  "En gestión directiva y estratégica, proceso de gobierno escolar, porque el manual lo aprueba el consejo directivo",
  "En gestión académica y pedagógica, proceso de acompañamiento y seguimiento académico, porque la inducción apoya a los estudiantes"],
 "En el Anexo 2 de la Guía 34 de 2026, el proceso «ambiente y clima escolar» (área directiva y estratégica) reúne inducción a nuevos estudiantes, manual de convivencia, Comité Escolar de Convivencia y motivación y sentido de pertenencia."),
('fd-gd', "El colegio reporta las novedades de matrícula con retraso y el archivo académico está desordenado. ¿En qué área y proceso de la Guía 34 de 2026 registras esa oportunidad de mejora?",
 "Gestión administrativa y financiera, proceso de apoyo a la gestión de la cobertura educativa",
 ["Gestión académica y pedagógica, proceso de acompañamiento y seguimiento académico, porque el archivo guarda las notas",
  "Gestión administrativa y financiera, proceso de talento humano, porque el archivo lo maneja el personal administrativo",
  "Gestión directiva y estratégica, proceso de direccionamiento estratégico, porque el rector responde por la matrícula"],
 "En la Guía de 2026 el proceso «apoyo al proceso de gestión de la cobertura educativa» del área administrativa y financiera incluye promoción, matrícula y novedades, y gestión documental y archivo académico."),
('fd-gd', "Los resultados de las pruebas externas, la asistencia y la repitencia se archivan cada período, pero nadie los analiza para decidir apoyos pedagógicos. ¿Cómo lo ubicas en la Guía 34 de 2026?",
 "Gestión académica y pedagógica: acompañamiento y seguimiento académico, uso pedagógico de la información",
 ["En gestión académica y pedagógica, proceso de diseño pedagógico, componente de evaluación para y del aprendizaje",
  "En gestión directiva y estratégica, proceso de direccionamiento estratégico, porque los datos sirven para actualizar el PEI",
  "En gestión de la comunidad, proceso de accesibilidad, porque se trata de conocer la situación de los estudiantes"],
 "El proceso «acompañamiento y seguimiento académico» de la Guía 2026 comprende usar pedagógicamente la información (resultados, asistencia, repitencia, trayectorias) para decidir apoyos oportunos; no es solo diseñar o evaluar."),
('fd-gd', "Un docente señala que el colegio no ha hecho una lectura del contexto y que no tiene estrategias para atender a estudiantes víctimas, con discapacidad y de comunidades étnicas. ¿Qué proceso de la Guía 34 de 2026 está débil?",
 "Accesibilidad, del área de la comunidad, que incluye la lectura de contexto y la atención a grupos diversos",
 ["Apoyo pedagógico a todas las personas sin excepción, del proceso de acompañamiento y seguimiento académico del área académica",
  "Estrategias para el bienestar y la permanencia de estudiantes, del área directiva y estratégica",
  "Participación y convivencia, del área de la comunidad, porque trata de la participación de los estudiantes"],
 "En la Guía 2026 el proceso «accesibilidad» (área de la comunidad) incluye la lectura de contexto con base en problemas socialmente relevantes y la atención educativa a grupos poblacionales diversos y de especial atención constitucional."),
('fd-gd', "Preparas la autoevaluación con la Guía 34 nueva y un docente te muestra una matriz de la versión anterior con 93 componentes. ¿Qué le explicas?",
 "Que la versión 2026 conserva las cuatro áreas, deja 45 componentes y trae su propia matriz (Anexo 2)",
 ["Que las dos matrices son equivalentes, porque los procesos y componentes se conservaron igual en la actualización",
  "Que la versión de 2008 sigue vigente para la autoevaluación y la nueva solo es un documento de consulta",
  "Que la actualización eliminó una de las cuatro áreas de gestión para simplificar la autoevaluación del colegio"],
 "La Introducción de la Guía de 2026 dice que se mantiene la estructura de cuatro áreas, se actualizan los fundamentos y se reducen los componentes de 93 a 45 para simplificar su aplicación."),
('fd-gd', "En el consejo directivo proponen un plan de mejoramiento a tres años porque «así lo decía la guía vieja». ¿Qué orientación da la Guía 34 de 2026?",
 "Que el plan es anual, se incorpora al Plan Operativo Anual y cada año inicia con una nueva autoevaluación",
 ["Un horizonte de tres años, con revisión de metas al final de cada vigencia, para dar tiempo a los cambios institucionales",
  "Un plan de cinco años que coincida con la vigencia del PEI, ajustado cada año con el presupuesto del Fondo",
  "El plazo lo fija el rector según su período, porque la Guía deja libre la duración del plan de mejoramiento"],
 "La Guía de 2026 habla de un ciclo de mejoramiento anual y continuo: el objetivo debe ser realizable en un año, las metas se alcanzan en un año y el plan se incorpora al Plan Anual de Acción u Operativo Anual."),
('fd-gd', "El rector quiere hacer la autoevaluación solo con su equipo directivo, para entregarla pronto a la secretaría de educación. ¿Qué le recuerdas con base en la Guía 34?",
 "Que la realiza el consejo directivo con todos los estamentos y la lidera el rector",
 ["Que la hace el equipo de gestión del rector y la valida el consejo académico antes de enviarla a la secretaría",
  "Que la hace la secretaría de educación con los datos del colegio, y el rector solo entrega la información",
  "Que la hace el consejo académico, porque evalúa los procesos pedagógicos, y el rector solo la firma"],
 "La Guía dice que la autoevaluación anual la realiza el consejo directivo (art. 84, Ley 115 de 1994) con participación efectiva de los estamentos, y que la lidera el rector o director, quien dirige el proceso y responde por su calidad."),
('fd-gd', "Durante años el colegio hizo su autoevaluación en noviembre, con el cierre de notas, y el plan siempre llegaba tarde. ¿Qué recomienda la Guía 34 de 2026 sobre el momento?",
 "Hacerla cada año, preferiblemente al comienzo del año escolar, para ejecutar el plan ese mismo año",
 ["Hacerla en noviembre, porque es cuando ya están todos los resultados académicos del año",
  "Hacerla cada tres años, porque el plan de mejoramiento es trienal y debe esperar a su cierre",
  "Hacerla cuando el consejo directivo lo decida, porque la Guía no recomienda ningún momento"],
 "En el principio de continuidad, la Guía dice que la autoevaluación debe hacerse periódicamente, «preferiblemente al comienzo del año escolar», con la mejor información disponible."),
('fd-gd', "Revisas cuatro redacciones del objetivo del plan de mejoramiento. ¿Cuál cumple con la Guía 34 de 2026?",
 "Fortalecer durante el año el uso pedagógico de los resultados de evaluación en el acompañamiento académico",
 ["Mejorar los resultados de la prueba Saber porque son bajos, mediante talleres de refuerzo para los grados once",
  "Realizar doce talleres de evaluación formativa con los docentes durante el segundo y tercer período",
  "Aumentar en diez puntos el puntaje global de la prueba Saber en los próximos cinco años del PEI"],
 "La Guía pide un objetivo concreto, realista y realizable en un año, centrado en la formación integral, sin el porqué ni las estrategias (que van en el plan de acción). La segunda opción es una acción, la tercera incluye el porqué y la estrategia y la cuarta supera el año."),
('fd-gd', "El equipo valoró tres factores críticos (urgencia, tendencia, impacto): A, 5-3-3; B, 4-5-4; C, 2-3-5. ¿Cuál priorizas según la Guía 34 de 2026?",
 "El B, porque suma 13 puntos y es el de mayor total entre los tres criterios",
 ["El A, porque tiene la urgencia más alta y es el que más apremia al colegio",
  "El C, porque tiene el mayor impacto y es el que más afecta los resultados",
  "Los tres por igual, porque la Guía no permite ordenar los factores críticos por puntaje"],
 "La herramienta de la Guía suma urgencia, tendencia e impacto (de 1 a 5) y ordena de mayor a menor: el de mayor total es el más prioritario. A suma 11, B suma 13 y C suma 10."),
('fd-gd', "Revisas cuatro enunciados del borrador del plan. ¿Cuál está escrito como una meta, según la Guía 34 de 2026?",
 "Al finalizar el tercer período, el 80 % de los estudiantes de 9.° participará en la caracterización de sus proyectos de vida",
 ["Fortalecer la orientación de los proyectos de vida de los estudiantes de básica secundaria mediante estrategias participativas",
  "Realizar talleres de caracterización de proyectos de vida con los estudiantes durante todo el año escolar",
  "Porcentaje de estudiantes de 9.° que participa en actividades de caracterización de sus proyectos de vida"],
 "Para la Guía las metas definen con precisión lo que se espera alcanzar y en qué tiempo, y son medibles. La primera opción falsa es un objetivo; la segunda, una acción; la cuarta, el nombre de un indicador."),
('fd-gd', "Cada bimestre mides el porcentaje de docentes que ya acordó con coordinación los mecanismos de seguimiento y retroalimentación de su labor. ¿Qué tipo de indicador es?",
 "De proceso, porque informa durante la ejecución y permite ajustar",
 ["De resultado, porque mide un porcentaje que puede compararse al cierre del período",
  "De impacto, porque muestra cómo mejora la práctica pedagógica de los docentes en el aula",
  "De gestión financiera, porque compara las reuniones realizadas con los recursos invertidos"],
 "La Guía distingue dos tipos básicos: los indicadores de proceso brindan información durante los procesos y permiten ajustar; los de resultado miden los efectos. Su propio ejemplo de indicador de proceso es el porcentaje de docentes que han acordado mecanismos de seguimiento."),
('fd-gd', "Un docente te entrega la ficha de un indicador con nombre y meta, y nada más. ¿Qué le falta para que todos lo calculen igual, según la hoja de ruta de la Guía 34?",
 "La unidad de medida, la fórmula de cálculo, las fuentes de datos, la periodicidad y el responsable",
 ["La firma del consejo directivo y del personero, para que el indicador tenga validez ante la comunidad educativa",
  "El presupuesto asignado y el proveedor que hará la medición, para garantizar que se ejecute en el año",
  "La lista de estudiantes evaluados y sus calificaciones, como evidencia del cumplimiento de la meta"],
 "La hoja de ruta del indicador incluye nombre, tipo, qué busca, unidad de medida, definición de variables, fórmula, fuentes de datos, aspectos metodológicos, periodicidad y responsable."),
('fd-gd', "Al armar el cronograma anual del plan, un docente propone programar todas las actividades de seguida, empezando en enero. ¿Qué le indicas según el paso 5 de la Guía?",
 "Que respete la secuencia de las actividades y descuente recesos, semanas culturales y jornadas pedagógicas",
 ["Que programe todo en el primer semestre para tener el segundo libre para el seguimiento del plan",
  "Que el cronograma lo elabore el rector solo, porque la participación se reserva para la formulación de metas",
  "Que no incluya fechas, porque el plan se ajusta en cada reunión del consejo académico según el avance"],
 "El paso 5 pide un cronograma anual por meses, que detalle las actividades con su secuencia, interdependencia y los períodos institucionales en los que no se puede avanzar (recesos, semanas culturales, jornadas pedagógicas)."),
('fd-gd', "El plan de mejoramiento ya tiene acciones y cronograma. El consejo directivo te pregunta cómo se hace el presupuesto. ¿Qué respondes según la Guía 34 de 2026?",
 "Un presupuesto anual con costos reales y fuentes de financiación de cada acción, construido y socializado en colectivo",
 ["Un presupuesto por tres años, calculado sobre los ingresos del Fondo, que el rector aprueba sin socializarlo",
  "Un listado de necesidades sin costos, que la secretaría de educación valora y financia con sus propios recursos",
  "Un presupuesto que lo elabora el contador por su cuenta, porque la comunidad no interviene en asuntos financieros"],
 "El paso 6 pide elaborar el presupuesto anual del plan con base en costos reales y en las acciones definidas, indicar fuentes de financiación y socializarlo; además, la Guía recuerda que el Fondo de Servicios Educativos puede financiar acciones del PMI."),
('fd-gd', "El plan quedó aprobado, pero solo lo conoce el equipo de gestión; los docentes y las familias no saben qué les corresponde. ¿Qué paso falta, según la Guía 34?",
 "La socialización y apropiación comunitaria del plan con todos los estamentos",
 ["El seguimiento, porque es en esa etapa donde se informa a los docentes y a las familias lo que les corresponde",
  "La nueva autoevaluación, porque con ella los estamentos conocerán el plan y sus responsabilidades",
  "La reformulación del objetivo, porque un plan que la comunidad no conoce no tiene objetivo claro"],
 "El paso 7 de la etapa 2 busca que cada actor conozca su papel en la ejecución, el seguimiento y la evaluación; la Guía sugiere reuniones generales o por estamentos y materiales como carteleras, boletines electrónicos o plataformas."),
('fd-gd', "El colegio tiene un manual de convivencia que todos conocen y aplican, y el comité funciona, pero nunca se ha evaluado si las acciones reducen los conflictos. ¿En qué nivel de la escala de la Guía 34 lo ubicas?",
 "Apropiación: la comunidad conoce y usa las acciones, pero falta su seguimiento y evaluación permanentes",
 ["Mejoramiento continuo: el manual se aplica de forma permanente y la comunidad lo respeta",
  "Pertinencia: hay avances de planeación, pero el manual todavía no se aplica en la práctica",
  "Existencia: el proceso es incipiente porque no se ha medido su efecto en los conflictos"],
 "Apropiación: acciones más articuladas, conocidas y apropiadas por la comunidad. Mejoramiento continuo exige que los procesos sean objeto de seguimiento, evaluación y fortalecimiento permanente."),
('fd-gd', "Como coordinador, lideras la mesa de la autoevaluación académica. Un docente quiere calificar todo en «mejoramiento continuo» porque «los resultados han sido buenos». ¿Cómo orientas la valoración?",
 "Pides evidencias de cada componente y que el equipo acuerde el nivel real",
 ["Aceptas la propuesta, porque los buenos resultados demuestran que los procesos se evalúan y se mejoran",
  "Asignas tú el nivel de cada componente, porque el coordinador conoce mejor los procesos académicos",
  "Pones todo en existencia, para que el plan de mejoramiento tenga más acciones y más recursos"],
 "La Guía pide que la valoración se apoye en evidencias (Anexo 3) y en principios como veracidad y participación. Participar en la autoevaluación es la función 12 del coordinador (Res. MEN 3842 de 2022)."),
('fd-gd', "En la semana de desarrollo institucional de junio revisas el plan con el equipo. Un docente propone solo contar cuántas actividades se cumplieron. ¿Cómo orientas el seguimiento según la Guía 34 de 2026?",
 "Analizar en colectivo las evidencias del plan y decidir qué continuar, ajustar o reorientar",
 ["Verificar el cumplimiento de las actividades y reportar los incumplimientos a la secretaría de educación",
  "Esperar al cierre del año para evaluar el plan completo, porque ajustar a mitad de año desordena el cronograma",
  "Aprobar una nueva versión del PEI, porque el seguimiento del plan consiste en reformar la identidad institucional"],
 "La tercera etapa busca que el seguimiento sea aprendizaje institucional: espacios colectivos, evidencias de proceso, resultados, percepción y aprendizaje, y decisiones documentadas de continuar, ajustar, reorientar o incorporar acciones."),
('fd-gd', "Al terminar el año, el equipo directivo comparó el perfil institucional de este año con el del año anterior. ¿Para qué sirve esa comparación y qué sigue en la ruta?",
 "Para ver avances, estancamientos y retrocesos, y con esos aprendizajes iniciar la siguiente autoevaluación anual",
 ["Para cerrar definitivamente el plan, porque la ruta termina cuando se compara el perfil con el del año anterior",
  "Para calificar al rector, porque la Guía usa el perfil como evaluación de su desempeño anual",
  "Para reemplazar el PEI, porque el perfil institucional ya contiene la identidad del colegio"],
 "El perfil se compara en cada autoevaluación para identificar avances, estancamientos y retrocesos. Los resultados del seguimiento retroalimentan la autoevaluación del año siguiente, y así se cierra un ciclo y se inicia otro."),
]
