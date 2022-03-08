-- Script containing queries to interact with the database
/**
 * Displays the average temperatures by city
 + Ordered by temperature (descending)
 */
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
