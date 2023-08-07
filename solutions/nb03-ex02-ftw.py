ftw_packages = maintainer_counts.filter(_.package_name.startswith("ftw-"))

print(f"{maintainer_counts.count()=}, {ftw_packages.count()=}")