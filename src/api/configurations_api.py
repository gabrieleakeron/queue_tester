from fastapi import APIRouter

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.scenario import ScenarioDto
from services.configurations.connection_service import save_connection, find_connections, find_connection_json, \
    delete_connection
from services.configurations.data_service import save_data, find_data, find_data_json, delete_data
from services.configurations.sample_service import save_sample, find_samples, find_sample_json, delete_sample
from services.configurations.scenario_service import save_scenario, find_scenarios, find_scenario_json, delete_scenario

router = APIRouter(prefix="/configuration")

@router.post("/connection")
async def add_connection(connection: QueueConnectionConfigTypes):
    path = save_connection(connection)
    return {"message": "Connection added", "path": path}

@router.get("/connection")
async def get_connection()->list[str]:
    return find_connections()

@router.get("/connection/{name}")
async def get_connection(name:str)->dict | list[dict]:
    return find_connection_json(name)

@router.delete("/connection/{name}")
async def delete_connection_api(name: str):
    success = delete_connection(name)
    if success:
        return {"message": "Connection deleted"}
    else:
        return {"message": "Connection not found"}, 404

@router.post("/data")
async def add_data(data: JsonContainerDto):
    path = save_data(data)
    return {"message": "Data added", "path": path}

@router.get("/data")
async def get_data()->list[str]:
    return find_data()

@router.get("/data/{name}")
async def get_data_json(name:str)->dict | list[dict]:
    return find_data_json(name)

@router.delete("/data/{name}")
async def delete_data_api(name: str):
    success = delete_data(name)
    if success:
        return {"message": "Data deleted"}
    else:
        return {"message": "Data not found"}, 404

@router.post("/sample")
async def add_sample(sample: JsonContainerDto):
    path = save_sample(sample)
    return {"message": "Sample added", "path": path}

@router.get("/sample")
async def get_samples()->list[str]:
    return find_samples()

@router.get("/sample/{name}")
async def get_sample(name:str)->dict | list[dict]:
    return find_sample_json(name)

@router.delete("/sample/{name}")
async def delete_sample_api(name: str):
    success = delete_sample(name)
    if success:
        return {"message": "Sample deleted"}
    else:
        return {"message": "Sample not found"}, 404

@router.post("/scenario")
async def add_scenario(scenario: ScenarioDto):
    path = save_scenario(scenario)
    return {"message": "Scenario added", "path": path}

@router.get("/scenario")
async def get_scenarios()->list[str]:
    return find_scenarios()

@router.get("/scenario/{name}")
async def get_scenario(name:str)->dict | list[dict]:
    return find_scenario_json(name)

@router.delete("/scenario/{name}")
async def delete_scenario_api(name: str):
    success = delete_scenario(name)
    if success:
        return {"message": "Scenario deleted"}
    else:
        return {"message": "Scenario not found"}, 404