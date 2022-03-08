-- Script containing queries to interact with the database
/**
 * Query: Lists all records of the table second_table
 * Display the score and the name (in this order)
 * Listed by descending score
 */
SELECT score, name FROM second_table
WHERE name IS NOT NULL 
ORDER BY score DESC;

