transitive_dependents = (
    expr.group_by(_.dependency)
    .agg(n_dependents=_.package.nunique())
    .order_by(_.n_dependents.desc())
    .select(name=_.dependency, n_dependents=_.n_dependents)
)
transitive_dependents
