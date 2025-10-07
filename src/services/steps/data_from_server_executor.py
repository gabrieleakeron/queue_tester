from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.scenario import ScenarioDto
from models.steps.step_dto import DataFromServerStepDto
from services.configurations.data_service import read_data
from services.operations.operation_executor_composite import execute_operation
from services.steps.step_executor import StepExecutor

class DataFromServerExecutor(StepExecutor):
    def execute(self, connection_config: QueueConnectionConfigTypes,scenario:ScenarioDto, step: DataFromServerStepDto) -> dict[str, str]:
        json_container:JsonContainerDto = read_data(step.data_name)
        return execute_operation(connection_config,scenario, step, step.operation, json_container.json_data)