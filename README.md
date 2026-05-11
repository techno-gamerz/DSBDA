# DSBDA Practical Assignments

Each assignment has its own folder with:
- README.md with easy steps
- code or scripts
- a data/ folder with small sample CSVs (replace with real datasets)

Notes:
- This repo follows the assignment list in `List of Laboratory Assignments.txt` and is cross-checked with `DSBDAL.pdf` and `DSBDA MMCOE.pdf`.
- Hadoop, Hive, and Tableau assignments need a suitable lab machine with those tools installed. The scripts and commands are provided, but those services are not bundled in this repo.
- Python scripts run on included sample data by default if the full real datasets are missing.
- For a clean first run of any Python assignment, create a virtual environment inside that assignment folder and install its `requirements.txt`.

General Python setup pattern:
```bash
cd group_b/01_facebook_metrics_ops
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python facebook_metrics_ops.py
```

First-run readiness summary:

| Assignment | Suitable system | First-run status |
| --- | --- | --- |
| [A1 Hadoop installation](group_a/01_hadoop_installation) | Ubuntu VM/native Linux with Java, SSH, Hadoop 3.x | README contains install and verification steps |
| [A2 Java MapReduce log analysis](group_a/02_mapreduce_log_analysis) | Hadoop pseudo-distributed mode, Java 8/11 | Compile/run commands included |
| [A3 HiveQL flight system](group_a/03_hiveql_flight_info) | Hadoop + Hive 2.x recommended for `CREATE INDEX` | Hive script and sample CSVs included |
| [B1 Facebook metrics](group_b/01_facebook_metrics_ops) | Python 3.9+ | Runs with `requirements.txt` |
| [B2 Air quality + heart disease](group_b/02_air_heart_pipeline) | Python 3.9+ | Runs with `requirements.txt` |
| [B3 Forest fire PyHadoop/Hive](group_b/03_python_hadoop_forest_fire) | Python 3 + Hadoop Streaming + Hive | Local and Hadoop commands included |
| [B4 Matplotlib/Seaborn visualization](group_b/04_visualization_matplotlib_seaborn) | Python 3.9+ | Runs after installing `requirements.txt` |
| [B5 Tableau visualization](group_b/05_tableau_visualization) | Python 3.9+ + Tableau Desktop/Public | Data prep script and Tableau chart list included |
| [C1 Review scraper](group_c/01_review_scraper) | Python 3.9+ | Runs on included sample HTML; live URLs depend on site permission/selectors |
| [C2 ML mini project](group_c/02_ml_mini_project) | Python 3.9+ | Runs with `requirements.txt` |

Folder map
- [group_a/01_hadoop_installation](group_a/01_hadoop_installation)
- [group_a/02_mapreduce_log_analysis](group_a/02_mapreduce_log_analysis)
- [group_a/03_hiveql_flight_info](group_a/03_hiveql_flight_info)
- [group_b/01_facebook_metrics_ops](group_b/01_facebook_metrics_ops)
- [group_b/02_air_heart_pipeline](group_b/02_air_heart_pipeline)
- [group_b/03_python_hadoop_forest_fire](group_b/03_python_hadoop_forest_fire)
- [group_b/04_visualization_matplotlib_seaborn](group_b/04_visualization_matplotlib_seaborn)
- [group_b/05_tableau_visualization](group_b/05_tableau_visualization)
- [group_c/01_review_scraper](group_c/01_review_scraper)
- [group_c/02_ml_mini_project](group_c/02_ml_mini_project)
