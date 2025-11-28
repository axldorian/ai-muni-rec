import pandas as pd

RAW_DIR = "data/raw/"


def main():
    # load dataset
    df = pd.read_csv(RAW_DIR + "dataset-081025.csv")
    
    # identifica si hay columnas con datos faltantes
    missing_data_columns = df.columns[df.isnull().any()].to_list()
    if missing_data_columns:
        print("Columnas con datos faltantes en el DataFrame original:")
        for col in missing_data_columns:
            missing_count = df[col].isnull().sum()
            print(f"- {col}: {missing_count} valores faltantes")
    else:
        print("No hay columnas con datos faltantes en el DataFrame original.")
    

if __name__ == "__main__":
    main()
