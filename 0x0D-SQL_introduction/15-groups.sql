-- Script containing queries to interact with the database
-- Query: Lists the number of records with the same score
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
