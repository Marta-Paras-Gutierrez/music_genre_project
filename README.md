````
# Music Genre Classification - Exploratory Data Analysis

## Project Overview

This project performs an Exploratory Data Analysis (EDA) on the GTZAN Dataset - Music Genre Classification.

The main objective is to investigate whether different music genres present identifiable acoustic patterns using audio features extracted from songs.

The project includes:
- Data cleaning
- Feature engineering
- Exploratory visualizations
- Comparison between audio fragments of 3 and 30 seconds
- Modularized pipeline using Python

---

## Dataset

Dataset used:

https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

Datasets included:

- `features_30_sec.csv`
- `features_3_sec.csv`

These datasets contain acoustic characteristics extracted from songs belonging to different music genres.

---

## Research Questions

1. Are there acoustic patterns that help differentiate music genres?

2. Which acoustic variables have the greatest influence on musical identity?

3. Which music genres show higher energy or acoustic complexity?

4. Can tempo act as a differentiating factor between genres?

5. How does the audio fragment size (3 seconds vs 30 seconds) affect acoustic metrics?

6. Do MFCC coefficients provide useful information for future automatic music classification tasks?

---

## Technologies Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Structure

```text
music_genre_project/
│
├── data/
│   ├── raw/
│   │   ├── features_30_sec.csv
│   │   └── features_3_sec.csv
│   │
│   └── processed/
│       └── clean_dataset.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── outputs/
│   └── figures/
│
├── src/
│   ├── cleaning.py
│   ├── features.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
````

---

## Data Cleaning

The following cleaning operations were performed:

* Removal of duplicated rows
* Null value verification
* Removal of unnecessary columns
* Validation of dataset structure

---

## Feature Engineering

Three new features were created:

* `song_complexity`
* `mfcc_mean_total`
* `energy_tempo_ratio`

These variables summarize relevant acoustic properties related to:

* rhythm
* spectral behavior
* audio energy

---

## Visualizations

The notebook includes several visualizations:

* Genre distribution
* Correlation heatmap
* Tempo distribution by genre
* Spectral relationships
* Dataset comparison (3s vs 30s)

---

## Main Conclusions

* Different music genres present distinguishable acoustic patterns.
* Tempo and spectral variables are relevant for genre differentiation.
* Rock and metal genres show higher acoustic energy and variability.
* 3-second audio fragments generate more variable acoustic metrics.
* MFCC coefficients provide valuable information for future machine learning classification tasks.

---

## Future Work

As future work, a machine learning model could be developed for automatic music genre classification using the analyzed acoustic features.

````
