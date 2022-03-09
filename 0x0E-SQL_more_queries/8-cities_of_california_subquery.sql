-- Commans to managment a database
-- Query: Lists all the cities of California that can be foundin the db hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California'
);
