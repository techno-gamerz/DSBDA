CREATE DATABASE IF NOT EXISTS flight_db;
USE flight_db;

DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  year INT,
  month INT,
  dayofmonth INT,
  dayofweek INT,
  depdelay DOUBLE,
  origin STRING,
  dest STRING,
  flightnum STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

DROP TABLE IF EXISTS airports;
CREATE EXTERNAL TABLE airports (
  iata STRING,
  name STRING,
  city STRING,
  state STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/airports_ext';

LOAD DATA LOCAL INPATH 'data/flight_2008_sample.csv' INTO TABLE flights;
LOAD DATA LOCAL INPATH 'data/airports_sample.csv' INTO TABLE airports;

ALTER TABLE flights ADD COLUMNS (carrier STRING);

INSERT INTO TABLE flights VALUES
(2008,1,3,4,5.0,'SFO','LAX','UA123','UA');

SELECT f.flightnum, f.origin, a.city
FROM flights f
JOIN airports a ON f.origin = a.iata
LIMIT 10;

CREATE INDEX flights_origin_idx ON TABLE flights(origin)
AS 'COMPACT' WITH DEFERRED REBUILD;
ALTER INDEX flights_origin_idx ON flights REBUILD;

SELECT year, month, dayofmonth, AVG(depdelay) AS avg_depdelay
FROM flights
WHERE year = 2008
GROUP BY year, month, dayofmonth
ORDER BY year, month, dayofmonth;
