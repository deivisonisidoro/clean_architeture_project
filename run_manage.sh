#!/bin/bash

# Get the absolute path of the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set the Python path to the project root directory
export PYTHONPATH="$SCRIPT_DIR"

# Run the manage.py script
python "$SCRIPT_DIR/infrastructure/django_core/manage.py" "$@"
