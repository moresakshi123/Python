




-- Example 1: Find passengers whose names start with 'S'
SELECT passengername 
FROM passengers 
WHERE passengername LIKE 'S%';






-- Example 2: Find passengers with Gmail addresses
SELECT passengername,email 
FROM passengers 
WHERE email LIKE '%gmail.com';



-- Example 1: Find passengers who have not given phone numbers
SELECT passengername, email 
FROM passengers 
WHERE phone IS NULL;

-- Example 2: Find reservations where seat numbers are assigned
SELECT reservationid, seatno 
FROM reservations 
WHERE seatno IS NOT NULL;

