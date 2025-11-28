import pandas as pd
import unicodedata


def normalize_name(names: pd.Series) -> pd.Series:
    """
    Normalize names by stripping whitespace and converting to title case.

    Params
    ------
    names : pd.Series
        Series containing names to be normalized.

    Returns
    -------
    pd.Series
        Series containing normalized names.
    """

    # to lowercase
    names = names.str.lower().str.strip()

    # accents removal
    names = names.apply(
        lambda x: "".join(
            c for c in unicodedata.normalize("NFD", x) if not unicodedata.combining(c)
        )
    )

    # blank spaces to underscores
    names = names.str.replace(" ", "", regex=False)

    return names


def main():
    # Load the dataset
    df = pd.read_csv("data/processed/indicators_municipal.csv")

    # Normalize the 'municipio' column
    norm_munc = normalize_name(df["municipio"])

    # Add normalized names as a new column in the 2nd position
    df.insert(1, "municipio_norm", norm_munc)

    # Save the normalized dataset
    df.to_csv("data/processed/indicators_municipal_v2.csv", index=False)

    # Save "municipio" column separately as txt file
    df["municipio_norm"].to_csv(
        "data/processed/municipios.txt", index=False, header=False
    )


if __name__ == "__main__":
    main()
