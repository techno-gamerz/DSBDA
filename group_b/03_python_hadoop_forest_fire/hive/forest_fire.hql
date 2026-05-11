CREATE DATABASE IF NOT EXISTS forest_db;
USE forest_db;

DROP TABLE IF EXISTS forest_fires;
CREATE TABLE forest_fires (
  x INT,
  y INT,
  month STRING,
  day STRING,
  ffmc DOUBLE,
  dmc DOUBLE,
  dc DOUBLE,
  isi DOUBLE,
  temp DOUBLE,
  rh DOUBLE,
  wind DOUBLE,
  rain DOUBLE,
  area DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'data/forest_fires_sample.csv' INTO TABLE forest_fires;

SELECT month, AVG(area) AS avg_area
FROM forest_fires
GROUP BY month
ORDER BY avg_area DESC;

SELECT month, COUNT(*) AS fire_count
FROM forest_fires
GROUP BY month
ORDER BY fire_count DESC;
