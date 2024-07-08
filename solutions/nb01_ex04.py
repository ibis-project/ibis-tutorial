mean_mass_per_island = (
    penguins
    .group_by("island")
    .agg(island_mean_mass=penguins.body_mass_g.mean())
)

penguins.join(mean_mass_per_island, "island")
