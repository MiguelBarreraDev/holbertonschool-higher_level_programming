-- Commans to managment a database
-- Query: Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.name FROM tv_genres g
INNER JOIN tv_show_genres
ON g.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY g.name;
