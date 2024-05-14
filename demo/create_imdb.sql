DROP TABLE IF EXISTS imdb_title_basics;
CREATE TABLE imdb_title_basics (
  tconst TEXT,
  "titleType" TEXT,
  "primaryTitle" TEXT,
  "originalTitle" TEXT,
  "isAdult" BIGINT,
  "startYear" BIGINT,
  "endYear" BIGINT,
  "runtimeMinutes" BIGINT,
  genres TEXT
);

DROP TABLE IF EXISTS imdb_title_ratings;
CREATE TABLE imdb_title_ratings (
  tconst TEXT,
  "averageRating" DOUBLE PRECISION,
  "numVotes" BIGINT
);
