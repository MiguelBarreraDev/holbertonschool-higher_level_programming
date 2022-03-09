-- Commans to managment a database
-- Query: Lists all genres from hbtn_0d_tsvhows and displays the number od shows
-- linked to each
SELECT 
	tv_genres.name AS genre, 
	COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC
