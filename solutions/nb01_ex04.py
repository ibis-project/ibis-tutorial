(
    penguins
    .group_by("island")
    .agg(island_mean_mass=penguins.body_mass_g.mean())
    .join(penguins, "island")
)
