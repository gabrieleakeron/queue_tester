from abc import abstractmethod

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.scenario_dto import ScenarioDto
from models.steps.step_dto import StepDtoTypes


class StepExecutor:
    @abstractmethod
    def execute(self,connection_config:QueueConnectionConfigTypes,scenario:ScenarioDto, step:StepDtoTypes)->dict[str,str]:
        pass




