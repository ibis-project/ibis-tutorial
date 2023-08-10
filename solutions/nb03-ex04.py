top_maintainers_by_downloads = (
    maintainers.join(packages, [("package_name", "name")])
    .group_by("name")
    .aggregate(downloads=_.downloads.sum())
    .select("name", "downloads")
    .order_by(ibis.desc("downloads"))
    .limit(10)
)

top_maintainers_by_downloads
