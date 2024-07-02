import urllib.request
from pathlib import Path
import psycopg2
import duckdb


def setup_data_directory():
    print("Downloading data...")
    # Create the data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    paths = [
        ("penguins/0.10/palmer_penguins.ddb", "penguins"),
        ("pypi/2024-04-24/deps.parquet", "pypi"),
        ("pypi/2024-04-24/maintainers.parquet", "pypi"),
        ("pypi/2024-04-24/package_urls.parquet", "pypi"),
        ("pypi/2024-04-24/packages.parquet", "pypi"),
        ("pypi/2024-04-24/scorecard_checks.parquet", "pypi"),
        ("pypi/2024-04-24/wheels.parquet", "pypi"),
        ("imdb/2024-03-22/imdb_title_basics_sample_5.parquet", "imdb"),
        ("imdb/2024-03-22/imdb_title_basics.parquet", "imdb"),
        ("imdb/2024-03-22/imdb_title_ratings.parquet", "imdb"),
    ]

    for suffix, subdir in paths:
        folder = data_dir / subdir
        folder.mkdir(exist_ok=True)
        target = folder / suffix.rsplit("/", 1)[-1]

        if not target.exists():
            print(f"- {target}")
            urllib.request.urlretrieve(
                f"https://storage.googleapis.com/ibis-tutorial-data/{suffix}",
                target,
            )


def setup_postgres_database():
    create_tables = """
    DROP TABLE IF EXISTS imdb_title_basics;
    CREATE TABLE imdb_title_basics (
      tconst TEXT,
      "titleType" TEXT,
      "primaryTitle" TEXT,
      "originalTitle" TEXT,
      "isAdult" BIGINT,
      "startYear" BIGINT,
      "endYear" BIGINT,
      "runtimeMinutes" BIGINT,
      genres TEXT
    );
    
    DROP TABLE IF EXISTS imdb_title_ratings;
    CREATE TABLE imdb_title_ratings (
      tconst TEXT,
      "averageRating" DOUBLE PRECISION,
      "numVotes" BIGINT
    );
    """

    load_data = """
    ATTACH 'dbname=postgres user=postgres' AS pg (TYPE POSTGRES);

    INSERT INTO pg.imdb_title_basics FROM 'data/imdb/imdb_title_basics.parquet';
    INSERT INTO pg.imdb_title_ratings FROM 'data/imdb/imdb_title_ratings.parquet';
    """

    validate_data = """
    SELECT 'imdb_title_basics' table, COUNT(*) n FROM imdb_title_basics UNION
    SELECT 'imdb_title_ratings' table, COUNT(*) n FROM imdb_title_ratings
    ORDER BY "table";
    """

    print("Creating postgres tables...")
    with psycopg2.connect(dbname="postgres", user="postgres") as pg:
        with pg.cursor() as cur:
            cur.execute(create_tables)

    print("Loading data into postgres...")
    with duckdb.connect() as ddb:
        ddb.execute(load_data)
    

def setup():
    setup_data_directory()
    setup_postgres_database()
    print("Done!")


if __name__ == "__main__":
    setup()
