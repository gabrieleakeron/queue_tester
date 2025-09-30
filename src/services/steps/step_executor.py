from abc import abstractmethod

from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.scenario import ScenarioDto
from models.steps.step_dto import StepDtoTypes


class StepExecutor:
    @abstractmethod
    def execute(self,connection_config:QueueConnectionConfigTypes,scenario:ScenarioDto, step:StepDtoTypes)->dict[str,str]:
        pass




