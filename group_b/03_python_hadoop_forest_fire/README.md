# Group B3 - Python and Hadoop on forest fire dataset

Aim
- Integrate Python with Hadoop to analyze the forest fire dataset using streaming MapReduce and Hive.

Files
- mapper.py
- reducer.py
- hive/forest_fire.hql
- data/forest_fires_sample.csv

MapReduce steps (local test)
1. Run locally with pipes:
   ```bash
   type data\forest_fires_sample.csv | python mapper.py | sort | python reducer.py
   ```

MapReduce steps (Hadoop streaming)
1. Put data into HDFS:
   ```bash
   hdfs dfs -mkdir -p /input/forest
   hdfs dfs -put data/forest_fires_sample.csv /input/forest/
   ```
2. Run streaming:
   ```bash
   hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
     -files mapper.py,reducer.py \
     -mapper "python mapper.py" \
     -reducer "python reducer.py" \
     -input /input/forest/forest_fires_sample.csv \
     -output /output/forest_fire_month_avg
   ```
3. View output:
   ```bash
   hdfs dfs -cat /output/forest_fire_month_avg/part-00000
   ```

Hive steps
1. Start Hive and run:
   ```bash
   hive -f hive/forest_fire.hql
   ```

Outputs
- MapReduce output shows average burned area per month
- Hive queries show average area and top months
