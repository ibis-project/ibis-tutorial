sol3 = (
    basics
    .join(ratings, "tconst")
    .select("titleType", "primaryTitle", "numVotes", "averageRating", "isAdult")
    .rename("snake_case")
)

sol3
