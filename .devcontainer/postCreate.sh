#!/usr/bin/env bash

set -euo pipefail

sudo apt update -y
sudo apt install -y graphviz

# install tutorial deps
python3 -m pip install ipython altair plotnine plotly ipykernel \
  'ibis-framework[duckdb,postgres,polars,visualization,examples]'