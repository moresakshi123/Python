-- Example 1: Show top 5 highest-paid employees
SELECT employeename, salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 5;

-- Example 1: Find employees working at Delhi airport
SELECT employeename, jobrole 
FROM employees 
WHERE baseairport = 'DEL';


-- Find reservations where fare is more than 5000
SELECT reservationid, passengerid, fare
FROM reservations
WHERE fare > 5000;


-- Example 1: Find reservations made between Jan 1 and Jun 30, 2024
SELECT reservationid, bookingdate 
FROM reservations 
WHERE bookingdate BETWEEN '2024-01-01' AND '2024-06-30';







-- Example 2: Get employees whose salary is between 30,000 and 60,000
SELECT employeename, salary 
FROM employees 
WHERE salary BETWEEN 30000 AND 60000;








-- Example 1: Find airports in Mumbai, Delhi, and Bangalore
SELECT airportname, city 
FROM airports 
WHERE city IN ('Mumbai', 'Delhi', 'Bangalore');





-- Example 2: Get employees with job role as Pilot
SELECT employeename, jobrole 
FROM employees 
WHERE jobrole IN ('Pilot');




