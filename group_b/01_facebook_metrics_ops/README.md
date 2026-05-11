# Group B1 - Facebook metrics operations (Python)

Aim
- Perform data subsets, merge, sort, transpose, and reshape operations on the Facebook metrics dataset.

Tools and environment
- Python 3.9+
- pandas, numpy

Files
- facebook_metrics_ops.py
- requirements.txt
- data/facebook_metrics_sample.csv
- data/facebook_metrics_secondary_sample.csv

Steps
1. Install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. (Optional) Place the real dataset at data/facebook_metrics.csv. If missing, sample data is used.
3. Run the script:
   ```bash
   python facebook_metrics_ops.py
   ```
4. Check outputs in outputs/.

Operations covered (manual aligned)
- Subsets using indexing, loc, and iloc
- Merge/concat of two dataframes
- Sort with sort_values
- Transpose with transpose or .T
- Reshape from wide to long and back (melt/pivot)

Outputs
- subset_cols.csv
- subset_rows.csv
- merged.csv
- sorted.csv
- transposed.csv
- reshaped.csv
- cast_wide.csv

Notes
- If you need the same operations on another dataset (for example, book reviews), reuse the same steps and update file paths.
