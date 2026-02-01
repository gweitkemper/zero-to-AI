#!/bin/bash

# Start the MCP server in HTTP mode.
#Chris Joakim, 3Cloud/Cognizant, 2026

source .venv/bin/activate

python --version

python m26-mcp-server.py --http
