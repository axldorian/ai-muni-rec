import pandas as pd


def grade_connectivity(row: pd.Series):
    """
    Asigna el nivel de conectividad basado en el porcentaje de viviendas con acceso
    a internet, computadoras y celular.
    """
    # Verificar datos faltantes
    if (
        pd.isna(row["viv"])
        or pd.isna(row["viv_internet"])
        or pd.isna(row["viv_computadoras"])
        or pd.isna(row["viv_celular"])
    ):
        return "Sin datos"

    if row["viv"] == 0:
        return "Sin datos"

    pct_internet = (row["viv_internet"] / row["viv"]) * 100
    pct_computadoras = (row["viv_computadoras"] / row["viv"]) * 100
    pct_celular = (row["viv_celular"] / row["viv"]) * 100

    # Promedio ponderado (internet y celular tienen más peso)
    promedio = pct_internet * 0.4 + pct_celular * 0.4 + pct_computadoras * 0.2

    if promedio >= 70:
        return "Alto"
    elif promedio >= 40:
        return "Medio"
    elif promedio >= 20:
        return "Bajo"
    else:
        return "Muy bajo"


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
        return "Alto"
    elif pct_carencias <= 30:
        return "Medio"
    elif pct_carencias <= 60:
        return "Bajo"
    else:
        return "Muy bajo"


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
        return "Alto"
    elif elementos_por_mil >= 2:
        return "Medio"
    elif elementos_por_mil >= 1:
        return "Bajo"
    else:
        return "Muy bajo"


def grade_education(row: pd.Series):
    """
    Asigna el nivel de rezago educativo basado en el porcentaje de población analfabeta
    y el grado de escolaridad promedio.
    """
    # Verificar datos faltantes
    if (
        pd.isna(row["pob_total"])
        or pd.isna(row["tasa_de_analfabetizacion"])
        or pd.isna(row["grado_promedio_de_escolaridad"])
    ):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"

    # Combinación de factores (mayor alfabetización y escolaridad = menor rezago)
    pct_analfabetizacion = row["tasa_de_analfabetizacion"]
    escolaridad = row["grado_promedio_de_escolaridad"]
    score = (pct_analfabetizacion * 0.6) + ((12 - escolaridad) * 0.4)

    if score >= 30:
        return "Muy alto"
    elif score >= 15:
        return "Alto"
    elif score >= 5:
        return "Medio"
    else:
        return "Bajo"


# Indicador que utilice la caracteristica "gini"
def grade_gini(row: pd.Series):
    """
    Asigna el nivel de desigualdad basado en el índice de Gini.
    """
    # Verificar datos faltantes
    if pd.isna(row["gini"]):
        return "Sin datos"

    # if row["gini"] < 0.2:
    #     return "Baja desigualdad"
    # elif row["gini"] < 0.4:
    #     return "Desigualdad moderada"
    # elif row["gini"] < 0.6:
    #     return "Alta desigualdad"
    # else:
    #     return "Muy alta desigualdad"

    if row["gini"] >= 0.6:
        return "Muy alta"
    elif row["gini"] >= 0.4:
        return "Alta"
    elif row["gini"] >= 0.2:
        return "Media"
    else:
        return "Baja"


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

    # if row["tasa_ingresos"] < 0.05:
    #     return "Baja dependencia económica"
    # elif row["tasa_ingresos"] < 0.15:
    #     return "Dependencia económica moderada"
    # elif row["tasa_ingresos"] < 0.25:
    #     return "Alta dependencia económica"
    # else:
    #     return "Muy alta dependencia económica"

    if row["tasa_ingresos"] >= 0.25:
        return "Muy alta"
    elif row["tasa_ingresos"] >= 0.15:
        return "Alta"
    elif row["tasa_ingresos"] >= 0.05:
        return "Media"
    else:
        return "Baja"


# --------------------------


def grade_housing_quality(row: pd.Series):
    """
    Evalúa la calidad de vivienda basado en materiales y hacinamiento.
    """
    if (
        pd.isna(row["viv"])
        or pd.isna(row["pct_piso_tierra"])
        or pd.isna(row["pct_hacinamiento"])
        # or pd.isna(row["pct_muros_irregulares"])
    ):
        return "Sin datos"

    if row["viv"] == 0:
        return "Sin datos"

    pct_piso_tierra = row["pct_piso_tierra"]
    hacinamiento = row["pct_hacinamiento"]

    # Score combinado (menos piso tierra y menos hacinamiento = mejor)
    score = (pct_piso_tierra * 0.5) + (hacinamiento * 0.5)

    if score <= 25:
        return "Alta"
    elif score <= 50:
        return "Media"
    elif score <= 75:
        return "Baja"
    else:
        return "Muy baja"


def grade_food_security(row: pd.Series):
    """
    Evalúa la seguridad alimentaria basado en carencias alimentarias.
    """
    if pd.isna(row["pob_total"]) or pd.isna(row["pob_car_alimentacion"]):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"

    pct_carencia = (row["pob_car_alimentacion"] / row["pob_total"]) * 100

    if pct_carencia <= 10:
        return "Alta"
    elif pct_carencia <= 25:
        return "Media"
    elif pct_carencia <= 50:
        return "Baja"
    else:
        return "Muy baja"


def grade_social_security(row: pd.Series):
    """
    Evalúa el acceso a servicios de salud/seguridad social.
    """
    if pd.isna(row["pob_total"]) or pd.isna(row["pob_car_salud"]):
        return "Sin datos"

    if row["pob_total"] == 0:
        return "Sin datos"

    pct_sin_servicios = (row["pob_car_salud"] / row["pob_total"]) * 100

    if pct_sin_servicios <= 15:
        return "Alta"
    elif pct_sin_servicios <= 35:
        return "Media"
    elif pct_sin_servicios <= 60:
        return "Baja"
    else:
        return "Muy baja"


def generate_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """
    Genera un DataFrame con los indicadores categorizados para cada municipio.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame que contiene los datos municipales.

    Returns
    -------
        pd.DataFrame: DataFrame con los indicadores categorizados por municipio.
    """
    indicators = []

    for _, row in data.iterrows():
        profile = {
            "cve_mun": row["cve_mun"],
            "municipio": row["municipio"],
            "grad_margi": row["grad_margi"],
            "grad_rez_social": row["grad_rez_social"],
            "conectividad": grade_connectivity(row),
            "servicios_basicos": grade_basic_services(row),
            "elementos_salud": grade_health(row),
            "educacion": grade_education(row),
            "desigualdad": grade_gini(row),
            "dependencia_economica": grade_income_rate(row),
            "calidad_vivienda": grade_housing_quality(row),
            "seguridad_alimentaria": grade_food_security(row),
            "seguridad_social": grade_social_security(row),
        }
        indicators.append(profile)

    return pd.DataFrame(indicators)


def municipality_profile(data, nombre_municipio, print_profile=True):
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
        "cve_mun": mun["cve_mun"],
        "municipio": mun["municipio"],
        "grad_margi": mun["grad_margi"],
        "grad_rez_social": mun["grad_rez_social"],
        "conectividad": grade_connectivity(mun),
        "servicios_basicos": grade_basic_services(mun),
        "elementos_salud": grade_health(mun),
        "educacion": grade_education(mun),
        "desigualdad": grade_gini(mun),
        "dependencia_economica": grade_income_rate(mun),
        "calidad_vivienda": grade_housing_quality(mun),
        "seguridad_alimentaria": grade_food_security(mun),
        "seguridad_social": grade_social_security(mun),
    }

    if print_profile:
        # Imprimir perfil
        header = f" PERFIL DEL MUNICIPIO: {profile['municipio'].upper()} "
        print(f"\n{header:=^80}")

        print(f"\nRESUMEN DEL PERFIL:")
        print(f"  • Marginación: {profile['marginacion']}")
        print(f"  • Rezago social: {profile['rezago_social']}")
        print(f"  • Conectividad: {profile['conectividad']}")
        print(f"  • Servicios básicos: {profile['servicios_basicos']}")
        print(f"  • Elementos de salud: {profile['elementos_salud']}")
        print(f"  • Educación: {profile['educacion']}")
        print(f"  • Desigualdad: {profile['desigualdad']}")
        print(f"  • Dependencia económica: {profile['dependencia_economica']}")
        print(f"  • Calidad de vivienda: {profile['calidad_vivienda']}")
        print(f"  • Grado de acceso a alimentos: {profile['seguridad_alimentaria']}")
        print(
            f"  • Grado de acceso a servicios de salud: {profile['seguridad_social']}"
        )
        print("=" * 80)

    return profile


def print_munprofile(data, nombre_municipio):
    """
    Imprime el perfil descriptivo del municipio basado en sus indicadores.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame que contiene los datos municipales.
    nombre_municipio : str
        Nombre del municipio a analizar.
    """

    profile = data[data["municipio"] == nombre_municipio].iloc[0]

    # Imprimir perfil
    header = f" PERFIL DEL MUNICIPIO: {profile['municipio'].upper()} "
    print(f"\n{header:=^80}")

    print(f"\nRESUMEN DEL PERFIL:")
    print(f"  • Marginación: {profile['grad_margi']}")
    print(f"  • Rezago social: {profile['grad_rez_social']}")
    print(f"  • Conectividad: {profile['conectividad']}")
    print(f"  • Servicios básicos: {profile['servicios_basicos']}")
    print(f"  • Elementos de salud: {profile['elementos_salud']}")
    print(f"  • Educación: {profile['educacion']}")
    print(f"  • Desigualdad: {profile['desigualdad']}")
    print(f"  • Dependencia económica: {profile['dependencia_economica']}")
    print(f"  • Calidad de vivienda: {profile['calidad_vivienda']}")
    print(f"  • Grado de acceso a alimentos: {profile['seguridad_alimentaria']}")
    print(f"  • Grado de acceso a servicios de salud: {profile['seguridad_social']}")
    print("=" * 80)
