ATTACH 'dbname=postgres user=postgres' AS pycon2024 (TYPE POSTGRES);

INSERT INTO pycon2024.imdb_title_basics
  FROM 'https://storage.googleapis.com/ibis-tutorial-data/imdb/2024-03-22/imdb_title_basics.parquet';
INSERT INTO pycon2024.imdb_title_ratings
  FROM 'https://storage.googleapis.com/ibis-tutorial-data/imdb/2024-03-22/imdb_title_ratings.parquet';
