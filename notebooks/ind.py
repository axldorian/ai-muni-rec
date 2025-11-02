import pandas as pd


def grade_connectivity(row: pd.Series):
    """
    Asigna el nivel de conectividad basado en el porcentaje de viviendas con acceso
    a internet, computadoras y celular.
    """
    # Verificar datos faltantes
    if pd.isna(row["viv"]) or pd.isna(row["viv_internet"]) or \
       pd.isna(row["viv_computadoras"]) or pd.isna(row["viv_celular"]):
        return "Sin datos"

    if row["viv"] == 0:
        return "Sin datos"

    pct_internet = (row["viv_internet"] / row["viv"]) * 100
    pct_computadoras = (row["viv_computadoras"] / row["viv"]) * 100
    pct_celular = (row["viv_celular"] / row["viv"]) * 100

    # Promedio ponderado (internet y celular tienen más peso)
    promedio = pct_internet * 0.4 + pct_celular * 0.4 + pct_computadoras * 0.2

    if promedio >= 70:
        return "Alta conectividad"
    elif promedio >= 40:
        return "Conectividad media"
    elif promedio >= 20:
        return "Baja conectividad"
    else:
        return "Muy baja conectividad"


def grade_basic_services(row: pd.Series):
    """
    Asigna el nivel de acceso a servicios básicos basado en las carencias.
    """
    # Verificar datos faltantes
    if pd.isna(row["pob_total"]) or pd.isna(row["pob_car_ser_basicos"]):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"

    pct_carencias = (row["pob_car_ser_basicos"] / row["pob_total"]) * 100

    if pct_carencias <= 10:
        return "Buen acceso a servicios básicos"
    elif pct_carencias <= 30:
        return "Acceso moderado a servicios básicos"
    elif pct_carencias <= 60:
        return "Bajo acceso a servicios básicos"
    else:
        return "Muy bajo acceso a servicios básicos"


def grade_health(row: pd.Series):
    """
    Asigna el nivel de acceso a servicios de salud basado en el número total de elementos
    de salud por cada 1000 habitantes.
    """
    # Verificar datos faltantes
    if pd.isna(row["pob_total"]) or pd.isna(row["total_elementos_salud"]):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"

    elementos_por_mil = (row["total_elementos_salud"] / row["pob_total"]) * 1000

    if elementos_por_mil >= 5:
        return "Buen acceso a servicios de salud"
    elif elementos_por_mil >= 2:
        return "Acceso moderado a servicios de salud"
    elif elementos_por_mil >= 1:
        return "Bajo acceso a servicios de salud"
    else:
        return "Muy bajo acceso a servicios de salud"


def grade_education(row: pd.Series):
    """
    Asigna el nivel de rezago educativo basado en el porcentaje de población analfabeta
    y el grado de escolaridad promedio.
    """
    # Verificar datos faltantes
    if pd.isna(row["pob_total"]) or pd.isna(row["tasa_de_analfabetizacion"]) or \
       pd.isna(row["grado_promedio_de_escolaridad"]):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"


    # Combinación de factores (mayor alfabetización y escolaridad = menor rezago)
    pct_analfabetizacion = row["tasa_de_analfabetizacion"]
    escolaridad = row["grado_promedio_de_escolaridad"]
    score = (pct_analfabetizacion * 0.6) + ((12 - escolaridad) * 0.4)

    if score <= 5:
        return "Bajo rezago educativo"
    elif score <= 15:
        return "Rezago educativo moderado"
    elif score <= 30:
        return "Alto rezago educativo"
    else:
        return "Muy alto rezago educativo"

# Indicador que utilice la caracteristica "gini"
def grade_gini(row: pd.Series):
    """
    Asigna el nivel de desigualdad basado en el índice de Gini.
    """
    # Verificar datos faltantes
    if pd.isna(row["gini"]):
        return "Sin datos"
    
    if row["gini"] < 0.2:
        return "Baja desigualdad"
    elif row["gini"] < 0.4:
        return "Desigualdad moderada"
    elif row["gini"] < 0.6:
        return "Alta desigualdad"
    else:
        return "Muy alta desigualdad"


# Indicador que utilice la caracteristica "tasa_ingresos"
# (porcentaje adicional de dinero que entra a las arcas publicas de un municipio,
# la mayoria de datos se encuentra entre valores del 0.10 al 0.20)
def grade_income_rate(row: pd.Series):
    """
    Asigna el nivel de dependencia económica basado en la tasa de ingresos.
    """
    # Verificar datos faltantes
    if pd.isna(row["tasa_ingresos"]):
        return "Sin datos"
    
    if row["tasa_ingresos"] < 0.05:
        return "Baja dependencia económica"
    elif row["tasa_ingresos"] < 0.15:
        return "Dependencia económica moderada"
    elif row["tasa_ingresos"] < 0.25:
        return "Alta dependencia económica"
    else:
        return "Muy alta dependencia económica"


def municipality_profile(data, nombre_municipio):
    """
    Genera un perfil descriptivo del municipio basado en sus indicadores,
    clasificando sus características en categorías cualitativas.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame que contiene los datos municipales.
    nombre_municipio : str
        Nombre del municipio a analizar.

    Returns
    -------
        dict: Diccionario con el perfil categorizado del municipio
    """
    # Buscar el municipio
    municipio = data[data["municipio"].str.lower() == nombre_municipio.lower()]

    if municipio.empty:
        print(f"Municipio '{nombre_municipio}' no encontrado.")
        return None

    # Obtener la primera fila
    mun = municipio.iloc[0]

    # Aplicar funciones de clasificación
    profile = {
        "municipio": mun["municipio"],
        "clave_mun": mun["cve_mun"],
        "marginacion": mun["grad_margi"],
        "rezago_social": mun["grad_rez_social"],
        "conectividad": grade_connectivity(mun),
        "servicios_basicos": grade_basic_services(mun),
        "salud": grade_health(mun),
        "educacion": grade_education(mun),
        "desigualdad": grade_gini(mun),
        "dependencia_economica": grade_income_rate(mun),
    }

    # Imprimir perfil
    header = f" PERFIL DEL MUNICIPIO: {profile['municipio'].upper()} "
    print(f"\n{header:=^80}")

    print(f"\nRESUMEN DEL PERFIL:")
    print(f"  • Marginación: {profile['marginacion']}")
    print(f"  • Rezago social: {profile['rezago_social']}")
    print(f"  • Conectividad: {profile['conectividad']}")
    print(f"  • Servicios básicos: {profile['servicios_basicos']}")
    print(f"  • Salud: {profile['salud']}")
    print(f"  • Educación: {profile['educacion']}")
    print(f"  • Desigualdad: {profile['desigualdad']}")
    print(f"  • Dependencia económica: {profile['dependencia_economica']}")

    print("=" * 80)

    return profile
