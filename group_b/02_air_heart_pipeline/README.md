# Group B2 - Air quality and heart disease pipeline (Python)

Aim
- Perform data cleaning, integration, transformation, error correction, and model building.

Tools and environment
- Python 3.9+
- pandas, numpy, scikit-learn

Files
- air_heart_pipeline.py
- requirements.txt
- data/air_quality_sample.csv
- data/heart_disease_sample.csv

Steps
1. Install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. (Optional) Place real datasets:
   - data/air_quality.csv
   - data/heart_disease.csv
3. Run:
   ```bash
   python air_heart_pipeline.py
   ```
4. Check outputs in outputs/.

Operations covered (manual aligned)
- Data cleaning: null handling (dropna/fillna), duplicates, type fixes (to_datetime)
- Error correction: range checks and replacements
- Data integration: merge datasets and store an integrated preview
- Data transformation: encoding and scaling
- Model building: train/test split, train a model, evaluate metrics

Outputs
- air_quality_clean.csv
- heart_disease_clean.csv
- heart_scaled.csv
- integration_preview.csv
- health_env.db (SQLite integration)
- heart_model.pkl
- metrics.json
