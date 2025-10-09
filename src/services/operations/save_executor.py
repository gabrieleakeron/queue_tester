import json

from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.operation import Operation
from models.scenario_dto import ScenarioDto
from models.steps.step_dto import StepDto
from services.operations.operation_executor import OperationExecutor
from services.sqlite.scenario_results_service import ScenarioResultsService


class SaveExecutor(OperationExecutor):
    def execute(self,connection_config:QueueConnectionConfigTypes, scenario:ScenarioDto, step:StepDto, operation: Operation, data:list[dict])->dict[str, str]:

        rows = 0
        for index, item in enumerate(data):
            ScenarioResultsService.insert(scenario.name, step.description, json.dumps(item))
            rows += 1

        return {"message": f"Created {rows} rows in scenario_results table"}
