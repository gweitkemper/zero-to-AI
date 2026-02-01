#!/bin/bash

# Bash script to deploy the M26 MCP Server to the Cursor IDE.
# Chris Joakim, 3Cloud/Cognizant, 2026

source .venv/bin/activate
python --version

current_dir=$(pwd)
server_filename="${current_dir}/m26-mcp-server.py"
echo "Current directory: ${current_dir}"
echo "Server filename:   ${server_filename}"

fastmcp install cursor m26-mcp-server.py --project $server_filename
