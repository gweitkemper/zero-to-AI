"""
Pydantic models for the M26 MCP Server.
Chris Joakim, 3Cloud/Cognizant, 2026
"""

from typing import Optional

from pydantic import BaseModel


class SpeedCalculationModel(BaseModel):
    successful: bool
    distance_value: Optional[float] = None
    distance_unit: Optional[str] = None
    elapsed_time_hhmmss: Optional[str] = None
    miles_per_hour: Optional[float] = None
    kilometers_per_hour: Optional[float] = None
    yards_per_hour: Optional[float] = None
    seconds_per_mile: Optional[float] = None
    pace_per_mile: Optional[str] = None


class RunWalkCalculationModel(BaseModel):
    run_hhmmss: str
    run_ppm: str
    walk_hhmmss: str
    walk_ppm: str
    miles: float
    avg_mph: Optional[float] = None
    avg_ppm: Optional[str] = None
    proj_time: Optional[str] = None
    proj_miles: Optional[float] = None


class HealthStatusModel(BaseModel):
    status: str
    timestamp: str
    server_name: str
    server_start_time: str
    version: str
    tools_available: list[str]
    resources_available: list[str]


class ServerCapabilitiesModel(BaseModel):
    tools: int
    resources: int
    prompts: int


class ServerEndpointsModel(BaseModel):
    tools: list[str]
    resources: list[str]


class ServerInfoModel(BaseModel):
    name: str
    description: str
    version: str
    created: str
    capabilities: ServerCapabilitiesModel
    endpoints: ServerEndpointsModel
