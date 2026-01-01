





-- Count how many employees are working
SELECT COUNT(*) AS total_employees
FROM employees;


-- Find total revenue from reservations
SELECT SUM(fare) AS total_revenue
FROM reservations;

-- Find average age of passengers
SELECT AVG(age) AS average_age
FROM passengers;


-- Find the maximum salary among employees
SELECT MAX(salary) AS highest_salary
FROM employees;
-- Find the minimum fare paid for a reservation
SELECT MIN(fare) AS lowest_fare
FROM reservations;

-- Find average salary for each job role
SELECT jobrole,AVG(salary)
FROM employees
GROUP BY jobrole;


-- Find total revenue collected for each flight


-- Count number of reservations per flight


SELECT baseairport, COUNT(*) AS total_employees
FROM employees
GROUP BY baseairport
HAVING COUNT(*) > 5;

