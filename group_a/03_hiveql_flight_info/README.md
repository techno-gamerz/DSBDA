# Group A3 - HiveQL flight information system

Aim
- Use HiveQL to create and manage flight tables, load data, join tables, create an index, and compute average departure delay per day in 2008.

Tools and environment
- Hadoop + Hive on Ubuntu/WSL

Files
- flight_info.hql
- data/flight_2008_sample.csv
- data/airports_sample.csv

Steps
1. Start Hadoop:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```
2. Create Hive warehouse directories in HDFS:
   ```bash
   hdfs dfs -mkdir -p /user/hive/warehouse
   hdfs dfs -mkdir -p /tmp/hive
   hdfs dfs -chmod 777 /user/hive/warehouse
   hdfs dfs -chmod 777 /tmp
   hdfs dfs -chmod 777 /tmp/hive
   ```
3. Initialize the Hive metastore (first run only):
   ```bash
   schematool -initSchema -dbType derby
   ```
   If Hive fails to start and metastore_db exists, back it up and re-init.
4. Run the Hive script:
   ```bash
   hive -f flight_info.hql
   ```

What the script does
- Creates and drops database tables
- Creates an external Hive table
- Loads data and inserts new rows
- Joins flights with airports
- Creates an index on the flight table
- Finds average departure delay per day in 2008

Notes
- Update file paths inside flight_info.hql if your data lives elsewhere.
- For large data, put CSVs in HDFS and update the external table LOCATION.
- If your dataset is TSV, update FIELDS TERMINATED BY in flight_info.hql.
