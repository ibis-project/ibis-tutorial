sol4 = (
    basics
    .join(ratings, "tconst")
    .select("titleType", "primaryTitle", "numVotes", "averageRating", "isAdult")
    .rename("snake_case")
    .filter(
        [
            _.title_type == "movie",
            _.is_adult == 0,
            _.num_votes >= 100_000,
        ]
    )
    .order_by(_.average_rating.desc())
    .select(
        _.primary_title,
        _.average_rating,
    )
)

sol4
