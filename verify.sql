SELECT 'deps' table, COUNT(*) n FROM deps UNION
SELECT 'maintainers' table, COUNT(*) n FROM maintainers UNION
SELECT 'package_urls' table, COUNT(*) n FROM package_urls UNION
SELECT 'packages' table, COUNT(*) n FROM packages UNION
SELECT 'scorecard_checks' table, COUNT(*) n FROM scorecard_checks UNION
SELECT 'wheels' table, COUNT(*) n FROM wheels
ORDER BY "table";
