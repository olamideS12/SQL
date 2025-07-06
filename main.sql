CREATE TABLE Salesman (
    Salesman_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commission REAL
);

-- Inserting data into Salesman
INSERT INTO Salesman VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5007, 'Paul Adam', 'Rome', 0.13),
(5003, 'Lauson Hen', 'San Jose', 0.12);

SELECT * FROM Salesman;

SELECT  MIN (Commission) FROM Salesman;
SELECT MAX (Commission) FROM Salesman;

SELECT * FROM Salesman
WHERE CITY = 'Paris' AND Commission > 0.12;

SELECT * FROM Salesman
WHERE CITY ='LONDON ' OR Commission > 0.13;