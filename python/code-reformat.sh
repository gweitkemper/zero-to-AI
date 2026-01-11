#!/bin/bash

# This script reformats the python codebase per the formatting rules
# defined in the 'ruff' program.
#
# Chris Joakim, 3Cloud/Cognizant, 2026

black *.py
black src 
black tests
