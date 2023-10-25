# Ibis Tutorial PyData NYC 2023

- 01: Basic verbs
- 02: Memtables, joins, and selectors
- 03: Exploring PyPI data: `.sql`, integrations, UDFs

A previous iteration of this tutorial was given at EuroSciPy 2023 ([youtube recording](https://youtu.be/tkejUD5Uq40))  

## Setup

### Install dependencies

We recommend using `conda` or `mamba`, but `pip` works, too! 

#### conda / mamba

```sh
mamba create -n ibis-tutorial python ibis-duckdb=7 python-duckdb=0.8.1 jupyterlab altair plotnine
```

#### pip

```sh
python -m pip install 'ibis-framework[duckdb]==7' duckdb==0.8.1 jupyterlab altair>=5.0.1 plotnine
```

or

```sh
python -m pip install -r requirements.txt
```

### Clone this repository

```sh
git clone https://github.com/ibis-project/ibis-tutorial.git
```

