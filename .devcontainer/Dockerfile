FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

COPY requirements.txt /

RUN apt-get update -y && apt-get install -y --no-install-recommends graphviz

RUN python3 -m pip install -r requirements.txt
