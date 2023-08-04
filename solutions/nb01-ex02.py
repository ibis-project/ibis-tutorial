# What was the largest female penguin (by body mass) on each island in the year 2008
sol2 = (
    penguins
    .filter(
        [
            penguins.sex == "female",
            penguins.year == 2008,
        ]
    )
    .group_by("island")
    .body_mass_g.max()
)

sol2
