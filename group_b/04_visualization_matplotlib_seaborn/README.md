# Assignment B4: Data Visualization using Matplotlib and Seaborn

## 1. Problem Statement
Use Matplotlib and Seaborn libraries in Python to visualize various datasets (Air Quality, Heart Disease, and Forest Fires) to identify patterns, correlations, and distributions.

## 2. Objectives
- Perform exploratory data analysis through visualization.
- Create time-series plots, heatmaps, and categorical bar charts.
- Master Matplotlib and Seaborn styling and layouts.

## 3. Software Requirements
- Python 3.x
- Pandas, Matplotlib, Seaborn
- Jupyter Notebook (Optional) or any Python IDE

## 4. Visualizations Performed
1. **Air Quality (Time Series):** CO levels over time using a Line Plot.
2. **Heart Disease (Correlation):** Identifying relationships between attributes using a Correlation Heatmap.
3. **Forest Fires (Distribution):** Average burned area per month using a Bar Plot.

## 5. Implementation Details
The script `visualize_air_heart_forest.py` follows these steps:
- **Data Loading:** Uses Pandas to load datasets from the `data/` directory.
- **Preprocessing:** Handles date-time conversions and numeric formatting.
- **Plotting:** 
  - `plt.plot()` for Line Charts.
  - `sns.heatmap()` for Correlation Matrices.
  - `sns.barplot()` for monthly aggregations.
- **Storage:** Saves all plots as PNG files in the `outputs/` directory.

## 6. Execution Steps
1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the visualization script:**
   ```bash
   python visualize_air_heart_forest.py
   ```
4. **View the results:**
   Check the `outputs/` folder for generated image files.

The script uses sample Air Quality, Heart Disease, and Forest Fire CSV files unless full datasets named `air_quality.csv`, `heart_disease.csv`, and `forest_fires.csv` are placed in `data/`.

## 7. Conclusion
Visualized complex datasets using Python, demonstrating the ability to communicate data insights through graphical representations.
