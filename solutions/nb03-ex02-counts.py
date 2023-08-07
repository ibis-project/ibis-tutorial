ibis.options.repr.interactive.max_rows = 20

maintainer_counts = (
    maintainers.group_by("package_name")
    .agg(maintainers=_.count())
    .filter([_.maintainers == 12])
)

maintainer_counts