:- use_module(library(csv)).
:- use_module(library(lists)).

%Lista de indices
aspectos([marginacion,
          rezagosocial,
          conectividad,
          serviciosbasicos,
          elementosdesalud,
          seguridadsocial,
          educacion,
          desigualdad,
          dependenciaeconomica,
          calidaddevivienda,
          seguridadalimentaria
          ]).

% Lista de municipios conocidos
municipios_conocidos([abejones, acatlandeperezfigueroa, asuncioncacalotepec, asuncioncuyotepeji, asuncionixtaltepec, asuncionnochixtlan, asuncionocotlan, asunciontlacolulita, ayotzintepec, elbarriodelasoledad, calihuala, candelarialoxicha, cienegadezimatlan, ciudadixtepec, coatecasaltas, coicoyandelasflores, lacompania, concepcionbuenavista, concepcionpapalo, constanciadelrosario, cosolapa, cosoltepec, cuilapamdeguerrero, cuyamecalcovilladezaragoza, chahuites, chalcatongodehidalgo, chiquihuitlandebenitojuarez, heroicaciudaddeejutladecrespo, eloxochitlandefloresmagon, elespinal, tamazulapamdelespiritusanto, fresnillodetrujano, guadalupeetla, guadalupederamirez, guelataodejuarez, gueveadehumboldt, mesoneshidalgo, villahidalgo, heroicaciudaddehuajuapandeleon, huautepec, huautladejimenez, ixtlandejuarez, juchitandezaragoza, lomabonita, magdalenaapasco, magdalenajaltepec, santamagdalenajicotlan, magdalenamixtepec, magdalenaocotlan, magdalenapenasco, magdalenateitipac, magdalenatequisistlan, magdalenatlacotepec, magdalenazahuatlan, mariscaladejuarez, martiresdetacubaya, matiasromeroavendano, mazatlanvilladeflores, miahuatlandeporfiriodiaz, mixistlandelareforma, monjas, natividad, nazarenoetla, nejapademadero, ixpantepecnieves, santiagoniltepec, oaxacadejuarez, ocotlandemorelos, lape, pinotepadedonluis, plumahidalgo, sanjosedelprogreso, putlavilladeguerrero, santacatarinaquioquitani, reformadepineda, lareforma, reyesetla, rojasdecuauhtemoc, salinacruz, sanagustinamatengo, sanagustinatenango, sanagustinchayuco, sanagustindelasjuntas, sanagustinetla, sanagustinloxicha, sanagustintlacotepec, sanagustinyatareni, sanandrescabeceranueva, sanandresdinicuiti, sanandreshuaxpaltepec, sanandreshuayapam, sanandresixtlahuaca, sanandreslagunas, sanandresnuxino, sanandrespaxtlan, sanandressinaxtla, sanandressolaga, sanandresteotilalpam, sanandrestepetlapa, sanandresyaa, sanandreszabache, sanandreszautla, sanantoninocastillovelasco, sanantoninoelalto, sanantoninomonteverde, sanantonioacutla, sanantoniodelacal, sanantoniohuitepec, sanantonionanahuatipam, sanantoniosinicahua, sanantoniotepetlapa, sanbaltazarchichicapam, sanbaltazarloxicha, sanbaltazaryatzachielbajo, sanbartolocoyotepec, sanbartolomeayautla, sanbartolomeloxicha, sanbartolomequialana, sanbartolomeyucuane, sanbartolomezoogocho, sanbartolosoyaltepec, sanbartoloyautepec, sanbernardomixtepec, sanblasatempa, sancarlosyautepec, sancristobalamatlan, sancristobalamoltepec, sancristoballachirioag, sancristobalsuchixtlahuaca, sandionisiodelmar, sandionisioocotepec, sandionisioocotlan, sanestebanatatlahuca, sanfelipejalapadediaz, sanfelipetejalapam, sanfelipeusila, sanfranciscocahuacua, sanfranciscocajonos, sanfranciscochapulapa, sanfranciscochindua, sanfranciscodelmar, sanfranciscohuehuetlan, sanfranciscoixhuatan, sanfranciscojaltepetongo, sanfranciscolachigolo, sanfranciscologueche, sanfrancisconuxano, sanfranciscoozolotepec, sanfranciscosola, sanfranciscotelixtlahuaca, sanfranciscoteopan, sanfranciscotlapancingo, sangabrielmixtepec, sanildefonsoamatlan, sanildefonsosola, sanildefonsovillaalto, sanjacintoamilpas, sanjacintotlacotepec, sanjeronimocoatlan, sanjeronimosilacayoapilla, sanjeronimososola, sanjeronimotaviche, sanjeronimotecoatl, sanjorgenuchita, sanjoseayuquila, sanjosechiltepec, sanjosedelpenasco, sanjoseestanciagrande, sanjoseindependencia, sanjoselachiguiri, sanjosetenango, sanjuanachiutla, sanjuanatepec, animastrujano, sanjuanbautistaatatlahuca, sanjuanbautistacoixtlahuaca, sanjuanbautistacuicatlan, sanjuanbautistaguelache, sanjuanbautistajayacatlan, sanjuanbautistalodesoto, sanjuanbautistasuchitepec, sanjuanbautistatlacoatzintepec, sanjuanbautistatlachichilco, sanjuanbautistatuxtepec, sanjuancacahuatepec, sanjuancieneguilla, sanjuancoatzospam, sanjuancolorado, sanjuancomaltepec, sanjuancotzocon, sanjuanchicomezuchil, sanjuanchilateca, sanjuandelestado, sanjuandelrio, sanjuandiuxi, sanjuanevangelistaanalco, sanjuanguelavia, sanjuanguichicovi, sanjuanihualtepec, sanjuanjuquilamixes, sanjuanjuquilavijanos, sanjuanlachao, sanjuanlachigalla, sanjuanlajarcia, sanjuanlalana, sanjuandeloscues, sanjuanmazatlan, sanjuanmixtepec, sanjuanmixtepec, sanjuannumi, sanjuanozolotepec, sanjuanpetlapa, sanjuanquiahije, sanjuanquiotepec, sanjuansayultepec, sanjuantabaa, sanjuantamazola, sanjuanteita, sanjuanteitipac, sanjuantepeuxila, sanjuanteposcolula, sanjuanyaee, sanjuanyatzona, sanjuanyucuita, sanlorenzo, sanlorenzoalbarradas, sanlorenzocacaotepec, sanlorenzocuaunecuiltitla, sanlorenzotexmelucan, sanlorenzovictoria, sanlucascamotlan, sanlucasojitlan, sanlucasquiavini, sanlucaszoquiapam, sanluisamatlan, sanmarcialozolotepec, sanmarcosarteaga, sanmartindeloscansecos, sanmartinhuamelulpam, sanmartinitunyoso, sanmartinlachila, sanmartinperas, sanmartintilcajete, sanmartintoxpalan, sanmartinzacatepec, sanmateocajonos, capulalpamdemendez, sanmateodelmar, sanmateoyoloxochitlan, sanmateoetlatongo, sanmateonejapam, sanmateopenasco, sanmateopinas, sanmateoriohondo, sanmateosindihui, sanmateotlapiltepec, sanmelchorbetaza, sanmiguelachiutla, sanmiguelahuehuetitlan, sanmiguelaloapam, sanmiguelamatitlan, sanmiguelamatlan, sanmiguelcoatlan, sanmiguelchicahua, sanmiguelchimalapa, sanmigueldelpuerto, sanmigueldelrio, sanmiguelejutla, sanmiguelelgrande, sanmiguelhuautla, sanmiguelmixtepec, sanmiguelpanixtlahuaca, sanmiguelperas, sanmiguelpiedras, sanmiguelquetzaltepec, sanmiguelsantaflor, villasoladevega, sanmiguelsoyaltepec, sanmiguelsuchixtepec, villataleadecastro, sanmigueltecomatlan, sanmigueltenango, sanmigueltequixtepec, sanmigueltilquiapam, sanmigueltlacamama, sanmigueltlacotepec, sanmigueltulancingo, sanmiguelyotao, sannicolas, sannicolashidalgo, sanpablocoatlan, sanpablocuatrovenados, sanpabloetla, sanpablohuitzo, sanpablohuixtepec, sanpablomacuiltianguis, sanpablotijaltepec, sanpablovillademitla, sanpabloyaganiza, sanpedroamuzgos, sanpedroapostol, sanpedroatoyac, sanpedrocajonos, sanpedrocoxcaltepeccantaros, sanpedrocomitancillo, sanpedroelalto, sanpedrohuamelula, sanpedrohuilotepec, sanpedroixcatlan, sanpedroixtlahuaca, sanpedrojaltepetongo, sanpedrojicayan, sanpedrojocotipac, sanpedrojuchatengo, sanpedromartir, sanpedromartirquiechapa, sanpedromartiryucuxaco, sanpedromixtepec, sanpedromixtepec, sanpedromolinos, sanpedronopala, sanpedroocopetatillo, sanpedroocotepec, sanpedropochutla, sanpedroquiatoni, sanpedrosochiapam, sanpedrotapanatepec, sanpedrotaviche, sanpedroteozacoalco, sanpedroteutila, sanpedrotidaa, sanpedrotopiltepec, sanpedrototolapam, villadetututepec, sanpedroyaneri, sanpedroyolox, sanpedroysanpabloayutla, villadeetla, sanpedroysanpabloteposcolula, sanpedroysanpablotequixtepec, sanpedroyucunama, sanraymundojalpan, sansebastianabasolo, sansebastiancoatlan, sansebastianixcapa, sansebastiannicananduta, sansebastianriohondo, sansebastiantecomaxtlahuaca, sansebastianteitipac, sansebastiantutla, sansimonalmolongas, sansimonzahuatlan, santaana, santaanaateixtlahuaca, santaanacuauhtemoc, santaanadelvalle, santaanatavela, santaanatlapacoyan, santaanayareni, santaanazegache, santacatalinaquieri, santacatarinacuixtla, santacatarinaixtepeji, santacatarinajuquila, santacatarinalachatao, santacatarinaloxicha, santacatarinamechoacan, santacatarinaminas, santacatarinaquiane, santacatarinatayata, santacatarinaticua, santacatarinayosonotu, santacatarinazapoquila, santacruzacatepec, santacruzamilpas, santacruzdebravo, santacruzitundujia, santacruzmixtepec, santacruznundaco, santacruzpapalutla, santacruztacachedemina, santacruztacahua, santacruztayata, santacruzxitla, santacruzxoxocotlan, santacruzzenzontepec, santagertrudis, santainesdelmonte, santainesyatzeche, santaluciadelcamino, santaluciamiahuatlan, santaluciamonteverde, santaluciaocotlan, santamariaalotepec, santamariaapazco, santamarialaasuncion, heroicaciudaddetlaxiaco, ayoquezcodealdama, santamariaatzompa, santamariacamotlan, santamariacolotepec, santamariacortijo, santamariacoyotepec, santamariachachoapam, villadechilapadediaz, santamariachilchotla, santamariachimalapa, santamariadelrosario, santamariadeltule, santamariaecatepec, santamariaguelace, santamariaguienagati, santamariahuatulco, santamariahuazolotitlan, santamariaipalapa, santamariaixcatlan, santamariajacatepec, santamariajalapadelmarques, santamariajaltianguis, santamarialachixio, santamariamixtequilla, santamarianativitas, santamarianduayaco, santamariaozolotepec, santamariapapalo, santamariapenoles, santamariapetapa, santamariaquiegolani, santamariasola, santamariatataltepec, santamariatecomavaca, santamariatemaxcalapa, santamariatemaxcaltepec, santamariateopoxco, santamariatepantlali, santamariatexcatitlan, santamariatlahuitoltepec, santamariatlalixtac, santamariatonameca, santamariatotolapilla, santamariaxadani, santamariayalina, santamariayavesia, santamariayolotepec, santamariayosoyua, santamariayucuhiti, santamariazacatepec, santamariazaniza, santamariazoquitlan, santiagoamoltepec, santiagoapoala, santiagoapostol, santiagoastata, santiagoatitlan, santiagoayuquililla, santiagocacaloxtepec, santiagocamotlan, santiagocomaltepec, villadesantiagochazumba, santiagochoapam, santiagodelrio, santiagohuajolotitlan, santiagohuauclilla, santiagoihuitlanplumas, santiagoixcuintepec, santiagoixtayutla, santiagojamiltepec, santiagojocotepec, santiagojuxtlahuaca, santiagolachiguiri, santiagolalopa, santiagolaollaga, santiagolaxopa, santiagollanogrande, santiagomatatlan, santiagomiltepec, santiagominas, santiagonacaltepec, santiagonejapilla, santiagonundiche, santiagonuyoo, santiagopinotepanacional, santiagosuchilquitongo, santiagotamazola, santiagotapextla, villatejupamdelaunion, santiagotenango, santiagotepetlapa, santiagotetepec, santiagotexcalcingo, santiagotextitlan, santiagotilantongo, santiagotillo, santiagotlazoyaltepec, santiagoxanica, santiagoxiacui, santiagoyaitepec, santiagoyaveo, santiagoyolomecatl, santiagoyosondua, santiagoyucuyachi, santiagozacatepec, santiagozoochila, nuevozoquiapam, santodomingoingenio, santodomingoalbarradas, santodomingoarmenta, santodomingochihuitan, santodomingodemorelos, santodomingoixcatlan, santodomingonuxaa, santodomingoozolotepec, santodomingopetapa, santodomingoroayaga, santodomingotehuantepec, santodomingoteojomulco, santodomingotepuxtepec, santodomingotlatayapam, santodomingotomaltepec, santodomingotonala, santodomingotonaltepec, santodomingoxagacia, santodomingoyanhuitlan, santodomingoyodohino, santodomingozanatepec, santosreyesnopala, santosreyespapalo, santosreyestepejillo, santosreyesyucuna, santotomasjalieza, santotomasmazaltepec, santotomasocotepec, santotomastamazulapan, sanvicentecoatlan, sanvicentelachixio, sanvicentenunu, silacayoapam, sitiodexitlapehua, soledadetla, villadetamazulapamdelprogreso, tanetzedezaragoza, taniche, tataltepecdevaldes, teococuilcodemarcosperez, teotitlandefloresmagon, teotitlandelvalle, teotongo, tepelmemevillademorelos, heroicavillatezoatlandesegurayluna, cunadelaindependenciadeoaxaca, sanjeronimotlacochahuaya, tlacoluladematamoros, tlacotepecplumas, tlalixtacdecabrera, totontepecvillademorelos, trinidadzaachila, latrinidadvistahermosa, unionhidalgo, valeriotrujano, sanjuanbautistavallenacional, villadiazordaz, yaxe, magdalenayodoconodeporfiriodiaz, yogana, yutanduchideguerrero, villadezaachila, sanmateoyucutindoo, zapotitlanlagunas, zapotitlanpalmas, santainesdezaragoza, zimatlandealvarez]).

%Lista de niveles de los aspectos y prioridades
niveles([
          muybajo,
          bajo,
          medio,
          alto,
          muyalto,
          muybaja,
          baja,
          media,
          alta,
          muyalta
]).

%------------ 1.Funcion principal ------
procesar_consulta(Archivo, StringEntrada, Resultado) :-
    % 1. Convertir la entrada a una lista de atomos (Tokens) sin acentos o mayusculas
    sin_acentos(StringEntrada,StringEntrada2),
    string_lower(StringEntrada2, StringMinusculas),
    tokenize_atom(StringMinusculas, Tokens),
    % 2. Intentar parsear la consulta con la DCG y obtener el Request unificado
    (phrase(consulta(Archivo, Request), Tokens) ->
        % Exito en el parseo
        ejecutar_accion(Request, Archivo, Resultado)
        ;
        % Fallo en el parseo
        Resultado = 'No se entendió la consulta o el formato es incorrecto.'
    ).

ejecutar_accion(imprimir_tabla_municipio(Archivo, Municipio), Archivo, Resultado) :-
    %Llama la impresion y el Resultado es un mensaje de exito.
    imprimir_tabla_municipio(Archivo, Municipio),
    %Llama a la nueva función para obtener la lista de niveles
    (obtener_niveles_municipio(Archivo, Municipio, ListaNiveles) ->
        %Formatea el resultado a una cadena para que sea el valor de retorno.
        format(atom(Resultado), 'Impresión de tabla exitosa. Niveles de carencia encontrados: ~w', [ListaNiveles])
    ;
        %Manejo de error si no se encuentra el municipio.
        Resultado = 'Error al obtener los niveles de carencia o municipio no encontrado.'
    ).

ejecutar_accion(request(Archivo, Municipio, Aspecto, Tipo_solicitud), Archivo, Resultado) :-
    % Llama a la logica de busqueda de dato unico.
    manejar_request(Archivo, Municipio, Aspecto,Tipo_solicitud, Resultado).

                     % --- 2. Gramatica DCG ---
consulta(Archivo, Request) --> pregunta_prioridad_nivel(Archivo,Request),!.
consulta(Archivo, Request) --> pregunta_aspectos(Archivo,Request),!.
consulta(Archivo, Request) --> pregunta_prioridad(Archivo,Request),!.
consulta(Archivo, Request) --> pregunta_status(Archivo, Request),!.
consulta(Archivo, Request) --> pregunta_estado(Archivo,Request).

%------------------- Consultas -----------------------------
%�Cual es el "estado" del "municipio"?
pregunta_estado(Archivo,imprimir_tabla_municipio(Archivo,Municipio)) -->
    ignora_palabras,
    [estado],
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.

% �Cual es el "estatus" del "aspecto" del "municio"?
pregunta_status(Archivo, request(Archivo, Municipio, Aspecto, _)) -->
    ignora_palabras,
    [estado],
    ignora_palabras,
    [Aspecto],
    {es_aspecto(Aspecto)},
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.

%�Cuales son los "aspectos" del "municipio" que tienen cierto "nivel"?
pregunta_aspectos(Archivo, request(Archivo, Municipio, Nivel, _)) -->
    ignora_palabras,
    [aspectos],
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras,
    [Nivel],
    {es_nivel(Nivel)},
    ignora_palabras.

% �Que "prioridad" tiene el "aspecto" del "municipio"?
pregunta_prioridad(Archivo, request(Archivo, Municipio, Aspecto, prioridad)) -->
    ignora_palabras,
    [prioridad],
    ignora_palabras,
    [Aspecto],
    {es_aspecto(Aspecto)},
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.


%�Qu� "aspectos" del "municipio" "requieren" apoyo de prioridad "nivel"?
pregunta_prioridad_nivel(Archivo, request(Archivo, Municipio, Prioridad,apoyo_nivel)) -->
    ignora_palabras,
    [aspectos],
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras,
    [requieren],
    ignora_palabras,
    [Prioridad],
    {es_nivel(Prioridad)},
    ignora_palabras.

% Ayudante DCG: ignora 0 o mas palabras
ignora_palabras --> [_], ignora_palabras.
ignora_palabras --> [].

%-------------- Casos de las preguntas ----------------------
%Caso 1: Solicitud del estado de un aspecto
manejar_request(Archivo, Municipio, Aspecto, estado, NivelCarencia) :-
    %Se busca la fila del municipio en el archivo csv
    buscar_municipio(Archivo, Municipio, Fila_Municipio),
    %Se busca la columna del aspecto en el archivo csv
    buscar_columna(Aspecto, Columna),
    %Se extrae la informacion de la celda
    extraer_informacion(Fila_Municipio, Columna, NivelCarencia).

% Caso 2: Solicitud de prioridad de un aspecto
manejar_request(Archivo, Municipio, Aspecto, prioridad, NivelPrioridad) :-
    %Se busca la fila del municipio en el archivo csv
    buscar_municipio(Archivo, Municipio, Fila_Municipio),
    %Se busca la columna del aspecto en el archivo csv
    buscar_columna(Aspecto, Columna),
    %Se extrae la informacion de la celda
    extraer_informacion(Fila_Municipio, Columna, NivelCarencia),
    %Se convierte el nivel de carencia a nivel de prioridad
    carencia_a_prioridad(NivelCarencia, NivelPrioridad).

%Caso 3: Solicitud de aspectos por nivel
manejar_request(Archivo, Municipio, NivelAtom, por_nivel, Resultado) :-
    %Se obtiene la fila del municipio
    buscar_municipio(Archivo, Municipio, Fila_Municipio),
    %Se convierte el atomo de nivel (con espacio y primer letra en mayuscula)
    atom_nivel_a_csv_string(NivelAtom, NivelCSV),
    %Se itera sobre todos los aspectos para encontrar aquellos con NivelCSV
    aspectos(ListaAspectos),
    %Se filtra la lista de aspectos
    findall(AspectoEncontrado,
            aspecto_tiene_nivel(Fila_Municipio, AspectoEncontrado, NivelCSV),
            AspectosCoincidentes),
    %Formatea el resultado
    (AspectosCoincidentes = [] ->
        format(atom(Resultado), 'El municipio ~w no tiene aspectos con un nivel de carencia "~w".', [Municipio, NivelCSV])
    ;
        %Se convierten los atomos de aspecto a nombres amigables para la salida
        maplist(aspecto_display_name, AspectosCoincidentes, NombresAspectos),

        %Se crea la lista
        list_to_formatted_string(NombresAspectos, ListaFormateada),
        format(atom(Resultado), 'Los aspectos del municipio ~w con nivel de carencia "~w" son: ~w.', [Municipio, NivelCSV, ListaFormateada])
    ).

%Caso 4: Solicitud de aspectos por nivel de prioridad
manejar_request(Archivo, Municipio, NivelAtom, apoyo_nivel, Resultado) :-
    %Se obtiene la fila del municipio
    buscar_municipio(Archivo, Municipio, Fila_Municipio),
    %Mapea el �tomo de entrada al string de prioridad
    nivel_atom_a_prioridad_string(NivelAtom, NivelCarenciaBuscado),
    carencia_a_prioridad(NivelCarenciaBuscado,NivelPrioridad),
    aspectos(ListaAspectos),
    %Filtra la lista de aspectos que coinciden con el nivel de carencia
    findall(AspectoEncontrado,
            aspecto_requiere_prioridad(Fila_Municipio, AspectoEncontrado, NivelPrioridad),
            AspectosCoincidentes),
    %Formatea el resultado
    (AspectosCoincidentes = [] ->
        format(atom(Resultado), 'El municipio ~w no tiene aspectos que requieran una prioridad de apoyo "~w".', [Municipio, NivelPrioridad])
    ;
        maplist(aspecto_display_name, AspectosCoincidentes, NombresAspectos),
        list_to_formatted_string(NombresAspectos, ListaFormateada),
        format(atom(Resultado), 'Los aspectos del municipio ~w que requieren una prioridad de apoyo "~w" son: ~w.', [Municipio, NivelPrioridad, ListaFormateada])
    ).

%--------------------------- Se imprime la tabla --------------
imprimir_tabla_municipio(Archivo, Municipio) :-
    (buscar_municipio(Archivo, Municipio, Fila_Municipio) ->
        % 1. Imprimir el encabezado de la tabla
        write('=========================================='), nl,
        write(' DATOS COMPLETOS DE: '), write(Municipio), nl,
        write('------------------------------------------'), nl,
        write(' Aspecto                      | Nivel'), nl,
        write('=========================================='), nl,
        % 2. Llamada recursiva
        aspectos(ListaAspectos),
        imprimir_aspectos_y_niveles(Fila_Municipio, ListaAspectos),
        write('=========================================='), nl
    ;
        % Fallo si el Municipio no existe
        write('Error: El municipio '), write(Municipio), write(' no fue encontrado.'), nl,
        fail
    ).
% Caso base: La lista de aspectos esta vacia, terminamos.
imprimir_aspectos_y_niveles(_, []).
% Caso recursivo: Procesar el primer Aspecto (H) y luego el resto (T).
imprimir_aspectos_y_niveles(Fila_Municipio, [AspectoAtom|RestoAspectos]) :-
    % 1. Encontrar el indice de columna para el Aspecto
    (buscar_columna(AspectoAtom, Columna) ->
        % 2. Extraer el valor (Nivel)
        extraer_informacion(Fila_Municipio, Columna, Nivel),
        % 3. Obtener el nombre bonito para imprimir
        aspecto_display_name(AspectoAtom, AspectoDisplay),
        % 4. Formatear e imprimir la lnea de la tabla
        formatear_y_escribir(AspectoDisplay, Nivel),
        nl
    ;
        % Si el aspecto no tiene mapeo de columna, lo ignora y pasa al siguiente
        true
    ),
    % 5.Llamada recursiva
imprimir_aspectos_y_niveles(Fila_Municipio, RestoAspectos).
formatear_y_escribir(Aspecto, Nivel) :-
    % Usamos ~t~30| para rellenar con espacios hasta la columna 30
    format(' ~w~t~30| ~w', [Aspecto, Nivel]).

% --------------------------- NUEVO PREDICADO: Obtiene la lista de niveles --------------
obtener_niveles_municipio(Archivo, Municipio, ListaNiveles) :-
    % 1. Busca la fila del municipio
    buscar_municipio(Archivo, Municipio, Fila_Municipio),
    % 2. Obtiene la lista de aspectos
    aspectos(ListaAspectos),
    % 3. Llama al predicado auxiliar para recolectar los niveles
    findall(Nivel,
            (
                member(AspectoAtom, ListaAspectos),
                buscar_columna(AspectoAtom, Columna),
                extraer_informacion(Fila_Municipio, Columna, Nivel)
            ),
            ListaNiveles).

% -------------- Predicado auxiliar para verificar si un Aspecto tiene
%un nivel especifico en la fila -------------
aspecto_tiene_nivel(Fila_Municipio, AspectoAtom, NivelCSV) :-
    % Asegurarse de que el atomo es un aspecto valido y tiene un mapeo de columna
    aspecto_display_name(AspectoAtom, _),
    buscar_columna(AspectoAtom, Columna),
    extraer_informacion(Fila_Municipio, Columna, NivelEncontrado),
    % Compara el Nivel del CSV con el Nivel buscado
    NivelEncontrado == NivelCSV.

% ------------------- Base de conocimiento para invertir el nivel de
% carencia en nivel de prioridad o inversa ---------------

%Carencia a prioridad
carencia_a_prioridad('Muy alto', 'Muy baja').
carencia_a_prioridad('Alto', 'Baja').
carencia_a_prioridad('Medio', 'Media').
carencia_a_prioridad('Bajo', 'Alta').
carencia_a_prioridad('Muy bajo', 'Muy alta').
%Prioridad a carencia
carencia_a_prioridad('Muy alta', 'Muy bajo').
carencia_a_prioridad('Alta', 'Bajo').
carencia_a_prioridad('Media', 'Medio').
carencia_a_prioridad('Baja', 'Alto').
carencia_a_prioridad('Muy baja', 'Muy alto').
% Se separan las palabras y se sacan mayusculas y se pasa de prioridad a
% carencia
nivel_atom_a_prioridad_string(muyalta, 'Muy bajo').
nivel_atom_a_prioridad_string(alta, 'Bajo').
nivel_atom_a_prioridad_string(media, 'Medio').
nivel_atom_a_prioridad_string(baja, 'Alto').
nivel_atom_a_prioridad_string(muybaja, 'Muy alto').
% Se separan las palabras y se sacan mayusculas y se pasa de carencia a
% prioridad
atom_nivel_a_csv_string(muyalto, 'Muy alta').
atom_nivel_a_csv_string(alto, 'Alto').
atom_nivel_a_csv_string(medio, 'Medio').
atom_nivel_a_csv_string(bajo, 'Bajo').
atom_nivel_a_csv_string(muybajo, 'Muy bajo').
%Se separan palabras, se ponen acentos y se sacan mayusculas
aspecto_display_name(marginacion, 'Marginaci�n').
aspecto_display_name(rezagosocial, 'Rezago Social').
aspecto_display_name(conectividad, 'Conectividad').
aspecto_display_name(serviciosbasicos, 'Servicios B�sicos').
aspecto_display_name(seguridadsocial, 'Seguridad Social').
aspecto_display_name(elementosdesalud, 'Elementos de Salud').
aspecto_display_name(educacion, 'Educaci�n').
aspecto_display_name(desigualdad, 'Desigualdad').
aspecto_display_name(dependenciaeconomica, 'Dependencia Econ�mica').
aspecto_display_name(calidaddevivienda, 'Calidad de Vivienda').
aspecto_display_name(seguridadalimentaria, 'Seguridad Alimentaria').

% Helper para unir listas de strings/atomos con comas y una 'y' final.
list_to_formatted_string([X], X).
list_to_formatted_string([X, Y], Resultado) :-
    atomic_list_concat([X, ' y ', Y], '', Resultado).
list_to_formatted_string([H|T], Resultado) :-
    T = [_|_], % Asegura que hay mas de dos elementos restantes
    list_to_formatted_string(T, RestoFormateado),
    atomic_list_concat([H, ', ', RestoFormateado], '', Resultado).

% Predicado auxiliar para verificar si un aspecto tiene un Nivel de
% prioridad especifico
aspecto_requiere_prioridad(Fila_Municipio, AspectoAtom, NivelPrioridadBuscado) :-
    aspecto_display_name(AspectoAtom, _),
    buscar_columna(AspectoAtom, Columna),
    %Se obtiene la carencia (dato crudo)
    extraer_informacion(Fila_Municipio, Columna, NivelCarencia),
    %Se calcula la prioridad
    carencia_a_prioridad(NivelCarencia, NivelPrioridadCalculado),
    %Se compara la prioridad
    NivelPrioridadCalculado == NivelPrioridadBuscado.

%Se encuentra la fila del municipio
buscar_municipio(Archivo, NombreBuscado, FilaEncontrada) :-
    csv_read_file(Archivo, Filas, []),
    encontrar_fila(NombreBuscado, Filas, FilaEncontrada).

encontrar_fila(NombreBuscado, Filas, FilaEncontrada) :-
    member(FilaEncontrada, Filas),
    % Descomponemos la FilaEncontrada en [Functor, Campo1, Campo2, ...]
    FilaEncontrada =.. ListaConFunctor,
    % Separamos: el functor, el primer campo de datos (_),
    % el segundo campo (que es el nombre) y el resto.
    ListaConFunctor = [_Functor, _CampoIgnorado, NombreEncontrado | _RestoCampos],
    % Verificamos si el 'NombreEncontrado' (el segundo campo) coincide
    NombreEncontrado == NombreBuscado,
    !.

%Se le asigna a cada aspecto el valor de su columna
buscar_columna(Aspecto, Columna) :-
    (Aspecto == marginacion -> Columna is 4);
    (Aspecto == rezagosocial -> Columna is 5);
    (Aspecto == conectividad -> Columna is 6);
    (Aspecto == serviciosbasicos -> Columna is 7);
    (Aspecto == elementosdesalud -> Columna is 8);
    (Aspecto == educacion -> Columna is 9);
    (Aspecto == desigualdad -> Columna is 10);
    (Aspecto == dependenciaeconomica -> Columna is 11);
    (Aspecto == calidaddevivienda -> Columna is 12);
    (Aspecto == seguridadalimentaria -> Columna is 13);
    (Aspecto == seguridadsocial -> Columna is 14).

%Se extrae informacion de la celda
extraer_informacion(Fila_Municipio, Columna, Aspecto):-
    Fila_Municipio =.. ListaConFunctor,
    ListaConFunctor = [_Functor | Campos],
    nth1(Columna, Campos, Aspecto).

%Se verifica que "aspecto" este en la lista de aspectos
es_aspecto(Aspecto) :-
    aspectos(ListaAspectos),
    member(Aspecto, ListaAspectos).

%Se verifica que "municipio" este en la lista de municipios
es_municipio(Municipio):-
    municipios_conocidos(ListaMunicipios),
    member(Municipio, ListaMunicipios).

% Se verifica que "nivel" este en la lista de niveles
es_nivel(Nivel) :-
    niveles(ListaNiveles),
    member(Nivel, ListaNiveles).

%-----------------------------Se quitan acentos------------------
sin_acentos(ConAcento, SinAcento) :-
    % 1. Convertir a lista de codigos para procesar
    % Usaremos string_codes/2 si estamos seguros de que la entrada es un string.
    (   string(ConAcento) -> string_codes(ConAcento, Codes)
    ;
        Codes = ConAcento
    ),

    % 2. Procesar la lista de codigos
    reemplazar_acentos(Codes, NewCodes),
    % 3. Convertir la lista de codigos resultante al tipo de salida deseado
    string_codes(SinAcento, NewCodes).


% reemplazar_acentos(+ListaCodes, -ListaCodesSinAcentos)
reemplazar_acentos([], []).

% Caso: Caracter acentuado, lo reemplaza
reemplazar_acentos([Code|Resto], [NewCode|NewResto]) :-
    reemplazo_caracter(Code, NewCode),
    reemplazar_acentos(Resto, NewResto),
    !. % Cortar para que no pruebe el caso general.

% Caso: Caracter no acentuado, lo mantiene
reemplazar_acentos([Code|Resto], [Code|NewResto]) :-
    reemplazar_acentos(Resto, NewResto).

% --- Base de Conocimiento para Reemplazos ---

% Acentos minúsculas
reemplazo_caracter(0'á, 0'a).
reemplazo_caracter(0'é, 0'e).
reemplazo_caracter(0'í, 0'i).
reemplazo_caracter(0'ó, 0'o).
reemplazo_caracter(0'ú, 0'u).

% Acentos mayúsculas
reemplazo_caracter(0'Á, 0'A).
reemplazo_caracter(0'É, 0'E).
reemplazo_caracter(0'Í, 0'I).
reemplazo_caracter(0'Ó, 0'O).
reemplazo_caracter(0'Ú, 0'U).















