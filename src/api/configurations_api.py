from fastapi import APIRouter



from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.json_type import JsonType
from models.scenario_dto import ScenarioDto
from services.sqlite.json_files_service import JsonFilesService

router = APIRouter(prefix="/configuration")

### QUEUE CONNECTIONS

@router.post("/connection/queue")
async def add_queue_connection(connection: QueueConnectionConfigTypes):
    JsonFilesService.insert_json(connection.name, JsonType.QUEUE_CONNECTION, connection.model_dump_json())
    return {"message": "Connection added"}

@router.get("/connection/queue")
async def get_queue_connections()->list[str]:
    return JsonFilesService.get_jsons_name_by_type(JsonType.QUEUE_CONNECTION)

@router.get("/connection/queue/{name}")
async def get_queue_connection(name:str)->dict:
    queue_connection = JsonFilesService.get_json_by_name_and_type(name, JsonType.QUEUE_CONNECTION)
    if not queue_connection:
        return {"message": f"Connection '{name}' not found"}
    return queue_connection

@router.delete("/connection/queue/{name}")
async def delete_queue_connection(name: str):
    count = JsonFilesService.delete_json_by_name_and_type(name, JsonType.QUEUE_CONNECTION)
    return {"message": f"{count} connection(s) deleted"}

### BROKER CONNECTIONS

@router.post("/connection/broker")
async def add_broker_connection(connection: BrokerConnectionConfigTypes):
    JsonFilesService.insert_json(connection.name, JsonType.BROKER_CONNECTION, connection.model_dump_json())
    return {"message": "Connection added"}

@router.get("/connection/broker")
async def get_broker_connections()->list[str]:
    return JsonFilesService.get_jsons_name_by_type(JsonType.BROKER_CONNECTION)

@router.get("/connection/broker/{name}")
async def get_broker_connection(name:str)->dict:
    return JsonFilesService.get_json_by_name_and_type(name, JsonType.BROKER_CONNECTION)

@router.delete("/connection/broker/{name}")
async def delete_broker_connection(name: str):
    count = JsonFilesService.delete_json_by_name_and_type(name, JsonType.BROKER_CONNECTION)
    return {"message": f"{count} connection(s) deleted"}


### DATA

@router.post("/data")
async def add_data(data: JsonContainerDto):
    JsonFilesService.insert_json(data.name, JsonType.DATA, data.model_dump_json())
    return {"message": "Data added"}

@router.get("/data")
async def get_data()->list[str]:
    return JsonFilesService.get_jsons_name_by_type(JsonType.DATA)

@router.get("/data/{name}")
async def get_data_json(name:str)->dict | list[dict]:
    return JsonFilesService.get_json_by_name_and_type(name, JsonType.DATA)

@router.delete("/data/{name}")
async def delete_data(name: str):
    count = JsonFilesService.delete_json_by_name_and_type(name, JsonType.DATA)
    return {"message": f"{count} data item(s) deleted"}

### SAMPLES

@router.post("/sample")
async def add_sample(sample: JsonContainerDto):
    JsonFilesService.insert_json(sample.name, JsonType.SAMPLE, sample.model_dump_json())
    return {"message": "Sample added"}

@router.get("/sample")
async def get_samples()->list[str]:
    return JsonFilesService.get_jsons_name_by_type(JsonType.SAMPLE)

@router.get("/sample/{name}")
async def get_sample(name:str)->dict | list[dict]:
    return JsonFilesService.get_json_by_name_and_type(name, JsonType.SAMPLE)

@router.delete("/sample/{name}")
async def delete_sample(name: str):
    result = JsonFilesService.delete_json_by_name_and_type(name, JsonType.SAMPLE)
    return {"message": f"{result} sample(s) deleted"}

### SCENARIOS

@router.post("/scenario")
async def add_scenario(scenario: ScenarioDto):
    JsonFilesService.insert_json(scenario.name, JsonType.SCENARIO, scenario.model_dump_json())
    return {"message": "Scenario added"}

@router.get("/scenario")
async def get_scenarios()->list[str]:
    return JsonFilesService.get_jsons_name_by_type(JsonType.SCENARIO)

@router.get("/scenario/{name}")
async def get_scenario(name:str)->dict | list[dict]:
    return JsonFilesService.get_json_by_name_and_type(name, JsonType.SCENARIO)

@router.delete("/scenario/{name}")
async def delete_scenario(name: str):
    result = JsonFilesService.delete_json_by_name_and_type(name, JsonType.SCENARIO)
    return {"message": f"{result} scenario(s) deleted"}