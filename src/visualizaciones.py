"""
Visualization functions for EDA.
"""

import os

import matplotlib.pyplot as plt
import seaborn as sns


# Crear carpeta automáticamente si no existe
OUTPUT_DIR = "outputs/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------------------------
# 1. Distribución de géneros
# ---------------------------------------------------

def plot_genre_distribution(df):

    plt.figure(figsize=(12, 6))

    sns.countplot(
        data=df,
        x="label",
        order=df["label"].value_counts().index,
        palette="viridis"
    )

    plt.title(
        "Distribución de géneros musicales",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Género musical",
        fontsize=12
    )

    plt.ylabel(
        "Cantidad de canciones",
        fontsize=12
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/genre_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------------------------------------------
# 2. Heatmap de correlaciones
# ---------------------------------------------------

def plot_correlation_heatmap(df):

    plt.figure(figsize=(18, 14))

    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(
        corr,
        cmap="coolwarm",
        linewidths=0.3
    )

    plt.title(
        "Mapa de correlaciones entre variables acústicas",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/correlation_heatmap.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------------------------------------------
# 3. Tempo por género
# ---------------------------------------------------

def plot_tempo_boxplot(df):

    plt.figure(figsize=(14, 6))

    sns.boxplot(
        data=df,
        x="label",
        y="tempo",
        palette="Set2"
    )

    plt.title(
        "Distribución del tempo por género musical",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Género musical",
        fontsize=12
    )

    plt.ylabel(
        "Tempo",
        fontsize=12
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/tempo_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------------------------------------------
# 4. Scatterplot espectral
# ---------------------------------------------------

def plot_spectral_relationship(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="spectral_centroid_mean",
        y="zero_crossing_rate_mean",
        hue="label",
        palette="tab10"
    )

    plt.title(
        "Relación entre spectral centroid y zero crossing rate",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Spectral Centroid Mean",
        fontsize=12
    )

    plt.ylabel(
        "Zero Crossing Rate Mean",
        fontsize=12
    )

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/spectral_relationship.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------------------------------------------
# 5. Histograma de tempo
# ---------------------------------------------------

def plot_tempo_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="tempo",
        kde=True,
        color="purple"
    )

    plt.title(
        "Distribución general del tempo",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Tempo",
        fontsize=12
    )

    plt.ylabel(
        "Frecuencia",
        fontsize=12
    )

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/tempo_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ---------------------------------------------------
# 6. Comparación datasets
# ---------------------------------------------------

def plot_dataset_comparison(comparison_df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=comparison_df,
        x="dataset",
        y="tempo",
        palette="Set2"
    )

    plt.title(
        "Comparación del tempo entre datasets",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Tipo de fragmento de audio",
        fontsize=12
    )

    plt.ylabel(
        "Tempo",
        fontsize=12
    )

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"{OUTPUT_DIR}/dataset_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
