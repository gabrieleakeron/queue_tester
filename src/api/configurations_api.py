from fastapi import APIRouter

from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.scenario import ScenarioDto
from services.connection_service import save_connection, find_connections
from services.data_service import save_data, find_data
from services.sample_service import save_sample, find_samples
from services.scenario_service import save_scenario, find_scenarios

router = APIRouter(prefix="/configuration")

@router.post("/connection")
async def add_connection(connection: QueueConnectionConfigTypes):
    path = save_connection(connection)
    return {"message": "Connection added", "path": path}

@router.get("/connection")
async def get_connection()->list[str]:
    return find_connections()

@router.post("/data")
async def add_data(data: JsonContainerDto):
    path = save_data(data)
    return {"message": "Data added", "path": path}

@router.get("/data")
async def get_data()->list[str]:
    return find_data()

@router.post("/sample")
async def add_sample(sample: JsonContainerDto):
    path = save_sample(sample)
    return {"message": "Sample added", "path": path}

@router.get("/sample")
async def get_samples()->list[str]:
    return find_samples()

@router.post("/scenario")
async def add_scenario(scenario: ScenarioDto):
    path = save_scenario(scenario)
    return {"message": "Scenario added", "path": path}

@router.get("/scenario")
async def get_scenarios()->list[str]:
    return find_scenarios()