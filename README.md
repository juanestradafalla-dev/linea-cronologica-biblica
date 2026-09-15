# Cronología bíblica

Página estática de fondo claro. Línea horizontal por décadas desde 600 a. C. hasta el cierre en 70 d. C.; recorrido de las 15 etapas originales desde la rebelión celestial. Conserva las 148 fichas y enlaza al mural de 417 fichas de familias y episodios, con 6.206 apariciones de personas o grupos y 2.839 relaciones. Las apariciones repetidas no son personas únicas.

La ampliación anterior completó los ocho bloques identificados: familias de jueces, ramas tribales, Safán, Baruc y su entorno, recabitas, casas del retorno, Job y parentescos del Nuevo Testamento. Las notas de Elena G. White distinguen obra, capítulo y referencia de página/párrafo en la edición inglesa consultada. Las familias enlazan a los acontecimientos relacionados y las fichas de acontecimientos permiten regresar a esas familias. El catálogo descargable documenta la cobertura y las incertidumbres.

La segunda implementación anterior incorporó los 34 hallazgos pendientes y 14 nuevos cotejos. En esa edición, el registro acumulado contenía 97 hallazgos incorporados, incluidos casos representados como cautelas de interpretación. Se añaden 47 ramas; las 103 anteriores permanecen idénticas. Incorporar una variante no significa resolverla: las casas, los vínculos de crianza y los parentescos espirituales se distinguen de la filiación biológica. La revisión integral de las fuentes continúa pendiente.

## Uso

Abrir `dist/index.html` en un navegador. No requiere instalación ni conexión para consultar el contenido. Las flechas avanzan una década o una etapa; cada ficha muestra fuentes y observaciones. El buscador consulta todos los campos del estudio.

## Fechas

Sólo se colocan en décadas los acontecimientos con año absoluto explícito en el estudio. No se inventan años para la creación, las generaciones o los años de reinado. Las fechas 457 a. C., 27, 31 y 34 d. C. conservan la atribución al modelo historicista de GC. La campaña de 67–69 figura en el intervalo 60–69; los periodos amplios muestran su referencia inicial, no una fecha para todos sus subacontecimientos.

Las décadas a. C. avanzan 600–591, 590–581, etc. No existe año cero. El primer intervalo d. C. contiene 1–9 y el último sólo 70, por el límite del estudio. Las columnas identifican intervalos, no una escala proporcional para medir duración.

## Publicación en GitHub y Vercel

Repositorio público: https://github.com/juanestradafalla-dev/linea-cronologica-biblica. Publicación: https://linea-cronologica-biblica.vercel.app/. Vercel, equipo `personal-3162`, despliega los cambios de `main`. Configuración: **Other**, sin comando de compilación, directorio de salida **dist**. `vercel.json` incluye estos ajustes.

No subir la carpeta superior del estudio ni los PDF: la carpeta `web` contiene toda la página necesaria. Los originales y el respaldo permanecen fuera del proyecto de publicación.

Documentación oficial: [configurar la compilación](https://vercel.com/docs/builds/configure-a-build) y [conectar GitHub](https://vercel.com/docs/git/vercel-for-github).

## Actualizar

`pagina-base.html` contiene diseño e interacciones. `preparar.py` genera `dist/index.html` desde los datos locales de `../estudio`, y copia el mural y el catálogo. Los archivos de `dist` están listos para publicar y no necesitan Python en Vercel.

La colección documental todavía no está cotejada íntegramente. Esta edición de estudio no afirma exhaustividad ni resuelve todas las variantes genealógicas.

## Incorporación de la revisión por libros

Se añaden 39 fichas documentadas (R098–R136): 204 apariciones y 30 relaciones explícitas. Las 150 fichas previas y los 148 acontecimientos permanecen idénticos. Total: 189 fichas, 2.723 apariciones y 2.225 relaciones; 136 hallazgos incorporados. El buscador del mural también encuentra títulos de familias y episodios. Las fichas nuevas explican relato, fuentes y marco temporal; no se inventan fechas o parentescos para compañeros de misión. La revisión integral continúa pendiente.

## Quinta ampliación

R137–R157 incorporados: 21 fichas, 125 apariciones y 10 relaciones adicionales. Total actual: 210 fichas, 4.174 apariciones y 2.653 relaciones; 157 hallazgos incorporados. Las 189 fichas anteriores y los 148 acontecimientos originales permanecen idénticos. Se mantienen las cautelas de identidad, cronología y parentesco. La revisión integral permanece pendiente.

## Sexta incorporación: personajes

26 listas y grupos con fuentes explícitas y cautelas de identidad. Las 210 fichas anteriores y los 148 acontecimientos se conservan. Continúa pendiente el cotejo integral de personajes; no se declara cerrado el inventario.

## Personajes de 1 Crónicas 9 y 12

Se cotejaron sus 84 versículos y se añadieron nueve fichas con 206 apariciones y 96 relaciones. No equivalen a 206 personas nuevas. Las 236 fichas previas y los acontecimientos permanecen intactos. El resto del libro continúa pendiente.

## Personajes de Esdras 10 y Nehemías 3 y 11

Doce fichas adicionales con 334 apariciones y 202 relaciones; no equivalen a 334 personas nuevas. Se cotejaron los 112 versículos y se conservaron las 245 fichas anteriores y los acontecimientos. Los demás capítulos y el contraste integral con White siguen pendientes.

El mural comparte internamente las cadenas repetidas para reducir tamaño sin eliminar contenido. La reconstrucción JavaScript se comparó con los datos completos; las 257 fichas y los 148 acontecimientos coinciden exactamente.

## Esdras: cotejo de personajes de los diez capítulos

Se completa una pasada por los 280 versículos de Esdras en KJV. Diez fichas adicionales: 161 apariciones y 19 relaciones, sin alterar las 257 fichas anteriores. Las variantes, identificaciones discutidas, paralelos y contraste completo con White siguen abiertos.

## Nehemías: cotejo de personajes de los trece capítulos

Se completa una pasada por los 406 versículos en KJV (338 en esta revisión y 68 previamente). Diecisiete fichas adicionales con 335 apariciones y 14 relaciones; no son 335 personas nuevas. Se conservan las 267 fichas anteriores y los acontecimientos. Las variantes, paralelos, identidades y contraste completo con White siguen pendientes.

## 1 Crónicas: cotejo de personajes de los veintinueve capítulos

Completada una pasada bíblica de personajes por los 942 versículos de 1 Crónicas en la KJV aportada: 858 leídos en esta tanda, además de los 84 de los capítulos 9 y 12 cotejados anteriormente. Diecinueve fichas adicionales (G285–G303; R232–R250): variantes genealógicas, jefes de Simeón, músicos y servidores del arca, turnos sacerdotales y militares y familiares secundarios. Total: 303 fichas, 5.123 apariciones de personas o grupos y 2.772 relaciones; las apariciones no son personas únicas. Se conservan las 284 fichas anteriores y los 148 acontecimientos. Las variantes, identificaciones, cronologías y el contraste completo con Elena G. White siguen abiertos.


## 2 Crónicas: cotejo de personajes de los treinta y seis capítulos

Completada una pasada bíblica de personajes por los 822 versículos de 2 Crónicas en la KJV aportada. Se añaden 23 fichas (G304–G326; R251–R273), con 377 apariciones de personas o grupos y 37 relaciones: maestros y capitanes de Josafat, servidores de las reformas, familias y colaboradores secundarios, y variantes entre Crónicas y Reyes. Total: 326 fichas, 4.923 apariciones y 2.757 relaciones. Las apariciones incluyen repeticiones y colectivos; no equivalen a personas únicas. Las 303 fichas previas y los 148 acontecimientos permanecen intactos. Siguen pendientes las identificaciones discutidas, cronologías y el contraste completo con Elena G. White.


## 1 Reyes: cotejo de personajes de los veintidós capítulos

Completada una pasada bíblica de personajes por los 816 versículos de 1 Reyes en la KJV aportada. Quince fichas adicionales (G327–G341; R274–R288): 200 apariciones y 15 relaciones. Se conservan personas anónimas, familias de adversarios, profetas, servidores y conexiones posteriores de los hijos de Nabot y la tumba del hombre de Dios. Total: 341 fichas, 5.123 apariciones de personas o grupos y 2.772 relaciones; las apariciones no son personas únicas. Las 326 fichas previas y los 148 acontecimientos permanecen intactos. Siguen abiertos los paralelos, identidades discutidas, cronologías y el contraste completo con Elena G. White.


## 2 Reyes: pasada de personajes completa

Completada una pasada bíblica de personajes por los 25 capítulos y 719 versículos de 2 Reyes en la KJV aportada. Se añaden 22 fichas G342–G363 / R289–R310, 365 apariciones y 16 relaciones. Total: 363 fichas, 5.488 apariciones de personas o grupos y 2.788 relaciones. Las apariciones incluyen colectivos y repeticiones; no son personas únicas. Se conservan las 341 fichas anteriores y los 148 acontecimientos. Descendientes sin nombres, auxiliares, familias de reyes y continuidad hasta el exilio incluyen fuentes y cautelas. Siguen pendientes identidades, sincronismos, variantes y el contraste completo con Elena G. White. Próximo libro propuesto: 1 Samuel.

## 1 Samuel: pasada de personajes completa

Completada una pasada bíblica de personajes por los 31 capítulos y 810 versículos de 1 Samuel en la KJV aportada. Se añaden 22 fichas G364–G385 / R311–R332, 284 apariciones y 19 relaciones. Total: 385 fichas, 5.772 apariciones de personas o grupos y 2.807 relaciones. Las apariciones incluyen colectivos y repeticiones; no son personas únicas. Las 363 fichas anteriores y los 148 acontecimientos permanecen intactos. Se incorporan ascendencias con sus formas propias, custodios del arca, madres y servidores anónimos, ramas y reapariciones. Se cotejan puntualmente PP 679.3; 680.1 y 714.1–2 para Endor y Nahas, con atribución explícita a Elena G. White. Siguen pendientes variantes, cronologías y el contraste completo con su corpus. Próximo libro propuesto: 2 Samuel.

## 2 Samuel: cotejo de personajes de los veinticuatro capítulos

Completada una pasada bíblica de personajes por los 24 capítulos y 695 versículos de 2 Samuel en la KJV aportada. Se añaden 17 fichas G386–G402 / R333–R349, 239 apariciones y 15 relaciones. Total: 402 fichas, 6.011 apariciones de personas o grupos y 2.822 relaciones. Las apariciones incluyen colectivos y repeticiones; no son personas únicas. Las 385 fichas anteriores y los 148 acontecimientos permanecen intactos. Se incorporan padres anónimos, nodriza de Mefiboset, Amiud–Talmai, variantes de los oficiales y auxiliares de las crisis de David. Se distinguen parábolas, acusaciones y genealogías documentadas. PP 735.3 se coteja puntualmente para Ahitofel y Betsabé, con atribución explícita a Elena G. White. Variantes, cronologías y contraste integral con White siguen abiertos. Próximo libro propuesto: Jueces.

## Jueces: cotejo de personajes de los veintiún capítulos

Completada una pasada bíblica de personajes por los 21 capítulos y 618 versículos de Jueces en la KJV aportada. Se añaden 15 fichas G403–G417 / R350–R364, 195 apariciones y 17 relaciones. Total: 417 fichas, 6.206 apariciones de personas o grupos y 2.839 relaciones. Las apariciones incluyen colectivos y repeticiones; no son personas únicas. Las 402 fichas anteriores y los 148 acontecimientos permanecen intactos. Se incorporan Gera–Aod, madre de Sísara, auxiliares de Gedeón, abuelo y tíos maternos de Abimelec, nueras de Ibzán y familias anónimas del cierre. La respuesta por medio de un profeta se atribuye expresamente a White, PP 557.3; también se cotejan PP 556.3 y 560.2–4. Siguen abiertos variantes, cronologías y contraste integral con White. Próximo libro propuesto: Rut.
