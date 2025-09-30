from pydantic import BaseModel

from models.operation import Operation

class StepDto(BaseModel):
    stepType: str
    description: str

class SleepStepDto(StepDto):
    stepType: str = "sleep"
    duration: int

class DataFromServerStepDto(StepDto):
    stepType: str = "data-from-server"
    data_name: str
    operation: Operation

class DataStepDTO(StepDto):
    stepType: str = "data"
    data: list[dict]
    operation: Operation

class DataFromSampleStepDto(DataStepDTO):
    stepType: str = "data-from-sample"
    sample_name: str
    operation: Operation

StepDtoTypes = StepDto | SleepStepDto | DataStepDTO | DataFromSampleStepDto | DataFromServerStepDto