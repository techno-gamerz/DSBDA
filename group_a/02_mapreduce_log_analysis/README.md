# Assignment A2: MapReduce Log Analysis

## 1. Problem Statement
Write a MapReduce program using Java to process a system log file. The goal is to calculate the total logged-in time for each user and identify the user(s) with the maximum total logged-in time.

## 2. Learning Objectives
- To understand the MapReduce programming model (Map, Reduce, and Driver).
- To learn how to process structured data (CSV) using Hadoop MapReduce.
- To implement multi-stage MapReduce jobs (Job Chaining).

## 3. Input Data Format
The input is a CSV file with the following columns:
- `user`: Username
- `start`: Login timestamp (yyyy-MM-dd HH:mm:ss)
- `end`: Logout timestamp (yyyy-MM-dd HH:mm:ss)

## 4. Implementation Details
The solution is implemented in two stages in [LogDurationDriver.java](src/LogDurationDriver.java):

1. **Job 1 (Duration Summation):** 
   - **Mapper:** ([Line 25](src/LogDurationDriver.java#L25)) Calculates duration in seconds for each log entry.
   - **Reducer:** ([Line 65](src/LogDurationDriver.java#L65)) Sums up durations per user.
2. **Job 2 (Global Maximum):**
   - **Mapper:** ([Line 77](src/LogDurationDriver.java#L77)) Emits all user totals with a single constant key.
   - **Reducer:** ([Line 104](src/LogDurationDriver.java#L104)) Finds the maximum duration and emits the user(s) who achieved it.

## 5. Execution Steps

### Step 1: Start Hadoop Daemons
```bash
start-dfs.sh
start-yarn.sh
jps
```

### Step 2: Compile the Java Code
```bash
export HADOOP_CLASSPATH=$(hadoop classpath)
mkdir -p build
javac -classpath "$HADOOP_CLASSPATH" -d build src/LogDurationDriver.java
jar -cvf log-analysis.jar -C build/ .
```

### Step 3: Prepare HDFS Input
```bash
hdfs dfs -mkdir -p /input/log_analysis
hdfs dfs -rm -f /input/log_analysis/sample_log.csv
hdfs dfs -put data/sample_log.csv /input/log_analysis/
```

### Step 4: Run the MapReduce Job
```bash
hdfs dfs -rm -r -f /output/totals /output/max_user
hadoop jar log-analysis.jar LogDurationDriver /input/log_analysis /output/totals /output/max_user
```

### Step 5: View Results
```bash
# Total time per user
hdfs dfs -cat /output/totals/part-r-00000
# User(s) with max time
hdfs dfs -cat /output/max_user/part-r-00000
```

Expected result on the included sample data:
```text
chris    15000
```
The exact spacing is Hadoop tab-separated output.

## 6. Viva Questions & Answers
Refer to the final report for advanced Viva questions related to this assignment.
