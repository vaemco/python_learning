# Phase 2 Project: Churn Analysis

This project consolidates data manipulation, cleaning, and visualization skills into a workflow for analyzing customer churn.

## Contents

- **`churn_analysis.py`**: The main script that:
    1.  Loads raw data (`churn_raw.csv`).
    2.  Removes rows with missing Customer IDs.
    3.  Imputes missing Age values with the mean.
    4.  Calculates a new feature (`Yearly_Cost`).
    5.  Visualizes correlations with a heatmap.
    6.  Exports the cleaned dataset to `churn_cleaned.csv`.

## Key Concepts

- **Data Pipeline**: The sequence of Load -> Clean -> Transform -> Visualize -> Export.
- **Handling Missing Data**: Strategies for cleaning data.
- **Feature Engineering**: Creating new meaningful data points from existing ones.
