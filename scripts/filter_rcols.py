import pandas as pd

PROCESSED_DIR = "data/processed/"


def main():
    # load dataset
    df = pd.read_csv(PROCESSED_DIR + "dataset_municipal_unificado.csv")
    
    # 1. Lista de todas las columnas que SÍ queremos eliminar
    columnas_a_eliminar = [
        # -- Otros
        # Columna de nombre de estado
        'estado',

        # --- 1. Identificadores y Metadatos ---
        'estado',
        # 'lugar_que_ocupa_en_el_contexto_estatal',
        # 'lugar_que_ocupa_en_el_contexto_nacional',
        
        # --- 2. Variables Categóricas Redundantes (Niveles) ---
        'nivel_hacinamiento',
        'nivel_agua_entubada',
        'nivel_drenaje',
        'nivel_piso_tierra',
        'nivel_uso_lena',
        
        # --- 3. Variables Granulares (Ruido - Shares sectoriales) ---
        'share_11',
        'share_31_33',
        'share_46',
        'share_48_49',
        'share_61',
        'share_62',

        'personas20_total',
        'viviendas20_total',

        # --- Grupo 1: Duplicados de Pobreza Indígena ---
        'pobreza_porcentaje_2020_poblaci_n_ind_gena',
        'carencia_rezago_educativo_porcentaje_2020_poblaci_n_ind_gena',
        'carencia_servicios_de_salud_porcentaje_2020_poblaci_n_ind_gena',
        'carencia_seguridad_social_porcentaje_2020_poblaci_n_ind_gena',
        'carencia_alimentacion_nutritiva_calidad_2020_poblaci_n_ind_gena',
        'carencia_servicios_basicos_vivienda_porc_2020_poblaci_n_ind_gena',
        'carencia_calidad_espacios_vivienda_porce_2020_poblaci_n_ind_gena',
        'ingreso_inferior_a_lpi_porcentaje_2020_poblaci_n_ind_gena',
        'poblacion_2020_poblaci_n_ind_gena', # Este es un conteo, no un %

        'ind_margi_norm',  # Redundante con ind_margi

        # --- Grupo 3: Duplicados de Educación ---
        'pob_analfabeta', # Es conteo, mejor usar tasa/pct
        'por_mas_15_analfabeta', # Redundante con tasa_de_analfabetizacion
        'grad_escol_prom_15', # Redundante con grado_promedio_de_escolaridad

        'clinics',
        'establishments', # Redundante con clinics
        'beds',
        'bed_average',
        'health_center_average',

        # --- Grupo 6: Totales de Población y Vivienda ---
        'personas20_total',
        'viviendas20_total',
        'total_de_viv',
        'total_de_viv_habitadas',

        # Duplicados de Municipio (eliminamos las 2 instancias de 'municipality')
        'municipality1', 
        'municipality2', 
        
        # Duplicados de Población Total
        'pob_total_ds1',
        'population1',
        'population2',
        
        # Duplicado de Población Afrodescendiente
        'pob_que_se_considera_afromexicana_o_afrodescendiente',
        
        # Duplicado de Población Analfabeta
        'pob_de_15_anos_y_mas_analfabeta',
        
        # Duplicado de Población con Discapacidad (conservamos 'pob_con_discapacidad')
        'pob_discapacidad',
        
        # Duplicados de Índices de Marginación (CONAPO 2020)
        'im_2020',
        'gm_2020',
        'imn_2020',
        
        # Duplicado de Viviendas
        'total_viviendas_est',
        
        # Duplicado de Tasa de Pobreza
        'tasa_pobreza_2020',
        
        # Duplicado de Tasa de Pobreza Extrema
        'tasa_pobreza_ext_2020',
        
        # Duplicado de Densidad DENUE
        'denue_density_per_1000_2020',
        
        # Columna de Población Indígena (Sección 3)
        'poblacion_2020_poblaci_n_ind_gena',

        'poverty_rate',
        'extreme_poverty_rate',
    ]

    # 2. Creamos un nuevo DataFrame 'df_limpio' sin esas columnas
    # Usamos errors='ignore' para que el script no falle si una columna
    # de la lista ya fue eliminada (ej. 'municipality' que aparece 2 veces).
    # df_limpio = df.drop(columns=columnas_a_eliminar, errors='ignore')
    df_limpio = df.drop(columns=columnas_a_eliminar)

    # Renombrar columna 'pob_total_ds2' a 'pob_total'
    df_limpio = df_limpio.rename(columns={'pob_total_ds2': 'pob_total'})

    # Renombrar columna 'pob_de_3_anos_y_mas_que_habla_alguna_lengua_indig' a 'pob_que_habla_lengua_indigena'
    df_limpio = df_limpio.rename(columns={'pob_de_3_anos_y_mas_que_habla_alguna_lengua_indig': 'pob_que_habla_lengua_indigena'})

    # 3. (Opcional) Verificamos las columnas restantes
    print("Columnas restantes en el DataFrame limpio:")
    print(df_limpio.columns.to_list())

    # identifica si hay columnas con datos faltantes
    missing_data_columns = df_limpio.columns[df_limpio.isnull().any()].to_list()
    if missing_data_columns:
        print("\nColumnas con datos faltantes:")
        for col in missing_data_columns:
            missing_count = df_limpio[col].isnull().sum()
            print(f"- {col}: {missing_count} valores faltantes")
    else:
        print("\nNo hay columnas con datos faltantes.")


    # Guardamos el DataFrame limpio en un nuevo archivo CSV
    df_limpio.to_csv(PROCESSED_DIR + "dataset_municipal.csv", index=False)
    

if __name__ == "__main__":
    main()
