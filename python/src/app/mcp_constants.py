"""
Constant values used by the M26 MCP Server.
Chris Joakim, 3Cloud/Cognizant, 2026
"""


class MCPConstants:
    """
    Application constants such as for the M26 MCP Server.
    """

    M26_MCP_TOOLS_LIST = [
        "miles_to_kilometers",
        "miles_to_yards",
        "kilometers_to_miles",
        "kilometers_to_yards",
        "hhmmss_to_seconds",
        "hhmmss_to_hours",
        "calculate_speed",
        "calculate_age",
        "calculate_run_walk",
    ]

    M26_MCP_RESOURCES_LIST = ["health://status", "server://info"]

    M26_MCP_PROMPTS_LIST = []

    UOM_MILES = "m"
    UOM_KILOMETERS = "k"
    UOM_YARDS = "y"
