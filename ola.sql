CREATE TABLE friends(
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    fav_color TEXT,
    monthly_salary REAL
);

-- Inserting data into Salesman
INSERT INTO friends VALUES
(5001, 'James Hoog', 'purple',100000),

(5002, 'Nail Knite', 'yellow', 50000),
(5005, 'Pit Alex', 'orange', 200000),
(5006, 'Mc Lyon', 'purple', 70000),
(5007, 'Paul Adam', 'yellow', 4000000),
(5003, 'Lauson Hen', 'pink', 40000);

SELECT * FROM friends;

SELECT COUNT(NAME) FROM friends;
SELECT AVG(MONTHLY_SALARY) FROM friends;
SELECT SUM(MONTHLY_SALARY) FROM friends;
select DISTINCT(FAV_COLOR) FROM friends;

SELECT * FROM friends ORDER BY  MONTHLY_SALARY DESC;
SELECT AVG (MONTHLY_SALARY),FAV_COLOR FROM friends GROUP BY FAV_COLOR;