




-- Example 1: Get passenger names with their reservation details
SELECT p.passengername, r.flightno, r.traveldate, r.fare
FROM passengers p
INNER JOIN reservations r ON p.passengerid = r.passengerid;



-- Example 1: Get all passengers and their reservations (even if no reservation exists)
SELECT p.passengername, r.flightno, r.traveldate
FROM passengers p
LEFT JOIN reservations r ON p.passengerid = r.passengerid;

-- Example 2: Get all employees and their base airport (show all airports even if no employee exists)
SELECT e.employeename, e.jobrole, a.airportname
FROM employees e
RIGHT JOIN airports a ON a.airportcode = e.baseairport;


-- Example 1: All passengers and reservations
SELECT p.passengername, r.flightno
FROM passengers p
LEFT JOIN reservations r ON p.passengerid = r.passengerid
UNION
SELECT p.passengername, r.flightno
FROM passengers p
RIGHT JOIN reservations r ON p.passengerid = r.passengerid;



