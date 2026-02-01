#!/bin/bash

# Chris Joakim, 3Cloud/Cognizant, 2026

# Activate the virtual environment, print the python version.
source .venv/bin/activate
python --version

# List the available kernels, then start jupyter.
echo 'listing available kernels ...'
jupyter kernelspec list

echo 'starting jupyter notebook ...'
jupyter notebook
