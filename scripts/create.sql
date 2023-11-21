CREATE DATABASE nl_profiel
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Dutch_Netherlands.1252'
    LC_CTYPE = 'Dutch_Netherlands.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- TIP to reuse scripts: create a view with this definition on top of your tables.
create table trips (
	device_id UUID, 
	provider_id UUID, 
	trip_id UUID, 
	start_time timestamp,
	end_time timestamp, 
	start_lat numeric,
	start_lng numeric, 
	end_lat numeric, 
	end_lng numeric, 
	duration integer, 
	distance integer,
	municipality text
);