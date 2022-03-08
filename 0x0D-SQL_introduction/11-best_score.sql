-- Script containing queries to interact with the database
/** 
 * Lists all records with a score >= 10 in the table second_table
 * Display both the score and the name (int this order)
 * Records should be ordered bt score (top first)
 */
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
