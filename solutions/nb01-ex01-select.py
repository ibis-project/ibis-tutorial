# Convert the metric units to imperial, and drop the metric columns.
penguins_imperial_select = penguins.select(
    "species",
    "island",
    "sex",
    "year",
    bill_length_in=penguins.bill_length_mm / 25.4,
    bill_depth_in=penguins.bill_depth_mm / 25.4,
    flipper_length_in=penguins.flipper_length_mm / 25.4,
    body_weight_lb=penguins.body_mass_g / 453.6,
)

penguins_imperial_select
