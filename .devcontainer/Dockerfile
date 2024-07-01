FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

COPY codespace_requirements.txt /

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends graphviz postgresql-client

# original command
# RUN python3 -m pip install ipython altair plotnine plotly ipykernel jupyter 'ibis-framework[duckdb,postgres,polars,visualization,examples]'
RUN python3 -m pip install -r codespace_requirements.txt
