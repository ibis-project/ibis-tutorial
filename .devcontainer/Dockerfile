FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

COPY requirements.txt /

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends graphviz postgresql-client

RUN python3 -m pip install -r requirements.txt
