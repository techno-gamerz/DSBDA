# Group B4 - Visualization with matplotlib and seaborn

Aim
- Visualize the datasets from assignments 2 and 3 using matplotlib and seaborn.

Files
- visualize_air_heart_forest.py
- requirements.txt
- data/air_quality_sample.csv
- data/heart_disease_sample.csv
- data/forest_fires_sample.csv

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
   - data/forest_fires.csv
3. Run:
   ```bash
   python visualize_air_heart_forest.py
   ```
4. Check outputs in outputs/.

Visualization types (manual aligned)
- Line plot for time series
- Bar or histogram for distributions
- Box plot for outliers
- Scatter plot for correlations
- Heat map for correlation matrices

Outputs
- air_co_timeseries.png
- heart_corr_heatmap.png
- forest_area_by_month.png
