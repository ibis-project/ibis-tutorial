ibis_dependents = (
    deps.filter(_.dep_name == "ibis-framework").select("package_name").distinct()
)

ibis_dependents
