# Movie Recommendation System using Content-Based Filtering

## Project Overview

This project builds a **Content-Based Movie Recommendation System** using the TMDB 5000 Movies Dataset.

The recommendation engine suggests movies similar to a selected movie based on:
- Genres
- Keywords
- Cast
- Director
- Movie overview

The system uses:
- NLP (Natural Language Processing)
- TF-IDF Vectorization
- Cosine Similarity

to compute similarity between movies and generate personalized recommendations.

---

# Dataset Information

The project uses two datasets:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Both datasets are merged using the movie ID.

## Dataset Features

### Movies Dataset
Contains:
- Genres
- Keywords
- Overview
- Popularity
- Revenue
- Vote statistics
- Release information

### Credits Dataset
Contains:
- Cast
- Crew
- Director information

---

# Dataset Source

[Kaggle TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- AST

---

# Exploratory Data Analysis (EDA)

The notebook includes:
- Vote count distribution
- Popular movie ranking analysis
- Weighted movie ranking
- Statistical analysis of ratings

## Key Insights
- Highly rated movies are not always the most reliable recommendations
- Movies with higher vote counts provide more trustworthy ratings
- Weighted ranking improves recommendation quality

---

# Data Preprocessing

Several preprocessing steps were performed:

## Merging Datasets
Merged movies and credits datasets using movie ID.

## Handling Missing Values
Missing values were cleaned and irrelevant columns removed.

## Feature Extraction
Extracted:
- Genres
- Keywords
- Top 3 Cast Members
- Director

from nested JSON-like columns.

## Text Cleaning
- Removed spaces between names
- Combined important metadata into a single `tags` column

Example:
```python
overview + genres + keywords + cast + director
