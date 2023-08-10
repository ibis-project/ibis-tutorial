top_pytest_extensions = (
    deps.filter(_.dep_name.startswith("pytest-"))
    .group_by("dep_name")
    .agg(dep_count=_.package_name.nunique())
    .order_by(_.dep_count.desc())
    .limit(10)
)

top_pytest_extensions
