-- Commands to managment a database
-- Query: Use the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter

SELECT s.title FROM tv_shows s
WHERE s.title NOT IN (
	SELECT s.title FROM tv_shows s
	LEFT JOIN tv_show_genres sg
	ON s.id = sg.show_id
	LEFT JOIN tv_genres g
	ON g.id = sg.genre_id
	WHERE g.name = 'Comedy'
)
ORDER BY s.title;
