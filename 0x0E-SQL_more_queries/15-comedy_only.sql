-- Commands to managment a database
-- Query: Lists all Comedy shows in the database hbtn_0d_tvshows
/*
 * The tv_genres table contains only one record where name = Comedy
 * Each record should display tv_shows.title
 * Sorted in ascending order by the show title
 */
SELECT s.title FROM tv_shows s
JOIN tv_show_genres sg
ON s.id = sg.show_id
JOIN tv_genres g
ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title 
