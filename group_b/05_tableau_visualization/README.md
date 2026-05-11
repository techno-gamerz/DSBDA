# Group B5 - Tableau visualizations (Adult and Iris)

Aim
- Create 1D, 2D, 3D, temporal, multidimensional, tree/hierarchical, and network visualizations in Tableau.

Files
- prep_tableau_data.py
- requirements.txt
- data/iris_sample.csv
- data/adult_sample.csv

Steps
1. Install dependencies for data prep:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. (Optional) Place full datasets here:
   - data/iris.csv
   - data/adult.csv
3. Run the prep script:
   ```bash
   python prep_tableau_data.py
   ```
4. Open Tableau Desktop.
5. Connect to outputs/iris_tableau.csv and outputs/adult_tableau.csv.
6. For each visualization, follow the standard workflow:
   - Connect to data source
   - Choose dimensions and measures
   - Apply the visualization type

Suggested visualizations
1. 1D (Linear)
   - Adult: histogram of age
   - Iris: histogram of sepal_length
2. 2D (Planar)
   - Iris: scatter sepal_length vs sepal_width, color by species
3. 3D (Volumetric)
   - Iris: scatter with sepal_length (X), sepal_width (Y), petal_length (Size)
4. Temporal
   - Adult: line chart of average hours_per_week over record_date
5. Multidimensional
   - Adult: scatter of age vs hours_per_week, color by income, size by education_num
6. Tree/Hierarchical
   - Adult: treemap of education -> occupation by count
7. Network
   - Adult: use outputs/adult_network_edges.csv as edges (source=occupation, target=education)

Notes
- record_date is a synthetic date added in the prep script for temporal visualization.
- For network views, use a Tableau extension or path-based marks.
