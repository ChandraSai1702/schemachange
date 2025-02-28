-- Add a new column to an existing table
BEGIN;
ALTER TABLE MY_SCHEMA.MY_TABLE ADD COLUMN AGE INT;
COMMIT;
