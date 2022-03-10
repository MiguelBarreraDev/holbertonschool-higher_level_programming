-- Commands to managment a database
-- Query: Lists all shows from hbtn_0d_tvshows_rate by their raiting
SELECT s.title, SUM(sr.rate) AS raiting FROM tv_shows s
JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY s.title
ORDER BY raiting DESC;
