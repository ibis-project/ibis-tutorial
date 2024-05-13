ATTACH 'dbname=postgres user=postgres' AS pycon2024 (TYPE POSTGRES);

INSERT INTO pycon2024.imdb_title_basics FROM 'imdb_title_basics.parquet';
INSERT INTO pycon2024.imdb_title_ratings FROM 'imdb_title_ratings.parquet';
