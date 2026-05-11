# Group B: Assignment B1 - Facebook Metrics Operations

## Problem Statement
Perform fundamental data manipulation operations on the Facebook metrics dataset using the Python Pandas library. The operations include subsetting, merging, sorting, transposing, and reshaping (melt/pivot).

## Objectives
1. Implement data subsetting using indexing and selection methods.
2. Perform data integration by merging multiple datasets.
3. Apply sorting techniques to organize data.
4. Demonstrate data restructuring using transposition and reshaping methods.

## Theory
### Data Manipulation with Pandas
Pandas is a core library for data science in Python.
- **Subsetting:** `loc` (label-based) and `iloc` (integer-based) allow precise extraction of data.
- **Merging:** `pd.merge()` provides SQL-like joining capabilities to combine datasets.
- **Sorting:** `sort_values()` reorders the data based on specified columns.
- **Transposing:** `.T` attribute flips the axes of the DataFrame.
- **Melt & Pivot:** `melt()` converts wide data to long format, while `pivot_table()` aggregates and reshapes data into a wide format.

## Prerequisites
- Python 3.9 or higher
- Pandas library

## Procedure
1. Load the primary Facebook metrics dataset.
2. Load a secondary dataset for merging demonstration.
3. Create subsets based on columns and specific row conditions.
4. Merge the two datasets on a common key (e.g., Post Month).
5. Sort the data by specific metrics.
6. Transpose a selection of the data.
7. Reshape the data using `melt` for a long-form view.
8. Use `pivot_table` to reshape the long-form data back to a summarized wide format.
9. Save all results to the `outputs/` directory.

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
   python facebook_metrics_ops.py
   ```

The script uses `data/facebook_metrics_sample.csv` and `data/facebook_metrics_secondary_sample.csv` by default. Replace them with the full Facebook metrics dataset using the same column structure if required.

## Files
- [facebook_metrics_ops.py](facebook_metrics_ops.py): Main implementation script.
- `requirements.txt`: Dependencies.
- [data/](data/): Sample datasets.
- [outputs/](outputs/): Processed CSV results.

## Conclusion
This assignment demonstrates essential data manipulation skills required for data preprocessing and exploration using the Pandas library.
