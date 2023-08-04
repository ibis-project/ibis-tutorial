sol3 = (
    basics
    .join(ratings, "tconst")
    .select("titleType", "primaryTitle", "numVotes", "averageRating", "isAdult")
    .relabel("snake_case")
)

sol3
