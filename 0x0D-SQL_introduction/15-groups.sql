-- Script containing queries to interact with the database
-- Query: Lists the number of records with the same score
SELECT score, COUNT(name) AS number from second_table
GROUP BY score;
