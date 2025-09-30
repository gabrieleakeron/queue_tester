from models.scenario import ScenarioDto
from services.file_service import create_json_file_from_model, load_json_file, find_files_name_in_dir
from services.steps.step_executor_composite import execute_step

SCENARIOS_DIR= "scenarios"

def create_scenario(procedure: ScenarioDto):
    return create_json_file_from_model(SCENARIOS_DIR, procedure.name, procedure)

def load_scenario(name: str) -> ScenarioDto | None:
    return ScenarioDto(**load_json_file(SCENARIOS_DIR, name))

def execute_scenario(name: str)-> list[dict[str,str]]:

    dto = load_scenario(name)

    print("Executing scenario:", dto.name)

    results = []
    for step in dto.steps:
        print(f"Executing {step.description}")
        results.append(execute_step(dto.connection_config,step))

    return results

def find_scenarios():
    return find_files_name_in_dir(SCENARIOS_DIR)







