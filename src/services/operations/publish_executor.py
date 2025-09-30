from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.operation import Operation
from models.scenario import ScenarioDto
from models.steps.step_dto import StepDto
from services.operations.operation_executor import OperationExecutor
from services.queue_connections.queue_connection_service_factory import QueueConnectionServiceFactory


class PublishExecutor(OperationExecutor):
    def execute(self, connection_config:QueueConnectionConfigTypes,scenario:ScenarioDto, step:StepDto, operation: Operation, data:list[dict]):
        service = QueueConnectionServiceFactory().get_service(connection_config)
        return service.publish_messages(connection_config,data)
