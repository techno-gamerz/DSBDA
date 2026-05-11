# Assignment B5: Data Visualization using Tableau

## 1. Problem Statement
Prepare the Adult and Iris datasets and create various types of visualizations in Tableau, including 1D, 2D, 3D, temporal, multidimensional, tree/hierarchical, and network visualizations.

## 2. Objectives
- Clean and prepare data for BI tools using Python.
- Learn to create diverse chart types in Tableau.
- Understand how to map dimensions and measures to visual encodings.

## 3. Software Requirements
- Tableau Desktop or Tableau Public
- Python 3.x (for data preparation)
- Pandas (for data preparation)

## 4. Visualizations to be Created
- **1D (Linear):** Histogram of Age (Adult dataset).
- **2D (Planar):** Scatter plot of Sepal Length vs Sepal Width (Iris dataset).
- **3D (Volumetric):** Bubble chart using X, Y, and Size/Color.
- **Temporal:** Line chart of hours worked over time.
- **Multidimensional:** Scatter plots with multiple encodings (Color, Size, Shape).
- **Tree/Hierarchical:** Treemap of Education and Occupation hierarchies.
- **Network:** Visualizing relationships between Education levels and Occupations.

## 5. Implementation Details
### Data Preparation (`prep_tableau_data.py`)
- Loads Iris and Adult datasets.
- Feature Engineering: Calculates areas, bins age/hours into groups.
- Temporal Data: Adds a synthetic `record_date` for time-series analysis.
- Network Data: Generates an edge list for network visualization.
- Exports cleaned CSV files to the `outputs/` directory.

## 6. Execution Steps
1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Prepare Data:**
   ```bash
   python prep_tableau_data.py
   ```
3. **Launch Tableau:**
   Import the generated CSV files from the `outputs/` folder.
4. **Build Dashboards:**
   Create worksheets for each required visualization type and assemble them into a dashboard.

Generated files:
- `outputs/adult_tableau.csv`
- `outputs/iris_tableau.csv`
- `outputs/adult_network_edges.csv`

## 7. Conclusion
Successfully prepared datasets and utilized Tableau to create advanced visualizations, enhancing the ability to derive business intelligence from raw data.
