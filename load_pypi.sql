ATTACH 'dbname=postgres user=postgres' AS pycon2024 (TYPE POSTGRES);

CREATE OR REPLACE TABLE pycon2024.deps AS
  FROM 'pypi/2024-04-24/deps.parquet';
CREATE OR REPLACE TABLE pycon2024.maintainers AS
  FROM 'pypi/2024-04-24/maintainers.parquet';
CREATE OR REPLACE TABLE pycon2024.package_urls AS
  FROM 'pypi/2024-04-24/package_urls.parquet';
CREATE OR REPLACE TABLE pycon2024.packages AS
  FROM 'pypi/2024-04-24/packages.parquet';
CREATE OR REPLACE TABLE pycon2024.scorecard_checks AS
  FROM 'pypi/2024-04-24/scorecard_checks.parquet';
CREATE OR REPLACE TABLE pycon2024.wheels AS
  FROM 'pypi/2024-04-24/wheels.parquet';
