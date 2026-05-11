# Group C2 - Mini project (Graduate admissions prediction)

Aim
- Train and compare predictive models on the graduate admissions dataset.

Tools and environment
- Python 3.9+
- pandas, scikit-learn

Files
- admissions_models.py
- requirements.txt
- data/admissions_sample.csv

Steps
1. Install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. (Optional) Download the full dataset and place it at data/admissions.csv:
   - https://www.kaggle.com/tanmoyie/us-graduate-schools-admission-parameters
3. Run:
   ```bash
   python admissions_models.py
   ```
4. Check outputs in outputs/.

Outputs
- best_model.pkl
- metrics.json
- predictions_sample.csv

Notes
- The script evaluates multiple models and keeps the best based on metrics.
