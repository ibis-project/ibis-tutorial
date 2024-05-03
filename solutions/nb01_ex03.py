sol3 = (
    penguins
    .filter(penguins.sex == "male")
    .group_by(["island", "year"])
    .agg(penguins.body_mass_g.max())
)

sol3
