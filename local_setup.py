import urllib.request
from pathlib import Path

import duckdb
from packaging.version import parse as vparse

## Download penguins DuckDB file

duck_version = vparse(duckdb.__version__)

ddb_file = Path("palmer_penguins.ddb")

if not ddb_file.exists():
    print(f"Downloading {ddb_file}")
    urllib.request.urlretrieve(
        f"https://storage.googleapis.com/ibis-tutorial-data/penguins/0.{duck_version.minor}/palmer_penguins.ddb",
        ddb_file,
    )

## Download PyPI maintainer data from Ibis Tutorial bucket

filenames = [
    "deps.parquet",
    "maintainers.parquet",
    "package_urls.parquet",
    "packages.parquet",
    "scorecard_checks.parquet",
    "wheels.parquet",
]

folder = Path("pypi")
folder.mkdir(exist_ok=True)

for filename in filenames:
    path = folder / filename
    if not path.exists():
        print(f"Downloading {filename} to {path}")
        urllib.request.urlretrieve(
            f"https://storage.googleapis.com/ibis-tutorial-data/pypi/2024-04-24/{filename}",
            path,
        )

from pathlib import Path

filenames = [
    "imdb_title_basics_sample_5.parquet",
    "imdb_title_ratings.parquet",
]

folder = Path("imdb_smol")
folder.mkdir(exist_ok=True)
for filename in filenames:
    path = folder / filename
    if not path.exists():
        print(f"Downloading {filename} to {path}")
        urllib.request.urlretrieve(
            f"https://storage.googleapis.com/ibis-tutorial-data/imdb/2024-03-22/{filename}",
            path,
        )
