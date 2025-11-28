# import pandas as pd
# import re
# import os
# from unidecode import unidecode

# # --- CONSTANTES ---
# # Directorio de datos crudos
# DATA_DIR = "data/raw/"
# # Directorio de datos procesados (el script lo creará si no existe)
# PROCESSED_DIR = "data/processed/"

# # Nombres de archivos (basados en tu código)
# file_names = [
#     "dataset-081025.csv",       # -> Corresponde a d1 (Dataset 2)
#     "combined_municipal.csv",     # -> Corresponde a d2 (Dataset 3 - el complejo)
#     "DATOS_MUNICIPIOS_19_10.xlsx", # -> Corresponde a d3 (Dataset 1 - el base)
# ]

# # --- FUNCIONES DE LIMPIEZA ---

# def limpiar_nombre_columna(nombre):
#     """
#     Limpia y estandariza un nombre de columna a snake_case.
#     Quita acentos, convierte a minúsculas, usa guiones bajos.
#     """
#     if not isinstance(nombre, str):
#         nombre = str(nombre)
        
#     nombre_limpio = unidecode(nombre).lower()
    
#     # Abreviaturas comunes (puedes agregar más)
#     nombre_limpio = re.sub(r'\bpoblacion\b', 'pob', nombre_limpio)
#     nombre_limpio = re.sub(r'\bmunicipio\b', 'mun', nombre_limpio)
#     nombre_limpio = re.sub(r'\bviviendas?\b', 'viv', nombre_limpio)
#     nombre_limpio = re.sub(r'\bindigena\b', 'indig', nombre_limpio)
#     nombre_limpio = re.sub(r'\bpreescolar\b', 'prees', nombre_limpio)
#     nombre_limpio = re.sub(r'\bprimaria\b', 'prim', nombre_limpio)
#     nombre_limpio = re.sub(r'\bsecundaria\b', 'sec', nombre_limpio)
    
#     # Reemplazar espacios y caracteres no alfanuméricos por guion bajo
#     nombre_limpio = re.sub(r'[^a-z0-9_]+', '_', nombre_limpio)
#     # Eliminar guiones bajos al inicio o final
#     nombre_limpio = nombre_limpio.strip('_')
#     # Reemplazar múltiples guiones bajos por uno solo
#     nombre_limpio = re.sub(r'__+', '_', nombre_limpio)
    
#     return nombre_limpio

# def filtrar_y_limpiar_ds3(df):
#     """
#     Aplica el filtrado selectivo y la limpieza agresiva al Dataset 3.
#     """
#     print(f"  [DS3] Columnas originales: {len(df.columns)}")
    
#     cols_originales = df.columns.to_list()
#     cols_a_mantener = []
    
#     # Regex para identificar años que queremos ELIMINAR
#     regex_anios_a_eliminar = re.compile(r'_(2010|2015|2016|2017)')
    
#     # --- 1. Filtrado de Columnas ---
#     for col in cols_originales:
#         col_lower = str(col).lower()
        
#         # 1.1: Mantener columnas clave
#         if col in ['agem', 'municipio', 'estado']:
#             cols_a_mantener.append(col)
#             continue
            
#         # 1.2: Eliminar IDs (excepto la clave 'agem') y metadatos
#         if col_lower.endswith(('_id', '_nation', '_state', '_nation_id', '_state_id')):
#             continue
            
#         # 1.3: Eliminar años no recientes (mantener 2020 o los que no especifican año)
#         if regex_anios_a_eliminar.search(col_lower):
#             continue
            
#         # 1.4: Eliminar 'population' del bloque de escolaridad (priorizar 'percentage')
#         if col_lower.startswith('niveles_de_escolaridad') and col_lower.endswith('__population'):
#             continue
            
#         # 1.5: Eliminar datos por sexo (priorizar totales)
#         if 'hombres' in col_lower or 'mujeres' in col_lower:
#             continue
            
#         # Si pasó todos los filtros, la mantenemos
#         cols_a_mantener.append(col)
        
#     df_filtrado = df[cols_a_mantener].copy()
#     print(f"  [DS3] Columnas después de filtrar: {len(df_filtrado.columns)}")

#     # --- 2. Renombrado Agresivo (de las columnas filtradas) ---
    
#     # Prefijos largos a eliminar
#     prefijos_a_eliminar = [
#         'niveles_de_escolaridad_de_la_poblacion_d__',
#         'pobreza_nivel_municipal__',
#         'pobreza_municipal_sexo_anio__', # Aunque ya filtramos, por si acaso
#         'unidades_de_salud_por_entidad_federativa__',
#         'visual_carencias__',
#         'distribucion_de_la_poblacion_total_segun__',
#         'poblacion_oaxaca_2016_2017__' # Eliminado por año, pero como ejemplo
#     ]
    
#     nuevos_nombres = []
#     for col in df_filtrado.columns:
#         nombre_limpio = str(col)
        
#         # Quitar prefijos
#         for p in prefijos_a_eliminar:
#             if nombre_limpio.startswith(p):
#                 nombre_limpio = nombre_limpio[len(p):]
#                 break
        
#         # Aplicar limpieza estándar (minúsculas, snake_case)
#         nombre_limpio = limpiar_nombre_columna(nombre_limpio)
#         nuevos_nombres.append(nombre_limpio)
        
#     df_filtrado.columns = nuevos_nombres
#     return df_filtrado

# # --- FUNCIÓN PRINCIPAL ---

# def main():
#     """
#     Script principal para cargar, limpiar, mapear y unir los 3 datasets.
#     """
#     print("Iniciando proceso de ETL...")
    
#     # Asegurarse de que el directorio de salida exista
#     os.makedirs(PROCESSED_DIR, exist_ok=True)
    
#     # --- 1. CARGA DE DATOS ---
#     # d1 = DS2, d2 = DS3, d3 = DS1
#     try:
#         print(f"Cargando {file_names[0]}...")
#         d1 = pd.read_csv(DATA_DIR + file_names[0], encoding="utf-8") # DS2
        
#         print(f"Cargando {file_names[1]}...")
#         d2 = pd.read_csv(DATA_DIR + file_names[1], encoding="utf-8") # DS3 (grande)
        
#         print(f"Cargando {file_names[2]}...")
#         d3 = pd.read_excel(DATA_DIR + file_names[2], engine="openpyxl") # DS1 (base)
        
#         print("Carga completada.\n")
    
#     except FileNotFoundError as e:
#         print(f"Error: No se encontró el archivo {e.filename}.")
#         print("Asegúrate de que los archivos estén en el directorio 'data/raw/'.")
#         return
#     except Exception as e:
#         print(f"Ocurrió un error inesperado durante la carga: {e}")
#         return

#     # --- 2. LIMPIEZA Y RENOMBRADO ---
    
#     print("Iniciando limpieza y renombrado...")
    
#     # 2.1: Procesar d3 (DS1 - "DATOS_MUNICIPIOS_19_10.xlsx") - Nuestro dataset base
#     d3.columns = [limpiar_nombre_columna(col) for col in d3.columns]
#     mapeo_d3 = {
#         'clave_mun': 'cve_mun',
#         'mun': 'municipio',
#         'pob_total': 'pob_total_ds1' # Identificar duplicado semántico
#     }
#     d3 = d3.rename(columns=mapeo_d3)
#     print("  [DS1] Limpieza y mapeo completados.")

#     # 2.2: Procesar d1 (DS2 - "dataset-081025.csv")
#     d1.columns = [limpiar_nombre_columna(col) for col in d1.columns]
#     mapeo_d1 = {
#         'clave_mun': 'cve_mun',
#         'mun': 'municipio',
#         'pob': 'pob_total_ds2' # Identificar duplicado semántico
#     }
#     d1 = d1.rename(columns=mapeo_d1)
#     print("  [DS2] Limpieza y mapeo completados.")

#     # 2.3: Procesar d2 (DS3 - "combined_municipal.csv") - Filtrado y limpieza agresiva
#     d2_limpio = filtrar_y_limpiar_ds3(d2)
    
#     # Mapeo manual final para d2 (DS3) - ¡El más importante!
#     # Aquí puedes acortar los nombres largos que quedaron
#     mapeo_d2 = {
#         'agem': 'cve_mun',
#         'mun': 'municipio',
        
#         # --- Ejemplo de renombrado semántico (puedes agregar más) ---
#         'poverty_rate_2020': 'tasa_pobreza_2020',
#         'extreme_poverty_rate_2020': 'tasa_pobreza_ext_2020',
        
#         # Carencias (población indígena 2020)
#         'carencia_alimentacion_nutritiva_calidad_2020_poblaci_n_indig': 'pct_indig_car_alim_2020',
#         'carencia_calidad_espacios_viv_porce_2020_poblaci_n_indig': 'pct_indig_car_viv_2020',
#         'carencia_rezago_educativo_porcentaje_2020_poblaci_n_indig': 'pct_indig_car_edu_2020',
#         'carencia_seguridad_social_porcentaje_2020_poblaci_n_indig': 'pct_indig_car_seg_soc_2020',
        
#         # Escolaridad (porcentajes)
#         'prees_o_k_nder_percentage': 'pct_pob_preescolar',
#         'primaria_percentage': 'pct_pob_primaria',
#         'secundaria_percentage': 'pct_pob_secundaria',
#         'preparatoria_o_bachillerato_general_percentage': 'pct_pob_prepa_gral',
#         'licenciatura_percentage': 'pct_pob_licenciatura',
#         'maestr_a_percentage': 'pct_pob_maestria',
#         'doctorado_percentage': 'pct_pob_doctorado'
#     }
#     d2_limpio = d2_limpio.rename(columns=mapeo_d2)
#     print("  [DS3] Mapeo manual final completado.")
#     print("\nLimpieza y renombrado finalizados.")

#     # --- 3. UNIFICACIÓN (MERGE) ---
    
#     print("Iniciando unificación de datasets...")
    
#     # Definir la clave de unión
#     merge_key = 'cve_mun'
    
#     # Preparar para la unión:
#     # d3 (DS1) es nuestra base. Eliminamos las columnas clave duplicadas
#     # de d1 (DS2) y d2 (DS3) para evitar sufijos _x, _y.
    
#     cols_a_eliminar_d1 = ['municipio']
#     cols_a_eliminar_d2 = ['municipio', 'estado'] # Asumimos que d3 (DS1) tiene 'estado'
    
#     d1_limpio = d1.drop(columns=[col for col in cols_a_eliminar_d1 if col in d1.columns])
#     d2_limpio = d2_limpio.drop(columns=[col for col in cols_a_eliminar_d2 if col in d2_limpio.columns])

#     # Unir d3 (DS1) con d1 (DS2)
#     df_unificado = pd.merge(
#         d3,
#         d1_limpio,
#         on=merge_key,
#         how='outer'  # 'outer' para no perder municipios de ningún dataset
#     )
    
#     # Unir el resultado con d2 (DS3)
#     df_unificado = pd.merge(
#         df_unificado,
#         d2_limpio,
#         on=merge_key,
#         how='outer'
#     )
    
#     print("¡Unificación completada!")

#     # --- 4. GUARDADO ---
    
#     output_filename = os.path.join(PROCESSED_DIR, "dataset_municipal_unificado.csv")
#     df_unificado.to_csv(output_filename, index=False, encoding='utf-8')
    
#     print(f"\n--- ¡Proceso Finalizado! ---")
#     print(f"Dataset unificado guardado en: {output_filename}")
#     print(f"Filas finales: {df_unificado.shape[0]}")
#     print(f"Columnas finales: {df_unificado.shape[1]}")
#     # print("\nColumnas finales:")
#     # print(df_unificado.columns.to_list())


# if __name__ == "__main__":
#     main()



import pandas as pd
import re
import os
from unidecode import unidecode

# --- CONSTANTES ---
# Directorio de datos crudos
DATA_DIR = "data/raw/"
# Directorio de datos procesados (el script lo creará si no existe)
PROCESSED_DIR = "data/processed/"

# Nombres de archivos (basados en tu código)
file_names = [
    "dataset-081025.csv",       # -> d1 (PRIORITARIO)
    "combined_municipal.csv",     # -> d2 (No prioritario)
    "DATOS_MUNICIPIOS_19_10.xlsx", # -> d3 (No prioritario)
]

# --- FUNCIONES DE LIMPIEZA ---

def limpiar_nombre_columna(nombre):
    """
    Limpia y estandariza un nombre de columna a snake_case.
    Quita acentos, convierte a minúsculas, usa guiones bajos.
    """
    if not isinstance(nombre, str):
        nombre = str(nombre)
        
    nombre_limpio = unidecode(nombre).lower()
    
    # Abreviaturas comunes (puedes agregar más)
    nombre_limpio = re.sub(r'\bpoblacion\b', 'pob', nombre_limpio)
    nombre_limpio = re.sub(r'\bmunicipio\b', 'mun', nombre_limpio)
    nombre_limpio = re.sub(r'\bviviendas?\b', 'viv', nombre_limpio)
    nombre_limpio = re.sub(r'\bindigena\b', 'indig', nombre_limpio)
    nombre_limpio = re.sub(r'\bpreescolar\b', 'prees', nombre_limpio)
    nombre_limpio = re.sub(r'\bprimaria\b', 'prim', nombre_limpio)
    nombre_limpio = re.sub(r'\bsecundaria\b', 'sec', nombre_limpio)
    
    # Reemplazar espacios y caracteres no alfanuméricos por guion bajo
    nombre_limpio = re.sub(r'[^a-z0-9_]+', '_', nombre_limpio)
    # Eliminar guiones bajos al inicio o final
    nombre_limpio = nombre_limpio.strip('_')
    # Reemplazar múltiples guiones bajos por uno solo
    nombre_limpio = re.sub(r'__+', '_', nombre_limpio)
    
    return nombre_limpio

def filtrar_y_limpiar_ds3(df):
    """
    Aplica el filtrado selectivo y la limpieza agresiva al Dataset 3.
    (Corresponde a 'combined_municipal.csv' o d2 en el script)
    """
    print(f"  [DS3/d2] Columnas originales: {len(df.columns)}")
    
    cols_originales = df.columns.to_list()
    cols_a_mantener = []
    
    # Regex para identificar años que queremos ELIMINAR
    regex_anios_a_eliminar = re.compile(r'_(2010|2015|2016|2017)')
    
    # --- 1. Filtrado de Columnas ---
    for col in cols_originales:
        col_lower = str(col).lower()
        
        # 1.1: Mantener columnas clave
        if col in ['agem', 'municipio', 'estado']:
            cols_a_mantener.append(col)
            continue
            
        # 1.2: Eliminar IDs (excepto la clave 'agem') y metadatos
        if col_lower.endswith(('_id', '_nation', '_state', '_nation_id', '_state_id')):
            continue
            
        # 1.3: Eliminar años no recientes (mantener 2020 o los que no especifican año)
        if regex_anios_a_eliminar.search(col_lower):
            continue
            
        # 1.4: Eliminar 'population' del bloque de escolaridad (priorizar 'percentage')
        if col_lower.startswith('niveles_de_escolaridad') and col_lower.endswith('__population'):
            continue
            
        # 1.5: Eliminar datos por sexo (priorizar totales)
        if 'hombres' in col_lower or 'mujeres' in col_lower:
            continue
            
        # Si pasó todos los filtros, la mantenemos
        cols_a_mantener.append(col)
        
    df_filtrado = df[cols_a_mantener].copy()
    print(f"  [DS3/d2] Columnas después de filtrar: {len(df_filtrado.columns)}")

    # --- 2. Renombrado Agresivo (de las columnas filtradas) ---
    
    # Prefijos largos a eliminar
    prefijos_a_eliminar = [
        'niveles_de_escolaridad_de_la_poblacion_d__',
        'pobreza_nivel_municipal__',
        'pobreza_municipal_sexo_anio__', # Aunque ya filtramos, por si acaso
        'unidades_de_salud_por_entidad_federativa__',
        'visual_carencias__',
        'distribucion_de_la_poblacion_total_segun__',
    ]
    
    nuevos_nombres = []
    for col in df_filtrado.columns:
        nombre_limpio = str(col)
        
        # Quitar prefijos
        for p in prefijos_a_eliminar:
            if nombre_limpio.startswith(p):
                nombre_limpio = nombre_limpio[len(p):]
                break
        
        # Aplicar limpieza estándar (minúsculas, snake_case)
        nombre_limpio = limpiar_nombre_columna(nombre_limpio)
        nuevos_nombres.append(nombre_limpio)
        
    df_filtrado.columns = nuevos_nombres
    return df_filtrado

# --- FUNCIÓN PRINCIPAL ---

def main():
    """
    Script principal para cargar, limpiar, mapear y unir los 3 datasets.
    """
    print("Iniciando proceso de ETL...")
    
    # Asegurarse de que el directorio de salida exista
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    # --- 1. CARGA DE DATOS ---
    try:
        print(f"Cargando (Prioritario) {file_names[0]}...")
        d1 = pd.read_csv(DATA_DIR + file_names[0], encoding="utf-8") # DS2 (PRIORITARIO)
        
        print(f"Cargando {file_names[1]}...")
        d2 = pd.read_csv(DATA_DIR + file_names[1], encoding="utf-8") # DS3 (grande)
        
        print(f"Cargando {file_names[2]}...")
        d3 = pd.read_excel(DATA_DIR + file_names[2], engine="openpyxl") # DS1 (base)
        
        print("Carga completada.\n")
    
    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo {e.filename}.")
        print("Asegúrate de que los archivos estén en el directorio 'data/raw/'.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la carga: {e}")
        return

    # --- 2. LIMPIEZA Y RENOMBRADO ---
    
    print("Iniciando limpieza y renombrado...")
    
    # 2.1: Procesar d1 (DS2 - "dataset-081025.csv") - PRIORITARIO
    d1.columns = [limpiar_nombre_columna(col) for col in d1.columns]
    mapeo_d1 = {
        'clave_mun': 'cve_mun',
        'mun': 'municipio',
        'pob': 'pob_total_ds2' # Identificar duplicado semántico
    }
    d1 = d1.rename(columns=mapeo_d1)
    print("  [DS2/d1] Limpieza y mapeo (Prioritario) completados.")

    # 2.2: Procesar d3 (DS1 - "DATOS_MUNICIPIOS_19_10.xlsx") - No prioritario
    d3.columns = [limpiar_nombre_columna(col) for col in d3.columns]
    mapeo_d3 = {
        'clave_mun': 'cve_mun',
        'mun': 'municipio',
        'pob_total': 'pob_total_ds1' # Identificar duplicado semántico
    }
    d3 = d3.rename(columns=mapeo_d3)
    print("  [DS1/d3] Limpieza y mapeo completados.")

    # 2.3: Procesar d2 (DS3 - "combined_municipal.csv") - No prioritario
    d2_limpio = filtrar_y_limpiar_ds3(d2)
    
    # Mapeo manual final para d2 (DS3)
    mapeo_d2 = {
        'agem': 'cve_mun',
        'mun': 'municipio',
        'poverty_rate_2020': 'tasa_pobreza_2020',
        'extreme_poverty_rate_2020': 'tasa_pobreza_ext_2020',
        # ... (puedes añadir más mapeos como en el script anterior)
        'carencia_rezago_educativo_porcentaje_2020_poblaci_n_indig': 'pct_indig_car_edu_2020',
        'prees_o_k_nder_percentage': 'pct_pob_preescolar',
        'primaria_percentage': 'pct_pob_primaria',
        'secundaria_percentage': 'pct_pob_secundaria',
    }
    d2_limpio = d2_limpio.rename(columns=mapeo_d2)
    print("  [DS3/d2] Mapeo manual final completado.")
    print("\nLimpieza y renombrado finalizados.")

    # --- 3. UNIFICACIÓN (MERGE) CON PRIORIZACIÓN ---
    
    print("Iniciando unificación de datasets...")
    
    # Definir la clave de unión
    merge_key = 'cve_mun'
    
    # Definir nuestro dataframe base (PRIORITARIO)
    df_base = d1
    print(f"  Dataframe base (prioritario) es 'd1' ({file_names[0]})")
    
    # Obtener la lista de columnas prioritarias
    priority_cols = set(df_base.columns)
    
    # --- Preparar d3 (DS1) para la unión ---
    cols_d3 = set(d3.columns)
    # Encontrar columnas duplicadas que NO sean la clave de unión
    cols_to_drop_d3 = (cols_d3 & priority_cols) - {merge_key}
    if cols_to_drop_d3:
        print(f"  [d3] Eliminando {len(cols_to_drop_d3)} columnas duplicadas: {cols_to_drop_d3}")
        d3_limpio = d3.drop(columns=list(cols_to_drop_d3))
    else:
        d3_limpio = d3
        
    # --- Preparar d2_limpio (DS3) para la unión ---
    cols_d2 = set(d2_limpio.columns)
    # Encontrar columnas duplicadas que NO sean la clave de unión
    cols_to_drop_d2 = (cols_d2 & priority_cols) - {merge_key}
    if cols_to_drop_d2:
        print(f"  [d2] Eliminando {len(cols_to_drop_d2)} columnas duplicadas: {cols_to_drop_d2}")
        d2_limpio_final = d2_limpio.drop(columns=list(cols_to_drop_d2))
    else:
        d2_limpio_final = d2_limpio

    # --- Unir todo ---
    print("  Realizando merge...")
    
    # Unir la base (d1) con d3
    df_unificado = pd.merge(
        df_base,
        d3_limpio,
        on=merge_key,
        how='outer'  # 'outer' para no perder municipios de ningún dataset
    )
    
    # Unir el resultado con d2
    df_unificado = pd.merge(
        df_unificado,
        d2_limpio_final,
        on=merge_key,
        how='outer'
    )
    
    print("¡Unificación completada!")

    # --- 4. GUARDADO ---
    
    output_filename = os.path.join(PROCESSED_DIR, "dataset_municipal_unificado_priorizado.csv")
    df_unificado.to_csv(output_filename, index=False, encoding='utf-8')
    
    print(f"\n--- ¡Proceso Finalizado! ---")
    print(f"Dataset unificado guardado en: {output_filename}")
    print(f"Filas finales: {df_unificado.shape[0]}")
    print(f"Columnas finales: {df_unificado.shape[1]}")


if __name__ == "__main__":
    main()