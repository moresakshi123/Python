#Order by:
-- Example 1: Sort passengers by age (highest first)
SELECT passengername,age
FROM passengers
ORDER BY age DESC;

-- Example 2: Sort products by date added (oldest first)
SELECT flightno,passengerid,DestinationAirport
FROM reservations 
ORDER BY passengerid;



SELECT airportname,city from airports;

-- Example 2: Get first 5 reservations
SELECT reservationid, passengerid, flightno 
FROM reservations 
LIMIT 5;