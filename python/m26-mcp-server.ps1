# PowerShell script to start the M26 MCP Server in HTTP mode.
# Chris Joakim, 3Cloud/Cognizant, 2026

.\.venv\Scripts\activate

python --version

python server.py --http
