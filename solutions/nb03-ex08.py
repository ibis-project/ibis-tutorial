bus_factor_1 = (
    maintainers.group_by("package_name")
    .agg(maintainer_count=_.count())
    .filter(_.maintainer_count == 1)
    .join(maintainers, "package_name")
    .join(
        (
            deps.select("package_name", "dep_name")
            .distinct()
            .group_by("dep_name")
            .agg(dep_count=_.count())
        ),
        [("package_name", "dep_name")],
    )
    .select("package_name", "name", "dep_count")
    .order_by(ibis.desc("dep_count"))
    .limit(10)
)

bus_factor_1
