from configurations.sqllite_config import db
from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_type import JsonType
from models.scenario import ScenarioDto
from services.steps.step_executor_composite import execute_step


def execute_scenario(name: str)-> list[dict[str,str]]:

    payload = db.get_json_by_name_and_type(name, JsonType.SCENARIO)
    if not payload:
        raise ValueError(f"Scenario '{name}' not found")

    dto = ScenarioDto.model_validate(payload)

    print("Executing scenario:", dto.name)

    payload = db.get_json_by_name_and_type(dto.connectionConfig, JsonType.CONNECTION)
    if not payload:
        raise ValueError(f"Connection config {dto.connectionConfig}for scenario '{name}' not found")

    connection_config:QueueConnectionConfigTypes = QueueConnectionConfigTypes.model_validate(payload)

    results = []
    for step in dto.steps:
        print(f"Executing {step.description}")
        results.append(execute_step(connection_config,dto,step))

    return results


