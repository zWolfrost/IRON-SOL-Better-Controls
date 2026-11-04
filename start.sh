#!/bin/bash

cd "$(dirname "$0")"
konsole -e bash -c "source .venv/bin/activate; python3 controls.py"
