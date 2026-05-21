"""
Feature engineering functions.
"""

import pandas as pd



def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new acoustic features.
    """

    df = df.copy()

    # Feature 1: song complexity
    df["song_complexity"] = (
        df["spectral_bandwidth_mean"]
        + df["zero_crossing_rate_mean"]
        + df["tempo"]
    ) / 3

    # Feature 2: MFCC global mean
    mfcc_cols = [
        col for col in df.columns
        if "mfcc" in col and "mean" in col
    ]

    df["mfcc_mean_total"] = df[mfcc_cols].mean(axis=1)

    # Feature 3: energy / tempo ratio
    df["energy_tempo_ratio"] = (
        df["rms_mean"] / df["tempo"]
    )

    return df