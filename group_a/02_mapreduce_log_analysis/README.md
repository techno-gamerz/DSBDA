# Group A2 - MapReduce log analysis (Java)

Aim
- Process a system log file and list users with the maximum total logged-in time.

Tools and environment
- Hadoop (pseudo-distributed)
- Java (JDK 8+)
- Ubuntu or WSL

Files
- src/LogDurationDriver.java
- data/sample_log.csv

Input format
- CSV header: user,start,end
- Timestamp format: yyyy-MM-dd HH:mm:ss
- Example: alice,2024-01-01 09:00:00,2024-01-01 12:30:00

Steps
1. Start Hadoop and verify services:
   ```bash
   start-dfs.sh
   start-yarn.sh
   jps
   ```
2. Prepare the log CSV (convert any raw log to CSV first).
3. Compile and build the jar:
   ```bash
   export HADOOP_CLASSPATH=$(hadoop classpath)
   mkdir -p build
   javac -classpath "$HADOOP_CLASSPATH" -d build src/LogDurationDriver.java
   jar -cvf log-duration.jar -C build/ .
   ```
4. Put the input file into HDFS:
   ```bash
   hdfs dfs -mkdir -p /input/logs
   hdfs dfs -put data/sample_log.csv /input/logs/
   ```
5. Run the job (two stages):
   ```bash
   hadoop jar log-duration.jar LogDurationDriver /input/logs /output/log_totals /output/log_max
   ```
   If rerunning, delete old outputs first:
   ```bash
   hdfs dfs -rm -r /output/log_totals /output/log_max
   ```
6. View results:
   ```bash
   hdfs dfs -cat /output/log_totals/part-r-00000
   hdfs dfs -cat /output/log_max/part-r-00000
   ```

Expected output
- /output/log_totals contains total seconds per user
- /output/log_max contains the user(s) with the maximum total time

Notes
- If javac cannot find Hadoop classes, ensure HADOOP_CLASSPATH is set for your Hadoop version.
- Keep the CSV format consistent with the mapper parser in LogDurationDriver.java.
