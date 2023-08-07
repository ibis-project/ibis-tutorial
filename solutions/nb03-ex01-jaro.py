sol1 = packages.sql(
    "SELECT name, version, jaro_similarity(packages.name, 'pandas') as sim from packages",
).order_by(_.sim.desc())

sol1