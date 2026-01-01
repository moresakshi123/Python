





SELECT passengerid, passengername,
ROW_NUMBER() OVER (ORDER BY passengername) AS row_num
FROM passengers;

-- Rank employees by salary (highest = rank 1)
SELECT employeeid, employeename, salary,
RANK() 
OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

SELECT employeeid, employeename, salary,
NTILE(4) OVER (ORDER BY salary DESC) AS salary_group
from employees;

-- Find passengers who have made at least one reservation
SELECT passengerid, passengername
FROM passengers
WHERE passengerid IN (
    SELECT passengerid FROM reservations
);


SELECT e.employeename,
       e.salary,
       (SELECT AVG(salary)
        FROM employees
        WHERE baseairport = e.baseairport) AS avg_salary_at_airport
FROM employees e;



SELECT e.employeename,
       e.baseairport,
       (SELECT AVG(fare)
        FROM reservations r
        WHERE r.sourceairport = e.baseairport) AS avg_fare_from_airport
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM reservations r
    WHERE r.sourceairport = e.baseairport
);



SELECT passengername,
       age,
       CASE
           WHEN age < 18 THEN 'Child'
           WHEN age BETWEEN 18 AND 59 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM passengers;