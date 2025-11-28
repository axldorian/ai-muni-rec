"""
Ejemplo de uso de Procesamiento_lenguaje.pl con pyswip
"""

from pyswip import Prolog

# Inicializar Prolog
prolog = Prolog()
prolog.consult("knowledge/Procesamiento_lenguaje.pl")


def procesar_consulta(consulta_texto):
    """
    Procesa una consulta en lenguaje natural y retorna el resultado.
    
    Args:
        consulta_texto (str): Consulta en lenguaje natural
        
    Returns:
        str: Resultado de la consulta
    """
    query = f"procesar_consulta('{consulta_texto}', R)"
    resultados = list(prolog.query(query))
    
    if resultados:
        return resultados[0]['R']
    return None


def parsear_datos_completos(datos_str):
    """
    Parsea los datos completos del municipio desde el formato estructurado.
    
    Formato entrada: "municipio|aspecto1:nivel1|aspecto2:nivel2|..."
    
    Args:
        datos_str (str): String con datos en formato estructurado
        
    Returns:
        dict: Diccionario con municipio y aspectos
    """
    partes = datos_str.split('|')
    municipio = partes[0]
    
    aspectos = {}
    for parte in partes[1:]:
        if ':' in parte:
            aspecto, nivel = parte.split(':', 1)
            aspectos[aspecto] = nivel
    
    return {
        'municipio': municipio,
        'aspectos': aspectos
    }


# =============================================================================
# EJEMPLOS DE USO
# =============================================================================

def ejemplo_1_consulta_simple():
    """Ejemplo 1: Consultar el nivel de un aspecto específico"""
    print("=" * 60)
    print("EJEMPLO 1: Consulta simple de un aspecto")
    print("=" * 60)
    
    resultado = procesar_consulta('cual es el estado de educacion de oaxacadejuarez')
    print(f"Pregunta: ¿Cuál es el estado de educación de Oaxaca de Juárez?")
    print(f"Respuesta: {resultado}\n")


def ejemplo_2_datos_completos():
    """Ejemplo 2: Obtener y parsear datos completos del municipio"""
    print("=" * 60)
    print("EJEMPLO 2: Datos completos del municipio")
    print("=" * 60)
    
    resultado = procesar_consulta('cual es el estado de oaxacadejuarez')
    datos = parsear_datos_completos(resultado)
    
    print(f"Municipio: {datos['municipio']}")
    print("\nIndicadores:")
    print("-" * 60)
    for aspecto, nivel in datos['aspectos'].items():
        print(f"  {aspecto:30} | {nivel}")
    print()


def ejemplo_3_prioridad():
    """Ejemplo 3: Consultar prioridad de apoyo"""
    print("=" * 60)
    print("EJEMPLO 3: Prioridad de apoyo")
    print("=" * 60)
    
    resultado = procesar_consulta('que prioridad tiene educacion de oaxacadejuarez')
    print(f"Pregunta: ¿Qué prioridad tiene educación en Oaxaca de Juárez?")
    print(f"Respuesta: {resultado}\n")


def ejemplo_4_aspectos_por_nivel():
    """Ejemplo 4: Aspectos con nivel específico"""
    print("=" * 60)
    print("EJEMPLO 4: Aspectos con nivel alto")
    print("=" * 60)
    
    resultado = procesar_consulta('cuales son los aspectos de oaxacadejuarez con nivel alto')
    print(f"Pregunta: ¿Cuáles aspectos tienen nivel alto?")
    print(f"Respuesta: {resultado}\n")


def ejemplo_5_con_acentos():
    """Ejemplo 5: Consulta con acentos y mayúsculas"""
    print("=" * 60)
    print("EJEMPLO 5: Con acentos y mayúsculas")
    print("=" * 60)
    
    resultado = procesar_consulta('¿Cuál es el ESTADO de EDUCACIÓN de oaxacadejuarez?')
    print(f"Pregunta: ¿Cuál es el ESTADO de EDUCACIÓN de oaxacadejuarez?")
    print(f"Respuesta: {resultado}\n")


def ejemplo_6_multiples_municipios():
    """Ejemplo 6: Comparar múltiples municipios"""
    print("=" * 60)
    print("EJEMPLO 6: Comparación entre municipios")
    print("=" * 60)
    
    municipios = ['oaxacadejuarez', 'santamariadeltu le']
    aspecto = 'educacion'
    
    print(f"Comparando '{aspecto}' entre municipios:\n")
    
    for muni in municipios:
        resultado = procesar_consulta(f'cual es el estado de {aspecto} de {muni}')
        print(f"  {muni:25} | {resultado}")
    print()


def ejemplo_7_tabla_formateada():
    """Ejemplo 7: Mostrar datos en tabla formateada"""
    print("=" * 60)
    print("EJEMPLO 7: Tabla formateada de indicadores")
    print("=" * 60)
    
    resultado = procesar_consulta('cual es el estado de oaxacadejuarez')
    datos = parsear_datos_completos(resultado)
    
    # Crear tabla bonita
    print(f"\n{'='*60}")
    print(f" DATOS COMPLETOS DE: {datos['municipio'].upper()}")
    print(f"{'-'*60}")
    print(f" {'Aspecto':<30} | {'Nivel'}")
    print(f"{'='*60}")
    
    for aspecto, nivel in datos['aspectos'].items():
        print(f" {aspecto:<30} | {nivel}")
    
    print(f"{'='*60}\n")


def ejemplo_8_filtrar_niveles_altos():
    """Ejemplo 8: Filtrar solo niveles altos/muy altos"""
    print("=" * 60)
    print("EJEMPLO 8: Aspectos con carencia alta")
    print("=" * 60)
    
    resultado = procesar_consulta('cual es el estado de oaxacadejuarez')
    datos = parsear_datos_completos(resultado)
    
    niveles_preocupantes = ['Alto', 'Muy alto']
    aspectos_preocupantes = {
        aspecto: nivel 
        for aspecto, nivel in datos['aspectos'].items()
        if nivel in niveles_preocupantes
    }
    
    if aspectos_preocupantes:
        print(f"Aspectos que requieren atención en {datos['municipio']}:\n")
        for aspecto, nivel in aspectos_preocupantes.items():
            print(f"  ⚠️  {aspecto}: {nivel}")
    else:
        print(f"No hay aspectos con carencia alta en {datos['municipio']}")
    print()


def ejemplo_9_estadisticas():
    """Ejemplo 9: Generar estadísticas del municipio"""
    print("=" * 60)
    print("EJEMPLO 9: Estadísticas del municipio")
    print("=" * 60)
    
    resultado = procesar_consulta('cual es el estado de oaxacadejuarez')
    datos = parsear_datos_completos(resultado)
    
    # Contar niveles
    conteo_niveles = {}
    for nivel in datos['aspectos'].values():
        conteo_niveles[nivel] = conteo_niveles.get(nivel, 0) + 1
    
    print(f"Municipio: {datos['municipio']}")
    print(f"Total de indicadores: {len(datos['aspectos'])}\n")
    print("Distribución de niveles:")
    for nivel, cantidad in sorted(conteo_niveles.items()):
        porcentaje = (cantidad / len(datos['aspectos'])) * 100
        barra = '█' * int(porcentaje / 5)
        print(f"  {nivel:15} | {cantidad:2} ({porcentaje:5.1f}%) {barra}")
    print()


def ejecutar_todos_los_ejemplos():
    """Ejecuta todos los ejemplos en secuencia"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "EJEMPLOS DE USO - PYSWIP + PROLOG" + " " * 14 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")
    
    ejemplo_1_consulta_simple()
    ejemplo_2_datos_completos()
    ejemplo_3_prioridad()
    ejemplo_4_aspectos_por_nivel()
    ejemplo_5_con_acentos()
    ejemplo_6_multiples_municipios()
    ejemplo_7_tabla_formateada()
    ejemplo_8_filtrar_niveles_altos()
    ejemplo_9_estadisticas()
    
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "TODOS LOS EJEMPLOS COMPLETADOS" + " " * 17 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")


if __name__ == "__main__":
    ejecutar_todos_los_ejemplos()
