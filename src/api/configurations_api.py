from fastapi import APIRouter

from configurations.sqllite_config import db
from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.json_type import JsonType
from models.scenario import ScenarioDto

router = APIRouter(prefix="/configuration")

@router.post("/connection")
async def add_connection(connection: QueueConnectionConfigTypes):
    db.insert_json(connection.name, JsonType.CONNECTION, connection.model_dump_json())
    return {"message": "Connection added"}

@router.get("/connection")
async def get_connection()->list[str]:
    return db.get_jsons_name_by_type(JsonType.CONNECTION)

@router.get("/connection/{name}")
async def get_connection(name:str)->dict:
    return db.get_json_by_name_and_type(name, JsonType.CONNECTION)

@router.delete("/connection/{name}")
async def delete_connection(name: str):
    count = db.delete_json_by_name_and_type(name, JsonType.CONNECTION)
    return {"message": f"{count} connection(s) deleted"}

@router.post("/data")
async def add_data(data: JsonContainerDto):
    db.insert_json(data.name, JsonType.DATA, data.model_dump_json())
    return {"message": "Data added"}

@router.get("/data")
async def get_data()->list[str]:
    return db.get_jsons_name_by_type(JsonType.DATA)

@router.get("/data/{name}")
async def get_data_json(name:str)->dict | list[dict]:
    return db.get_json_by_name_and_type(name, JsonType.DATA)

@router.delete("/data/{name}")
async def delete_data(name: str):
    count = db.delete_json_by_name_and_type(name, JsonType.DATA)
    return {"message": f"{count} data item(s) deleted"}

@router.post("/sample")
async def add_sample(sample: JsonContainerDto):
    db.insert_json(sample.name, JsonType.SAMPLE, sample.model_dump_json())
    return {"message": "Sample added"}

@router.get("/sample")
async def get_samples()->list[str]:
    return db.get_jsons_name_by_type(JsonType.SAMPLE)

@router.get("/sample/{name}")
async def get_sample(name:str)->dict | list[dict]:
    return db.get_json_by_name_and_type(name, JsonType.SAMPLE)

@router.delete("/sample/{name}")
async def delete_sample(name: str):
    result = db.delete_json_by_name_and_type(name, JsonType.SAMPLE)
    return {"message": f"{result} sample(s) deleted"}

@router.post("/scenario")
async def add_scenario(scenario: ScenarioDto):
    db.insert_json(scenario.name, JsonType.SCENARIO, scenario.model_dump_json())
    return {"message": "Scenario added"}

@router.get("/scenario")
async def get_scenarios()->list[str]:
    return db.get_jsons_name_by_type(JsonType.SCENARIO)

@router.get("/scenario/{name}")
async def get_scenario(name:str)->dict | list[dict]:
    return db.get_json_by_name_and_type(name, JsonType.SCENARIO)

@router.delete("/scenario/{name}")
async def delete_scenario(name: str):
    result = db.delete_json_by_name_and_type(name, JsonType.SCENARIO)
    return {"message": f"{result} scenario(s) deleted"}