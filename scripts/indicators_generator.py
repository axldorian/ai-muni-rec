import pandas as pd
from ind import generate_indicators

def main():

    df = pd.read_csv('data/processed/dataset_municipal_v2.csv')
    indicators = generate_indicators(df)

    # save as csv
    indicators.to_csv('data/processed/indicators_municipal.csv', index=False)

if __name__ == "__main__":
    main()
