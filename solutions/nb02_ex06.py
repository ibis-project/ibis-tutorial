sol6 = (
    penguins
    .group_by("species")
    .mutate(
        s.across(
            s.numeric() & ~s.c("year"),
            (_ - _.mean()) / _.std()
        )
    )
)

sol6
