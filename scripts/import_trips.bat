@echo off
REM credentials should placed in the .pgpass (POSTGRES example)

REM export data to file
SET username=postgres
SET time=2023-09-08T22
SET select=SELECT device_id, provider_id, trip_id, extract(epoch from start_time) * 1000, extract(epoch from end_time) * 1000, CONCAT(start_lat::text, ',', start_lng::text), CONCAT(end_lat::text, ',', end_lng::text), duration, distance, municipality FROM trips WHERE to_char(end_time,'YYYY-MM-DDTHH24') = '%time%'
SET sql=COPY (%select%) TO '%cd%\trips.%time%.csv' WITH DELIMITER ';' CSV

SET PGPASSWORD=postgres
psql -U %username% -d nl_profiel -c "%sql%"

REM move file
MOVE trips.%time%.csv ../code/import/

curl http://localhost:8080/admin/import/trips