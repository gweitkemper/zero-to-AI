"""
FastMCP Server for running, swimming, and cycling calculations with the 'm26'
package; see https://pypi.org/project/m26/.
Chris Joakim, 3Cloud/Cognizant, 2026

Also includes basic tools and health resource endpoint.
"""

import logging
import os
import sys

from datetime import datetime
from typing import Optional

from fastmcp import FastMCP

from starlette.requests import Request
from starlette.responses import JSONResponse

import m26

from src.app.mcp_constants import MCPConstants
from src.app.mcp_models import (
    HealthStatusModel,
    RunWalkCalculationModel,
    ServerCapabilitiesModel,
    ServerEndpointsModel,
    ServerInfoModel,
    SpeedCalculationModel,
)
from src.util.pyproject_parser import PyprojectParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SERVER_NAME = "m26-mcp-server"
SERVER_DESCRIPTION = (
    "MCP Server for running, swimming, and cycling calculations with the 'm26' package"
)
SERVER_VERSION = "0.1.0"
SERVER_START_TIME = datetime.now().isoformat()

logging.warning(f"SERVER_NAME:        {SERVER_NAME}")
logging.warning(f"SERVER_DESCRIPTION: {SERVER_DESCRIPTION}")
logging.warning(f"SERVER_VERSION:     {SERVER_VERSION}")
logging.warning(f"SERVER_START_TIME:  {SERVER_START_TIME}")

print("Creating FastMCP instance")
mcp = FastMCP(SERVER_NAME)


def convert_distance(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Convert a distance from one unit to another.
    For example: convert_distance(10.0, "m", "k") -> 16.0934
    Returns None if the conversion fails.
    """
    logging.warning(
        f"convert_distance: value={value} {str(type(value))}, from_unit={from_unit}, to_unit={to_unit}"
    )
    try:
        d = m26.Distance(value, from_unit)
        if from_unit == to_unit:
            return value
        elif to_unit == MCPConstants.UOM_KILOMETERS:
            return d.as_kilometers()
        elif to_unit == MCPConstants.UOM_YARDS:
            return d.as_yards()
        elif to_unit == MCPConstants.UOM_MILES:
            return d.as_miles()
        else:
            return value
    except Exception as e:
        logger.exception(
            f"Error in convert_distance: value={value}, from_unit={from_unit}, to_unit={to_unit}, error={e}"
        )
        return None


@mcp.tool()
def miles_to_kilometers(miles: float) -> Optional[float]:
    """
    Convert miles to kilometers.
    For example: miles_to_kilometers(10.0) -> 16.0934
    Returns None if the conversion fails.
    """
    return convert_distance(miles, MCPConstants.UOM_MILES, MCPConstants.UOM_KILOMETERS)


@mcp.tool()
def miles_to_yards(miles: float) -> Optional[float]:
    """
    Convert miles to yards.
    For example: miles_to_yards(10.0) -> 17600.0
    Returns None if the conversion fails.
    """
    return convert_distance(miles, MCPConstants.UOM_MILES, MCPConstants.UOM_YARDS)


@mcp.tool()
def kilometers_to_miles(kilometers: float) -> Optional[float]:
    """
    Convert kilometers to miles.
    For example: kilometers_to_miles(10.0) -> 6.21371
    Returns None if the conversion fails.
    """
    return convert_distance(kilometers, MCPConstants.UOM_KILOMETERS, MCPConstants.UOM_MILES)


@mcp.tool()
def kilometers_to_yards(kilometers: float) -> Optional[float]:
    """
    Convert kilometers to yards.
    For example: kilometers_to_yards(10.0) -> 10936.133
    Returns None if the conversion fails.
    """
    return convert_distance(kilometers, MCPConstants.UOM_KILOMETERS, MCPConstants.UOM_YARDS)


@mcp.tool()
def hhmmss_to_seconds(hhmmss: str) -> Optional[float]:
    """
    Convert a 'hh:mm:ss' formatted string to seconds.
    For example: hhmmss_to_seconds("01:01:01") -> 3661.0
    Returns None if the conversion fails.
    """
    try:
        et = m26.ElapsedTime(hhmmss)
        return float(et.secs)
    except Exception as e:
        logger.exception(f"Error in hhmmss_to_seconds: {e}")
        return None


@mcp.tool()
def hhmmss_to_hours(hhmmss: str) -> Optional[float]:
    """
    Convert a 'hh:mm:ss' formatted string to hours.
    For example: hhmmss_to_hours("01:01:01") -> 1.01694
    Returns None if the conversion fails.
    """
    try:
        et = m26.ElapsedTime(hhmmss)
        return float(et.hours())
    except Exception as e:
        logger.exception(f"Error in hhmmss_to_hours: {e}")
        return None


@mcp.tool()
def calculate_speed(
    distance_value: float, distance_unit: str, elapsed_time_hhmmss: str
) -> Optional[SpeedCalculationModel]:
    """
    Calculate the speed in miles per hour, kilometers per hour, yards per hour, seconds per mile, and pace per mile.
    The distance_value must be a positive number.
    The distance_unit must be one of the following: "m" (miles), "k" (kilometers), or "y" (yards).
    The elapsed_time_hhmmss must be a valid 'hh:mm:ss' formatted string.
    Returns None if the calculation fails.
    """
    try:
        d1 = m26.Distance(distance_value, distance_unit)
        et = m26.ElapsedTime(elapsed_time_hhmmss)
        sp = m26.Speed(d1, et)
        return SpeedCalculationModel(
            successful=True,
            distance_value=d1.value,
            distance_unit=d1.uom,
            elapsed_time_hhmmss=et.as_hhmmss(),
            miles_per_hour=sp.mph(),
            kilometers_per_hour=sp.kph(),
            yards_per_hour=sp.yph(),
            seconds_per_mile=sp.seconds_per_mile(),
            pace_per_mile=sp.pace_per_mile(),
        )
    except Exception as e:
        logger.exception(f"Error in calculate_speed: {e}")
        return None


@mcp.tool()
def calculate_age(yyyy_mm_dd_1: str, yyyy_mm_dd_2: str) -> Optional[float]:
    """
    Calculate the age between two dates in years.
    For example: calculate_age("1960-10-01", "2025-10-01") -> 65.0
    The two dates must be in the format "yyyy-mm-dd".
    Returns None if the calculation fails.
    """
    try:
        age = m26.AgeCalculator.calculate(yyyy_mm_dd_1.strip(), yyyy_mm_dd_2.strip())
        return float(age.value)
    except Exception as e:
        logger.exception(f"Error in calculate_age: {e}")
        return None


@mcp.tool()
def calculate_run_walk(
    run_hhmmss: str, run_ppm: str, walk_hhmmss: str, walk_ppm: str, miles: float
) -> Optional[RunWalkCalculationModel]:
    """
    Calculate average pace and projected time for a run/walk strategy.
    The run_hhmmss is the duration of the run interval in 'mm:ss' format (e.g., "2:30").
    The run_ppm is the running pace per mile in 'mm:ss' format (e.g., "9:16").
    The walk_hhmmss is the duration of the walk interval in 'mm:ss' format (e.g., "0:45").
    The walk_ppm is the walking pace per mile in 'mm:ss' format (e.g., "17:00").
    The miles is the total distance in miles (e.g., 31.0).
    Returns None if the calculation fails.
    """
    try:
        result = m26.RunWalkCalculator.calculate(run_hhmmss, run_ppm, walk_hhmmss, walk_ppm, miles)
        return RunWalkCalculationModel(
            run_hhmmss=result["run_hhmmss"],
            run_ppm=result["run_ppm"],
            walk_hhmmss=result["walk_hhmmss"],
            walk_ppm=result["walk_ppm"],
            miles=result["miles"],
            avg_mph=result.get("avg_mph"),
            avg_ppm=result.get("avg_ppm"),
            proj_time=result.get("proj_time"),
            proj_miles=result.get("proj_miles"),
        )
    except Exception as e:
        logger.exception(f"Error in calculate_run_walk: {e}")
        return None


@mcp.resource("server://info")
def server_info() -> ServerInfoModel:
    """
    Get detailed server information.
    """
    return ServerInfoModel(
        name=SERVER_NAME,
        description=SERVER_DESCRIPTION,
        version=SERVER_VERSION,
        created=SERVER_START_TIME,
        capabilities=ServerCapabilitiesModel(
            tools=len(MCPConstants.M26_MCP_TOOLS_LIST),
            resources=len(MCPConstants.M26_MCP_RESOURCES_LIST),
            prompts=len(MCPConstants.M26_MCP_PROMPTS_LIST),
        ),
        endpoints=ServerEndpointsModel(
            tools=MCPConstants.M26_MCP_TOOLS_LIST, resources=MCPConstants.M26_MCP_RESOURCES_LIST
        ),
    )


@mcp.resource("health://status")
def health_status() -> HealthStatusModel:
    """
    Get the current health status of the server.
    """
    return HealthStatusModel(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        server_name=SERVER_NAME,
        version=SERVER_VERSION,
        server_start_time=SERVER_START_TIME,
        tools_available=MCPConstants.M26_MCP_TOOLS_LIST,
        resources_available=MCPConstants.M26_MCP_RESOURCES_LIST,
    )


if __name__ == "__main__":
    print(f"Starting server, sys.argv: {sys.argv}")
    mode = "stdio"
    if "--http" in sys.argv:
        mode = "http"

    if mode == "stdio":
        print("Running in stdio mode")
        mcp.run()
    elif mode == "http":
        print("Running in http mode")
        mcp.run(transport="http", port=8157, host="0.0.0.0")
    else:
        raise ValueError(f"Invalid mode: {mode}")
