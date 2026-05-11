# Group A3 - HiveQL Flight Information System

## Aim
To design and implement a flight information system using HiveQL to perform data management, joins, indexing, and statistical analysis on flight datasets.

## Objectives
1. To create and manage internal and external tables in Hive.
2. To load data from local files into Hive tables.
3. To perform table modifications (adding columns and inserting rows).
4. To implement table joins and indexing for efficient querying.
5. To perform data aggregation (averages) grouped by time periods.

## Prerequisites
- Hadoop (HDFS & YARN) installed and running.
- Apache Hive installed and configured. Hive 2.x is recommended because the assignment requires `CREATE INDEX`, a manual-era Hive feature that is not supported in newer Hive 3.x installations.
- Java Development Kit (JDK) 8 or 11.
- Flight and Airport datasets in CSV format.

## Implementation Details
The system consists of two primary tables:
- **flights**: An internal table storing flight details like date, delay, origin, and destination.
- **airports**: An external table mapped to a specific HDFS location containing airport metadata.

### Workflow:
1. **Database Setup**: Create `flight_db` and switch to it.
2. **Schema Definition**: Define `flights` and `airports` with appropriate data types and delimiters.
3. **Data Ingestion**: Load sample CSV data into the tables.
4. **Schema Evolution**: Add a `carrier` column to the `flights` table.
5. **Analytical Queries**:
   - Join flights with airports to get city names.
   - Calculate average departure delay per day for the year 2008.
6. **Performance Optimization**: Create and rebuild a compact index on the `origin` column.

## How to Run
1. Start Hadoop Services:
   ```bash
   start-dfs.sh
   start-yarn.sh
   jps
   ```
2. Initialize Metastore once only, if it has not already been initialized:
   ```bash
   schematool -initSchema -dbType derby
   ```
3. Execute the Hive script:
   ```bash
   hive -f flight_info.hql
   ```

If you rerun the script, it drops and recreates the two assignment tables automatically. If your Hive version does not support indexes, comment the two index lines in `flight_info.hql` and explain during viva that Hive indexes were removed in newer Hive releases.

## Expected Output
The script will display:
- Successful table creation and data loading messages.
- A join result showing flight numbers, origins, and corresponding cities.
- A table listing Year, Month, Day, and the Average Departure Delay for 2008.

## Conclusion
This assignment demonstrates the use of HiveQL for big data warehousing, showing how SQL-like syntax can be used to process large-scale datasets stored in HDFS efficiently.
