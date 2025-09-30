from models.connections.connection_config_types import QueueConnectionConfigTypes
from pydantic import BaseModel

from models.steps.step_dto import StepDto, StepDtoTypes


class ScenarioDto(BaseModel):
    name: str
    description: str
    connection_config:QueueConnectionConfigTypes
    steps: list[StepDtoTypes]


