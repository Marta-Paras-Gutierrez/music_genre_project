"""
Main script for the project.

Executes the complete data pipeline:
1. Data loading
2. Data cleaning
3. Feature engineering
4. Visualization generation
5. Data export
"""

from src.cleaning import load_data, clean_data

from src.features import create_features

from src.visualizaciones import (
    plot_genre_distribution,
    plot_correlation_heatmap,
    plot_tempo_boxplot,
    plot_spectral_relationship,
    plot_tempo_distribution,
    plot_dataset_comparison
)

import pandas as pd


def main():

    # --------------------------------------------------
    # 1. LOAD DATASETS
    # --------------------------------------------------

    path_30 = "data/raw/features_30_sec.csv"

    path_3 = "data/raw/features_3_sec.csv"

    df_30 = load_data(path_30)

    df_3 = load_data(path_3)

    print("Datasets loaded successfully")


    # --------------------------------------------------
    # 2. CLEAN DATA
    # --------------------------------------------------

    df_30 = clean_data(df_30)

    df_3 = clean_data(df_3)

    print("Datasets cleaned")


    # --------------------------------------------------
    # 3. FEATURE ENGINEERING
    # --------------------------------------------------

    df_30 = create_features(df_30)

    print("Features created")


    # --------------------------------------------------
    # 4. DATASET COMPARISON
    # --------------------------------------------------

    df_30["dataset"] = "30 segundos"

    df_3["dataset"] = "3 segundos"

    comparison_df = pd.concat([df_30, df_3])

    print("Comparison dataset created")


    # --------------------------------------------------
    # 5. VISUALIZATIONS
    # --------------------------------------------------

    print("Generating visualizations...")


    plot_genre_distribution(df_30)

    plot_correlation_heatmap(df_30)

    plot_tempo_boxplot(df_30)

    plot_spectral_relationship(df_30)

    plot_tempo_distribution(df_30)

    plot_dataset_comparison(comparison_df)

    print("Visualizations saved in outputs/figures/")


    # --------------------------------------------------
    # 6. EXPORT CLEAN DATASET
    # --------------------------------------------------

    output_path = "data/processed/clean_dataset.csv"

    df_30.to_csv(output_path, index=False)

    print(f"Dataset exported to: {output_path}")


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    main()