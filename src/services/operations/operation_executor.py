from abc import abstractmethod, ABC

from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.operation import Operation
from models.scenario import ScenarioDto
from models.steps.step_dto import StepDto


class OperationExecutor(ABC):
    @abstractmethod
    def execute(self, connection_config:QueueConnectionConfigTypes, scenario:ScenarioDto, step:StepDto, op:Operation, data:list[dict])->dict[str,dict]:
        pass




