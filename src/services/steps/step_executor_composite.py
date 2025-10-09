from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.scenario_dto import ScenarioDto
from models.steps.step_dto import DataStepDTO, DataFromSampleStepDto, SleepStepDto, DataFromServerStepDto, \
    StepDto, StepDtoTypes
from services.steps.data_from_sample_executor import DataFromSampleExecutor
from services.steps.data_from_server_executor import DataFromServerExecutor
from services.steps.data_step_executor import DataStepExecutor
from services.steps.sleep_step_executor import SleepStepExecutor
from services.steps.step_executor import StepExecutor

_CONNECTOR_MAPPING: dict[type[StepDto], type[StepExecutor]] = {
    SleepStepDto: SleepStepExecutor,
    DataStepDTO: DataStepExecutor,
    DataFromServerStepDto:DataFromServerExecutor,
    DataFromSampleStepDto: DataFromSampleExecutor
}

def execute_step(connection_config:QueueConnectionConfigTypes, scenario:ScenarioDto, step:StepDtoTypes)->dict[str,str]:
    executor_class = _CONNECTOR_MAPPING.get(type(step))
    if executor_class is None:
        supported_types = list(_CONNECTOR_MAPPING.keys())
        raise ValueError(
            f"Unsupported step type: {step.stepType}. "
            f"Supported types: {supported_types}"
        )
    step_executor = executor_class()
    return step_executor.execute(connection_config,scenario, step)