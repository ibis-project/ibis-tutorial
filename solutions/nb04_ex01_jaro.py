@ibis.udf.scalar.builtin
def jaro_similarity(left: str, right: str) -> float:
    ...


packages.select("name", sim=jaro_similarity(packages.name, "pandas")).order_by(
    _.sim.desc()
)
