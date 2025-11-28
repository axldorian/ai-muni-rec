% =============================================================================
% SISTEMA DE CONSULTA DE INDICADORES MUNICIPALES
% =============================================================================
% Este módulo permite consultar información sobre indicadores de carencia
% y prioridad de apoyo para municipios de Oaxaca.
%
% Autor: [Equipo de desarrollo]
% Fecha: Noviembre 2025
% =============================================================================

% --- MÓDULOS EXTERNOS ---
:- use_module(library(csv)).
:- use_module(library(lists)).

% =============================================================================
% SECCIÓN 1: CONFIGURACIÓN Y CONSTANTES
% =============================================================================

% --- Ruta del archivo de datos ---
% Ruta fija al archivo CSV con los indicadores municipales
ruta_csv_indicadores('/home/axl/master-courses/ai-muni-rec/data/processed/indicators_municipal_v2.csv').

% --- Lista de aspectos/indicadores evaluados ---
aspectos([
    marginacion,
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

% --- Lista de municipios conocidos ---
% Se carga dinámicamente desde el CSV para no ocupar espacio
:- dynamic municipios_cache/1.

/**
 * municipios_conocidos(-ListaMunicipios)
 * 
 * Obtiene la lista de municipios desde el CSV (columna municipio_norm).
 * Usa caché para evitar leer el archivo múltiples veces.
 */
municipios_conocidos(ListaMunicipios) :-
    % Verificar si ya está en caché
    (municipios_cache(ListaMunicipios) ->
        true
    ;
        % Cargar desde CSV
        ruta_csv_indicadores(RutaCSV),
        csv_read_file(RutaCSV, Filas, []),
        % Extraer municipios de la columna 2 (municipio_norm)
        findall(Municipio,
                (member(Fila, Filas),
                 Fila =.. [_Functor, _Col1, Municipio | _Resto],
                 Municipio \= municipio_norm),  % Excluir encabezado
                ListaMunicipios),
        % Guardar en caché
        assertz(municipios_cache(ListaMunicipios))
    ).

% --- Niveles de carencia y prioridad ---
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

% =============================================================================
% SECCIÓN 2: INTERFAZ PRINCIPAL
% =============================================================================

/**
 * procesar_consulta(+StringEntrada, -Resultado)
 * 
 * Punto de entrada principal del sistema. Procesa una consulta en lenguaje
 * natural y retorna el resultado correspondiente.
 *
 * @param StringEntrada Consulta en lenguaje natural (texto)
 * @param Resultado Resultado de la consulta (átomo o string)
 */
procesar_consulta(StringEntrada, Resultado) :-
    % 1. Normalizar la entrada: quitar acentos y convertir a minúsculas
    sin_acentos(StringEntrada, StringSinAcentos),
    string_lower(StringSinAcentos, StringMinusculas),
    tokenize_atom(StringMinusculas, Tokens),
    
    % 2. Parsear la consulta usando la gramática DCG
    (phrase(consulta(Request), Tokens) ->
        % Parseo exitoso: ejecutar la acción correspondiente
        ejecutar_accion(Request, Resultado)
    ;
        % Parseo fallido: mensaje de error
        Resultado = 'No se entendió la consulta o el formato es incorrecto.'
    ).

/**
 * ejecutar_accion(+Request, -Resultado)
 * 
 * Ejecuta la acción correspondiente según el tipo de request parseado.
 */
ejecutar_accion(imprimir_tabla_municipio(Municipio), Resultado) :-
    % Obtener ruta del archivo CSV
    ruta_csv_indicadores(RutaCSV),
    
    % Obtener datos estructurados del municipio
    (obtener_datos_municipio(RutaCSV, Municipio, DatosEstructurados) ->
        Resultado = DatosEstructurados
    ;
        Resultado = 'Error: Municipio no encontrado.'
    ).

ejecutar_accion(request(Municipio, Aspecto, TipoSolicitud), Resultado) :-
    % Obtener ruta del archivo CSV
    ruta_csv_indicadores(RutaCSV),
    
    % Delegar al manejador de requests específicos
    manejar_request(RutaCSV, Municipio, Aspecto, TipoSolicitud, Resultado).

% =============================================================================
% SECCIÓN 3: GRAMÁTICA DCG PARA PARSING DE CONSULTAS
% =============================================================================

/**
 * consulta(-Request)
 * 
 * Gramática principal que intenta parsear diferentes tipos de consultas.
 * Prueba cada tipo de pregunta en orden de especificidad.
 */
consulta(Request) --> pregunta_prioridad_nivel(Request), !.
consulta(Request) --> pregunta_aspectos(Request), !.
consulta(Request) --> pregunta_prioridad(Request), !.
consulta(Request) --> pregunta_status(Request), !.
consulta(Request) --> pregunta_estado(Request).

% --- Reglas DCG para diferentes tipos de preguntas ---

/**
 * pregunta_estado(-Request)
 * 
 * Parsea: "¿Cuál es el estado del [municipio]?"
 * Genera una solicitud para imprimir la tabla completa del municipio.
 */
pregunta_estado(imprimir_tabla_municipio(Municipio)) -->
    ignora_palabras,
    [estado],
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.

/**
 * pregunta_status(-Request)
 * 
 * Parsea: "¿Cuál es el estado/estatus del [aspecto] del [municipio]?"
 * Consulta el nivel de carencia de un aspecto específico.
 */
pregunta_status(request(Municipio, Aspecto, estado)) -->
    ignora_palabras,
    [estado],
    ignora_palabras,
    [Aspecto],
    {es_aspecto(Aspecto)},
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.

/**
 * pregunta_aspectos(-Request)
 * 
 * Parsea: "¿Cuáles son los aspectos del [municipio] que tienen nivel [nivel]?"
 * Lista los aspectos con un nivel de carencia específico.
 */
pregunta_aspectos(request(Municipio, Nivel, por_nivel)) -->
    ignora_palabras,
    [aspectos],
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras,
    [Nivel],
    {es_nivel(Nivel)},
    ignora_palabras.

/**
 * pregunta_prioridad(-Request)
 * 
 * Parsea: "¿Qué prioridad tiene el [aspecto] del [municipio]?"
 * Consulta el nivel de prioridad de apoyo para un aspecto.
 */
pregunta_prioridad(request(Municipio, Aspecto, prioridad)) -->
    ignora_palabras,
    [prioridad],
    ignora_palabras,
    [Aspecto],
    {es_aspecto(Aspecto)},
    ignora_palabras,
    [Municipio],
    {es_municipio(Municipio)},
    ignora_palabras.

/**
 * pregunta_prioridad_nivel(-Request)
 * 
 * Parsea: "¿Qué aspectos del [municipio] requieren apoyo de prioridad [nivel]?"
 * Lista aspectos que requieren un nivel específico de prioridad.
 */
pregunta_prioridad_nivel(request(Municipio, Prioridad, apoyo_nivel)) -->
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

/**
 * ignora_palabras
 * 
 * Regla DCG auxiliar que ignora 0 o más palabras (tokens).
 * Útil para hacer el parsing más flexible.
 */
ignora_palabras --> [_], ignora_palabras.
ignora_palabras --> [].

% =============================================================================
% SECCIÓN 4: MANEJADORES DE REQUESTS
% =============================================================================

/**
 * manejar_request(+RutaCSV, +Municipio, +Parametro, +TipoSolicitud, -Resultado)
 * 
 * Procesa diferentes tipos de solicitudes sobre datos municipales.
 * Se implementan 4 tipos de consultas principales.
 */

% --- Caso 1: Consultar el estado (nivel de carencia) de un aspecto ---
manejar_request(RutaCSV, Municipio, Aspecto, estado, NivelCarencia) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    buscar_columna(Aspecto, Columna),
    extraer_informacion(FilaMunicipio, Columna, NivelCarencia).

% --- Caso 2: Consultar la prioridad de apoyo de un aspecto ---
manejar_request(RutaCSV, Municipio, Aspecto, prioridad, NivelPrioridad) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    buscar_columna(Aspecto, Columna),
    extraer_informacion(FilaMunicipio, Columna, NivelCarencia),
    carencia_a_prioridad(NivelCarencia, NivelPrioridad).

% --- Caso 3: Listar aspectos con un nivel de carencia específico ---
manejar_request(RutaCSV, Municipio, NivelAtom, por_nivel, Resultado) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    atom_nivel_a_csv_string(NivelAtom, NivelCSV),
    
    % Encontrar todos los aspectos con el nivel especificado
    findall(Aspecto,
            aspecto_tiene_nivel(FilaMunicipio, Aspecto, NivelCSV),
            AspectosCoincidentes),
    
    % Formatear el resultado
    formatear_resultado_aspectos(Municipio, AspectosCoincidentes, NivelCSV, 
                                  'con nivel de carencia', Resultado).

% --- Caso 4: Listar aspectos que requieren un nivel de prioridad específico ---
manejar_request(RutaCSV, Municipio, NivelAtom, apoyo_nivel, Resultado) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    nivel_atom_a_prioridad_string(NivelAtom, NivelCarenciaBuscado),
    carencia_a_prioridad(NivelCarenciaBuscado, NivelPrioridad),
    
    % Encontrar todos los aspectos con la prioridad especificada
    findall(Aspecto,
            aspecto_requiere_prioridad(FilaMunicipio, Aspecto, NivelPrioridad),
            AspectosCoincidentes),
    
    % Formatear el resultado
    formatear_resultado_aspectos(Municipio, AspectosCoincidentes, NivelPrioridad,
                                  'que requieren una prioridad de apoyo', Resultado).

/**
 * formatear_resultado_aspectos(+Municipio, +Aspectos, +Nivel, +Descripcion, -Resultado)
 * 
 * Helper para formatear resultados de listas de aspectos.
 */
formatear_resultado_aspectos(Municipio, [], Nivel, Descripcion, Resultado) :-
    format(atom(Resultado), 
           'El municipio ~w no tiene aspectos ~w "~w".', 
           [Municipio, Descripcion, Nivel]).

formatear_resultado_aspectos(Municipio, Aspectos, Nivel, Descripcion, Resultado) :-
    Aspectos \= [],
    maplist(aspecto_display_name, Aspectos, NombresAspectos),
    list_to_formatted_string(NombresAspectos, ListaFormateada),
    format(atom(Resultado), 
           'Los aspectos del municipio ~w ~w "~w" son: ~w.', 
           [Municipio, Descripcion, Nivel, ListaFormateada]).

% =============================================================================
% SECCIÓN 5: VISUALIZACIÓN DE DATOS
% =============================================================================

/**
 * imprimir_tabla_municipio(+RutaCSV, +Municipio)
 * 
 * Imprime una tabla formateada con todos los indicadores de un municipio.
 * Muestra aspecto y su nivel de carencia correspondiente.
 */
imprimir_tabla_municipio(RutaCSV, Municipio) :-
    (buscar_municipio(RutaCSV, Municipio, FilaMunicipio) ->
        % Imprimir encabezado
        write('=========================================='), nl,
        write(' DATOS COMPLETOS DE: '), write(Municipio), nl,
        write('------------------------------------------'), nl,
        write(' Aspecto                      | Nivel'), nl,
        write('=========================================='), nl,
        
        % Imprimir cada aspecto con su nivel
        aspectos(ListaAspectos),
        imprimir_aspectos_y_niveles(FilaMunicipio, ListaAspectos),
        
        % Imprimir pie de tabla
        write('=========================================='), nl
    ;
        % Error si el municipio no existe
        write('Error: El municipio '), write(Municipio), write(' no fue encontrado.'), nl,
        fail
    ).

/**
 * imprimir_aspectos_y_niveles(+FilaMunicipio, +ListaAspectos)
 * 
 * Predicado recursivo que imprime cada aspecto con su nivel.
 */
% Caso base: lista vacía
imprimir_aspectos_y_niveles(_, []).

% Caso recursivo: procesar primer aspecto y continuar con el resto
imprimir_aspectos_y_niveles(FilaMunicipio, [Aspecto|RestoAspectos]) :-
    (buscar_columna(Aspecto, Columna) ->
        extraer_informacion(FilaMunicipio, Columna, Nivel),
        aspecto_display_name(Aspecto, AspectoDisplay),
        format(' ~w~t~30| ~w~n', [AspectoDisplay, Nivel])
    ;
        % Si no hay mapeo de columna, ignorar
        true
    ),
    imprimir_aspectos_y_niveles(FilaMunicipio, RestoAspectos).

/**
 * obtener_niveles_municipio(+RutaCSV, +Municipio, -ListaNiveles)
 * 
 * Obtiene una lista con todos los niveles de carencia del municipio.
 * Útil para retornar información estructurada.
 */
obtener_niveles_municipio(RutaCSV, Municipio, ListaNiveles) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    aspectos(ListaAspectos),
    findall(Nivel,
            (member(Aspecto, ListaAspectos),
             buscar_columna(Aspecto, Columna),
             extraer_informacion(FilaMunicipio, Columna, Nivel)),
            ListaNiveles).

/**
 * obtener_datos_municipio(+RutaCSV, +Municipio, -DatosEstructurados)
 * 
 * Obtiene todos los datos del municipio en formato estructurado JSON-like.
 * Retorna una cadena con formato: "municipio|aspecto1:nivel1|aspecto2:nivel2|..."
 * Este formato es fácil de parsear en Python con pyswip.
 */
obtener_datos_municipio(RutaCSV, Municipio, DatosEstructurados) :-
    buscar_municipio(RutaCSV, Municipio, FilaMunicipio),
    aspectos(ListaAspectos),
    
    % Crear lista de pares aspecto:nivel
    findall(ParAspectoNivel,
            (member(Aspecto, ListaAspectos),
             buscar_columna(Aspecto, Columna),
             extraer_informacion(FilaMunicipio, Columna, Nivel),
             aspecto_display_name(Aspecto, NombreAspecto),
             format(atom(ParAspectoNivel), '~w:~w', [NombreAspecto, Nivel])),
            ParesDatos),
    
    % Unir todo en una cadena separada por pipes
    atomic_list_concat([Municipio|ParesDatos], '|', DatosEstructurados).

% =============================================================================
% SECCIÓN 6: PREDICADOS AUXILIARES DE BÚSQUEDA Y FILTRADO
% =============================================================================

/**
 * aspecto_tiene_nivel(+FilaMunicipio, +Aspecto, +NivelBuscado)
 * 
 * Verifica si un aspecto específico tiene el nivel de carencia buscado.
 */
aspecto_tiene_nivel(FilaMunicipio, Aspecto, NivelBuscado) :-
    aspecto_display_name(Aspecto, _),
    buscar_columna(Aspecto, Columna),
    extraer_informacion(FilaMunicipio, Columna, NivelEncontrado),
    NivelEncontrado == NivelBuscado.

/**
 * aspecto_requiere_prioridad(+FilaMunicipio, +Aspecto, +NivelPrioridadBuscado)
 * 
 * Verifica si un aspecto requiere un nivel de prioridad específico.
 * Convierte el nivel de carencia a prioridad y lo compara.
 */
aspecto_requiere_prioridad(FilaMunicipio, Aspecto, NivelPrioridadBuscado) :-
    aspecto_display_name(Aspecto, _),
    buscar_columna(Aspecto, Columna),
    extraer_informacion(FilaMunicipio, Columna, NivelCarencia),
    carencia_a_prioridad(NivelCarencia, NivelPrioridadCalculado),
    NivelPrioridadCalculado == NivelPrioridadBuscado.

% =============================================================================
% SECCIÓN 7: CONVERSIONES Y MAPEOS
% =============================================================================

% --- Conversión entre niveles de carencia y prioridad ---
% La relación es inversa: alta carencia = baja prioridad de apoyo, y viceversa

/**
 * carencia_a_prioridad(?NivelCarencia, ?NivelPrioridad)
 * 
 * Mapeo bidireccional entre niveles de carencia y prioridad.
 * La relación es inversa según la lógica del dominio.
 */
% Carencia -> Prioridad
carencia_a_prioridad('Muy alto', 'Muy baja').
carencia_a_prioridad('Alto', 'Baja').
carencia_a_prioridad('Medio', 'Media').
carencia_a_prioridad('Bajo', 'Alta').
carencia_a_prioridad('Muy bajo', 'Muy alta').

% Prioridad -> Carencia (relación inversa)
carencia_a_prioridad('Muy alta', 'Muy bajo').
carencia_a_prioridad('Alta', 'Bajo').
carencia_a_prioridad('Media', 'Medio').
carencia_a_prioridad('Baja', 'Alto').
carencia_a_prioridad('Muy baja', 'Muy alto').

% --- Conversión de átomos normalizados a strings CSV ---

/**
 * nivel_atom_a_prioridad_string(+NivelAtom, -StringPrioridad)
 * 
 * Convierte nivel de prioridad normalizado (minúsculas, sin espacios)
 * al string correspondiente del CSV (carencia equivalente).
 */
nivel_atom_a_prioridad_string(muyalta, 'Muy bajo').
nivel_atom_a_prioridad_string(alta, 'Bajo').
nivel_atom_a_prioridad_string(media, 'Medio').
nivel_atom_a_prioridad_string(baja, 'Alto').
nivel_atom_a_prioridad_string(muybaja, 'Muy alto').

/**
 * atom_nivel_a_csv_string(+NivelAtom, -StringCSV)
 * 
 * Convierte nivel de carencia normalizado al formato del CSV.
 */
atom_nivel_a_csv_string(muyalto, 'Muy alto').
atom_nivel_a_csv_string(alto, 'Alto').
atom_nivel_a_csv_string(medio, 'Medio').
atom_nivel_a_csv_string(bajo, 'Bajo').
atom_nivel_a_csv_string(muybajo, 'Muy bajo').

% --- Nombres legibles de aspectos ---

/**
 * aspecto_display_name(+AspectoAtom, -NombreDisplay)
 * 
 * Mapea átomos de aspectos a nombres legibles para humanos.
 */
aspecto_display_name(marginacion, 'Marginación').
aspecto_display_name(rezagosocial, 'Rezago Social').
aspecto_display_name(conectividad, 'Conectividad').
aspecto_display_name(serviciosbasicos, 'Servicios Básicos').
aspecto_display_name(seguridadsocial, 'Seguridad Social').
aspecto_display_name(elementosdesalud, 'Elementos de Salud').
aspecto_display_name(educacion, 'Educación').
aspecto_display_name(desigualdad, 'Desigualdad').
aspecto_display_name(dependenciaeconomica, 'Dependencia Económica').
aspecto_display_name(calidaddevivienda, 'Calidad de Vivienda').
aspecto_display_name(seguridadalimentaria, 'Seguridad Alimentaria').

% =============================================================================
% SECCIÓN 8: ACCESO A DATOS DEL CSV
% =============================================================================

/**
 * buscar_municipio(+RutaCSV, +NombreMunicipio, -FilaMunicipio)
 * 
 * Busca y retorna la fila completa de un municipio en el archivo CSV.
 * La fila contiene todos los indicadores del municipio.
 */
buscar_municipio(RutaCSV, NombreMunicipio, FilaMunicipio) :-
    csv_read_file(RutaCSV, Filas, []),
    encontrar_fila(NombreMunicipio, Filas, FilaMunicipio).

/**
 * encontrar_fila(+NombreBuscado, +Filas, -FilaEncontrada)
 * 
 * Auxiliar que busca una fila específica por nombre de municipio.
 * El nombre se encuentra en la segunda columna del CSV.
 */
encontrar_fila(NombreBuscado, Filas, FilaEncontrada) :-
    member(FilaEncontrada, Filas),
    FilaEncontrada =.. ListaConFunctor,
    % Estructura: [Functor, Campo1_ID, Campo2_Nombre, Campo3_..., ...]
    ListaConFunctor = [_Functor, _ID, NombreEncontrado | _RestoCampos],
    NombreEncontrado == NombreBuscado,
    !.

/**
 * buscar_columna(+Aspecto, -Columna)
 * 
 * Mapea cada aspecto a su índice de columna en el CSV.
 * Los índices comienzan desde 1 (incluyendo functor del término).
 */
buscar_columna(marginacion, 4).
buscar_columna(rezagosocial, 5).
buscar_columna(conectividad, 6).
buscar_columna(serviciosbasicos, 7).
buscar_columna(elementosdesalud, 8).
buscar_columna(educacion, 9).
buscar_columna(desigualdad, 10).
buscar_columna(dependenciaeconomica, 11).
buscar_columna(calidaddevivienda, 12).
buscar_columna(seguridadalimentaria, 13).
buscar_columna(seguridadsocial, 14).

/**
 * extraer_informacion(+FilaMunicipio, +Columna, -Valor)
 * 
 * Extrae el valor de una columna específica de la fila del municipio.
 */
extraer_informacion(FilaMunicipio, Columna, Valor) :-
    FilaMunicipio =.. ListaConFunctor,
    ListaConFunctor = [_Functor | Campos],
    nth1(Columna, Campos, Valor).

% =============================================================================
% SECCIÓN 9: VALIDACIÓN DE ENTRADAS
% =============================================================================

/**
 * es_aspecto(+Aspecto)
 * 
 * Verifica que el átomo corresponda a un aspecto/indicador válido.
 */
es_aspecto(Aspecto) :-
    aspectos(ListaAspectos),
    member(Aspecto, ListaAspectos).

/**
 * es_municipio(+Municipio)
 * 
 * Verifica que el átomo corresponda a un municipio conocido.
 */
es_municipio(Municipio) :-
    municipios_conocidos(ListaMunicipios),
    member(Municipio, ListaMunicipios).

/**
 * es_nivel(+Nivel)
 * 
 * Verifica que el átomo corresponda a un nivel válido.
 */
es_nivel(Nivel) :-
    niveles(ListaNiveles),
    member(Nivel, ListaNiveles).

% =============================================================================
% SECCIÓN 10: UTILIDADES GENERALES
% =============================================================================

/**
 * list_to_formatted_string(+Lista, -StringFormateado)
 * 
 * Convierte una lista en un string legible con comas y 'y' antes del último elemento.
 * Ejemplos:
 *   [a] -> "a"
 *   [a, b] -> "a y b"
 *   [a, b, c] -> "a, b y c"
 */
list_to_formatted_string([X], X).

list_to_formatted_string([X, Y], Resultado) :-
    atomic_list_concat([X, ' y ', Y], '', Resultado).

list_to_formatted_string([H|T], Resultado) :-
    T = [_|_],  % Asegura que hay más de un elemento
    list_to_formatted_string(T, RestoFormateado),
    atomic_list_concat([H, ', ', RestoFormateado], '', Resultado).

% =============================================================================
% SECCIÓN 11: NORMALIZACIÓN DE TEXTO
% =============================================================================

/**
 * sin_acentos(+TextoConAcento, -TextoSinAcento)
 * 
 * Elimina acentos del texto para normalizar consultas en lenguaje natural.
 * Convierte caracteres acentuados a sus equivalentes sin acento.
 */
sin_acentos(ConAcento, SinAcento) :-
    % Convertir a lista de códigos
    (string(ConAcento) -> 
        string_codes(ConAcento, Codes)
    ; atom(ConAcento) ->
        atom_codes(ConAcento, Codes)
    ; 
        Codes = ConAcento
    ),
    % Procesar la lista reemplazando caracteres acentuados
    reemplazar_acentos(Codes, NewCodes),
    % Convertir de vuelta a string
    (string(ConAcento) ->
        string_codes(SinAcento, NewCodes)
    ;
        atom_codes(SinAcento, NewCodes)
    ).

/**
 * reemplazar_acentos(+ListaCodigos, -ListaCodigosSinAcentos)
 * 
 * Procesa recursivamente una lista de códigos de caracteres,
 * reemplazando acentuados por no acentuados.
 */
% Caso base: lista vacía
reemplazar_acentos([], []).

% Caso: carácter acentuado - reemplazar
reemplazar_acentos([Code|Resto], [NewCode|NewResto]) :-
    reemplazo_caracter(Code, NewCode),
    reemplazar_acentos(Resto, NewResto),
    !.

% Caso: carácter normal - mantener
reemplazar_acentos([Code|Resto], [Code|NewResto]) :-
    reemplazar_acentos(Resto, NewResto).

/**
 * reemplazo_caracter(?CodigoAcentuado, ?CodigoNormal)
 * 
 * Base de conocimiento de mapeos de caracteres acentuados.
 */
% Vocales minúsculas
reemplazo_caracter(0'á, 0'a).
reemplazo_caracter(0'é, 0'e).
reemplazo_caracter(0'í, 0'i).
reemplazo_caracter(0'ó, 0'o).
reemplazo_caracter(0'ú, 0'u).
reemplazo_caracter(0'ü, 0'u).

% Vocales mayúsculas
reemplazo_caracter(0'Á, 0'A).
reemplazo_caracter(0'É, 0'E).
reemplazo_caracter(0'Í, 0'I).
reemplazo_caracter(0'Ó, 0'O).
reemplazo_caracter(0'Ú, 0'U).
reemplazo_caracter(0'Ü, 0'U).

% Caracteres especiales
reemplazo_caracter(0'ñ, 0'n).
reemplazo_caracter(0'Ñ, 0'N).

% =============================================================================
% FIN DEL ARCHIVO
% =============================================================================















