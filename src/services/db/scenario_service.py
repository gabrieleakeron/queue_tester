from models.json_type import JsonType
from models.scenario_dto import ScenarioDto
from services.scenarios.ScenarioExecutorThread import ScenarioExecutorThread
from services.sqlite.json_files_service import JsonFilesService


def load_scenario(name:str)-> ScenarioDto:
    payload = JsonFilesService.get_json_by_name_and_type(name, JsonType.SCENARIO)

    if not payload:
        raise ValueError(f"Scenario '{name}' not found")

    dto = ScenarioDto.model_validate(payload)

    return dto

def execute_scenario(name: str):
    ScenarioExecutorThread(name).start()


