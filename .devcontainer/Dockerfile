FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

RUN apt-get update -y && \
  apt-get install -y --no-install-recommends graphviz && \
  python3 -m pip install ipython altair plotnine plotly ipykernel notebook \
    'ibis-framework[duckdb,postgres,polars,visualization,examples]'
