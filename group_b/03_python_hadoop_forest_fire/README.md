# Assignment B3: Python and Hadoop MapReduce for Forest Fire Data Analysis

## 1. Problem Statement
Analyze the Forest Fire dataset to calculate the average burned area per month using Python and Hadoop Streaming (MapReduce). Additionally, perform data exploration using HiveQL.

## 2. Objectives
- Implement Mapper and Reducer scripts in Python.
- Execute the MapReduce job using Hadoop Streaming.
- Load data into Apache Hive and execute analytical queries.

## 3. Software Requirements
- Ubuntu/Linux OS
- Hadoop 3.x
- Apache Hive
- Python 3.x
- Forest Fire Dataset (CSV)

## 4. Dataset Description
The dataset contains 517 instances with 13 attributes:
- X, Y: Spatial coordinates
- month, day: Temporal attributes
- FFMC, DMC, DC, ISI: Fire Weather Index (FWI) components
- temp, RH, wind, rain: Meteorological attributes
- area: The burned area of the forest (target variable)

## 5. Implementation Details
### Mapper (`mapper.py`)
- Reads CSV data from standard input.
- Skips the header row.
- Extracts the `month` (index 2) and `area` (index 12).
- Emits `month` and `area` as a tab-separated key-value pair.

### Reducer (`reducer.py`)
- Reads the sorted key-value pairs from the mapper.
- Aggregates the `area` values for each `month`.
- Calculates and prints the average burned area per month.

## 6. Execution Steps
### A. Local Testing (without Hadoop)
```bash
cat data/forest_fires_sample.csv | python3 mapper.py | sort | python3 reducer.py
```
Expected sample output:
```text
aug     2.8000
mar     0.0000
may     0.0000
oct     0.0000
sep     0.7333
```

### B. Hadoop Streaming
1. **Upload data to HDFS:**
   ```bash
   hdfs dfs -mkdir -p /input/forest
   hdfs dfs -rm -f /input/forest/forest_fires_sample.csv
   hdfs dfs -put data/forest_fires_sample.csv /input/forest/
   ```
2. **Run Streaming Job:**
   ```bash
   hdfs dfs -rm -r -f /output/forest_fire_avg
   hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
     -files mapper.py,reducer.py \
     -mapper "python3 mapper.py" \
     -reducer "python3 reducer.py" \
     -input /input/forest/forest_fires_sample.csv \
     -output /output/forest_fire_avg
   ```

### C. Hive Execution
1. **Run the Hive script:**
   ```bash
   hive -f hive/forest_fire.hql
   ```
The Hive script uses the included sample CSV. Replace `data/forest_fires_sample.csv` with the full forest fire dataset path if your examiner provides the complete dataset.

## 7. Conclusion
Integrated Python with Hadoop Streaming to process large-scale datasets and used Hive for structured data analysis.
