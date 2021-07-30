-- settings.sql
CREATE DATABASE tonespoon;
CREATE USER tonespoonuser WITH PASSWORD 'tonespoon';
GRANT ALL PRIVILEGES ON DATABASE tonespoon TO tonespoonuser;