sol2 = maintainers.sql(
    "SELECT name, jaccard(maintainers.name, 'gforsyth') as sim from maintainers"
).distinct().order_by(_.sim.desc())

sol2