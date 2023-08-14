# Ibis Tutorial EuroSciPy 2023

- 01: Basic verbs
- 02: Memtables, joins, and selectors
- 03: Exploring PyPI data: `.sql`, integrations, UDFs

## Setup

### Install dependencies

We recommend using `conda` or `mamba`, but `pip` works, too! 

#### conda / mamba

```sh
mamba create -n ibis-tutorial python ibis-duckdb=6.1 python-duckdb=0.8.1 jupyterlab altair plotnine
```

#### pip

```sh
python -m pip install 'ibis-framework[duckdb]==6.1' duckdb==0.8.1 jupyterlab altair>=5.0.1 plotnine
```

or

```sh
python -m pip install -r requirements.txt
```

### Clone this repository

```sh
git clone https://github.com/gforsyth/ibis-tutorial.git
```

