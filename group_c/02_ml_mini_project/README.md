# Assignment Group C2: Graduate Admissions Prediction

## 1. Problem Statement
Develop a machine learning pipeline to predict the "Chance of Admit" for graduate students based on parameters such as GRE scores, TOEFL scores, university rating, SOP, LOR, CGPA, and research experience. Compare the performance of different regression algorithms.

## 2. Objectives
- To understand the machine learning workflow: data loading, preprocessing, model training, and evaluation.
- To implement and compare multiple regression models (Linear Regression, Random Forest, Gradient Boosting).
- To evaluate models using metrics like Root Mean Squared Error (RMSE) and R-squared (R2) score.
- To learn how to persist trained models using `joblib`.

## 3. Prerequisites
- Python 3.9 or higher
- Libraries: `pandas`, `scikit-learn`, `joblib`
- Dataset: Graduate Admissions dataset (available on Kaggle).

## 4. Implementation Details
The project is structured as follows:
- [admissions_models.py](admissions_models.py): Main script for training and evaluation.
- [data/admissions_sample.csv](data/admissions_sample.csv): A small subset of the dataset for testing.
- [outputs/](outputs/): Contains the saved model and performance report.

### Key Components:
- **Preprocessing**: Column names are normalized (lowercase, underscores). Features are scaled using `StandardScaler` (within a pipeline for linear models).
- **Models Evaluated**:
  1. **Linear Regression**: Baseline linear model.
  2. **Random Forest Regressor**: Ensemble of decision trees.
  3. **Gradient Boosting Regressor**: Boosting-based ensemble method.
- **Metrics**: 
  - **RMSE**: Measures the average magnitude of the error.
  - **R2 Score**: Represents the proportion of variance for a dependent variable that's explained by an independent variable.

## 5. Execution Instructions
1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Training**:
   ```bash
   python admissions_models.py
   ```
4. **Check Results**:
   - Metrics are available in `outputs/metrics.json`.
   - The best model is saved as `outputs/best_model.pkl`.

The script uses `data/admissions_sample.csv` by default. For the full Kaggle dataset, place the CSV in `data/` with a `Chance of Admit` column.

## 6. Result Analysis
The script identifies the best performing model based on the lowest RMSE. In typical runs, ensemble methods like Random Forest or Gradient Boosting tend to outperform simple Linear Regression due to their ability to capture non-linear relationships.
