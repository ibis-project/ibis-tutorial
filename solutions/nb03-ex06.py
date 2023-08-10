my_dependents = (
    deps.join(maintainers, _.dep_name == maintainers.package_name)
    .filter(_.name == "gforsyth")
    .select(package="dep_name", dependent="package_name")
    .distinct()
)

my_dependents
