from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.scenario import ScenarioDto
from services.configurations.connection_service import load_connection
from services.configurations.file_service import create_json_file_from_model, load_json_file, find_files_name_in_dir, delete_file
from services.steps.step_executor_composite import execute_step

SCENARIOS_DIR= "scenarios"

def save_scenario(procedure: ScenarioDto):
    return create_json_file_from_model(SCENARIOS_DIR, procedure.name, procedure)

def load_scenario(name: str) -> ScenarioDto | None:
    return ScenarioDto(**load_json_file(SCENARIOS_DIR, name))

def find_scenarios():
    return find_files_name_in_dir(SCENARIOS_DIR)

def find_scenario_json(name:str)->dict | list[dict]:
    return load_json_file(SCENARIOS_DIR, name)

def delete_scenario(name: str) -> bool:
    return delete_file(SCENARIOS_DIR,name)

def execute_scenario(name: str)-> list[dict[str,str]]:

    dto = load_scenario(name)

    print("Executing scenario:", dto.name)

    connection_config:QueueConnectionConfigTypes = load_connection(dto.connectionConfig)

    results = []
    for step in dto.steps:
        print(f"Executing {step.description}")
        results.append(execute_step(connection_config,dto,step))

    return results






