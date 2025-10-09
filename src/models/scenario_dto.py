from pydantic import BaseModel
from models.steps.step_dto import StepDtoTypes

class ScenarioDto(BaseModel):
    name: str
    description: str
    connectionConfig:str
    steps: list[StepDtoTypes]


