sol3 = (
    penguins
    .filter(penguins.sex == "male")
    .group_by(["island", "year"])
    .body_mass_g.max()
)

sol3
