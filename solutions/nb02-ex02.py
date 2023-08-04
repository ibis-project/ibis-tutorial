# Join basics with ratings on tconst, selecting out only a few columns.
sol2 = (
    basics
    .join(ratings, "tconst")
    .select("titleType", "primaryTitle", "numVotes", "averageRating", "isAdult")
)

sol2
