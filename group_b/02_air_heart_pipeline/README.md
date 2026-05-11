# Group B: Assignment B2 - Air Quality and Heart Disease Pipeline

## Problem Statement
Implement a data processing pipeline that performs data cleaning, integration, transformation, error correction, and model building using two different datasets: Air Quality and Heart Disease.

## Objectives
1. Perform data cleaning (handling nulls, duplicates, type conversions).
2. Implement error correction for out-of-range values.
3. Integrate datasets and store them in a relational database (SQLite).
4. Apply data transformations such as scaling and encoding.
5. Build and evaluate a predictive model (Logistic Regression).

## Theory
### Data Pipeline Stages
- **Data Cleaning:** Removing noise and correcting inconsistencies.
- **Data Integration:** Combining data from multiple sources.
- **Data Transformation:** Converting data into suitable formats for modeling (e.g., Z-score normalization).
- **Error Correction:** Identifying and fixing data entry errors using domain-specific ranges.
- **Model Building:** Using machine learning algorithms to extract patterns or predict outcomes.

## Prerequisites
- Python 3.9+
- libraries: `pandas`, `numpy`, `scikit-learn`, `joblib`, `sqlite3`

## Procedure
1. Load Air Quality and Heart Disease datasets (use samples if primary files are missing).
2. Clean Air Quality data: ([line 33](air_heart_pipeline.py#L33)) handle missing values (-200), convert datetime, and remove duplicates.
3. Clean Heart Disease data: ([line 57](air_heart_pipeline.py#L57)) handle "?" values, convert types, and clip out-of-range values.
4. Integrate both datasets into an SQLite database (`health_env.db`).
5. Perform Z-score normalization (StandardScaler) on heart disease features.
6. Concatenate samples of both datasets for a unified integration preview.
7. Split the heart disease data into training and testing sets.
8. Train a Logistic Regression model ([line 92](air_heart_pipeline.py#L92)) and evaluate its performance.
9. Save the model and metrics to the `outputs/` directory.

## Setup and Execution
1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Script:**
   ```bash
   python air_heart_pipeline.py
   ```

The script falls back to the included sample CSV files. For full practical execution, place the real datasets in `data/` as `air_quality.csv` and `heart_disease.csv`.

## Files
- [air_heart_pipeline.py](air_heart_pipeline.py): Pipeline implementation.
- `requirements.txt`: Dependencies.
- [data/](data/): Sample CSV files.
- [outputs/](outputs/): Cleaned data, model, and metrics.

## Conclusion
The assignment demonstrates a complete data engineering and basic machine learning pipeline, covering everything from raw data cleaning to model evaluation.
