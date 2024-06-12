FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

COPY requirements.txt /tmp/pip-tmp/
RUN python3 -m pip install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
