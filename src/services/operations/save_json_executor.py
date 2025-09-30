import json
from pathlib import Path

from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.operation import Operation
from models.scenario import ScenarioDto
from models.steps.step_dto import StepDto
from services.operations.operation_executor import OperationExecutor

def create_json(_dir:str, name:str, data: dict):

    dir_path = Path(__file__).parent.parent.parent / "tmp"
    dir_path.mkdir(exist_ok=True)

    dir_path = dir_path / _dir
    dir_path.mkdir(exist_ok=True)

    path = dir_path / f"{name}.json"

    with path.open("w") as f:
        json.dump(data, f, indent=2)

    return path

class SaveTempExecutor(OperationExecutor):
    def execute(self,connection_config:QueueConnectionConfigTypes, scenario:ScenarioDto, step:StepDto, operation: Operation, data:list[dict])->dict[str, str]:
        files: list[Path] = []

        output_dir = scenario.name

        for index, item in enumerate(data):
            files.append(create_json(output_dir,f"{step.description.replace(" ", "-")}-{index}",item))

        return {"message": f"Created {len(files)} JSON files in tmp directory"}
