from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.operation import Operation
from models.scenario_dto import ScenarioDto
from models.steps.step_dto import StepDtoTypes
from services.operations.operation_executor import OperationExecutor
from services.operations.publish_executor import PublishExecutor
from services.operations.save_executor import SaveExecutor

_CONNECTOR_MAPPING: dict[Operation, type[OperationExecutor]] = {
    Operation.PUBLISH: PublishExecutor,
    Operation.SAVE: SaveExecutor,
}

def execute_operation(connection_config:QueueConnectionConfigTypes,scenario:ScenarioDto,step:StepDtoTypes, op:Operation,  data:list[dict])->dict:
    executor_class = _CONNECTOR_MAPPING.get(op)
    if executor_class is None:
        supported_types = list(_CONNECTOR_MAPPING.keys())
        raise ValueError(
            f"Unsupported operation type: {op}. "
            f"Supported types: {supported_types}"
        )
    operation_executor = executor_class()
    return operation_executor.execute(connection_config,scenario, step, op, data)