from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.scenario import ScenarioDto
from models.steps.step_dto import DataStepDTO
from services.operations.operation_executor_composite import execute_operation
from services.steps.step_executor import StepExecutor


class DataStepExecutor(StepExecutor):
    def execute(self, connection_config: QueueConnectionConfigTypes,scenario:ScenarioDto, step: DataStepDTO) -> dict[str, dict]:
        return execute_operation(connection_config,scenario,step, step.operation, step.data)