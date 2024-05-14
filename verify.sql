SELECT 'imdb_title_basics' table, COUNT(*) n FROM imdb_title_basics UNION
SELECT 'imdb_title_ratings' table, COUNT(*) n FROM imdb_title_ratings
ORDER BY "table";
