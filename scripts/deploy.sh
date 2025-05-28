#!/bin/bash
uv venv
uv sync
cdk deploy "$@"
