-- Insert test data into the table
BEGIN;
INSERT INTO MY_SCHEMA.MY_TABLE (NAME, AGE) VALUES
('Alice', 30),
('Bob', 25),
('Charlie', 35);
COMMIT;
