ftw_packages = maintainer_counts.filter(_.package_name.startswith("ftw-"))

maint_counts = maintainer_counts.count().to_pandas()
ftw_counts = ftw_packages.count().to_pandas()
print(f"{maint_counts=}, {ftw_counts=}")