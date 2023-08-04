sol3 = (
    basics
    .join(ratings, "tconst")
    .select(
        title_type="titleType",
        primary_title="primaryTitle",
        num_votes="numVotes",
        average_rating="averageRating",
        is_adult="isAdult",
    )
)

sol3
