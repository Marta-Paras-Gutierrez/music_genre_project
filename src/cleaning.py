"""
Data loading and cleaning functions.
"""

import pandas as pd



def load_data(path: str) -> pd.DataFrame:
    """
    Load CSV dataset.
    """

    return pd.read_csv(path)



def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning process.
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove null values
    df = df.dropna()

    # Remove unnecessary column
    if "filename" in df.columns:
        df = df.drop(columns=["filename"])

    return df