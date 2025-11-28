import pandas as pd

PROCESSED_DIR = "data/processed/"


def main():
    df = pd.read_csv(PROCESSED_DIR + "dataset_municipal.csv")

    cols_with_empty_values = [
        "gini",
        "tasa_ingresos",
    ]

    cols_with_only_zeros = [
        "cama_hospital",
        "cama_fuera_hospital",
        "cama_rec_nac",
        "consultorios",
        "equipamento",
        "medicos_otros",
        "medicos_gen_esp_odont",
        "otro_pers",
        "otro_pers_prof",
        "enfermeria_contac_paciente",
        "enfermeria_otras",
        "medicos_adiest",
        "per_tecnico",
        "total_elementos_salud",
    ]

    # on cols_with_only_zeros, replace 0 with empty value
    for col in cols_with_only_zeros:
        df[col] = df[col].replace(0, pd.NA)

    # Show empty value counts for verification
    print("Empty value counts after replacement:")
    for col in cols_with_only_zeros:
        empty_count = df[col].isna().sum()
        print(f"Column '{col}' has {empty_count} empty values.")

    # Save the modified DataFrame back to CSV
    df.to_csv(PROCESSED_DIR + "dataset_municipal_v2.csv", index=False)

if __name__ == "__main__":
    main()
