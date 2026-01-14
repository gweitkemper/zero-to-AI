#!/bin/bash

# Execute code analysis and checking with the pylint library
# Chris Joakim, 3Cloud/Cognizant, 2026

# See https://pypi.org/project/pylint/
# See https://github.com/pylint-dev/pylint

source .venv/bin/activate

pylint --errors-only *.py src
