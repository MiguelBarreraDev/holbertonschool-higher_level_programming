-- Script containing queries to interact with the database
/**
 * Displays the top 3 of cites temperatures during July and August
 + Ordered by temperature (descending)
 */
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
