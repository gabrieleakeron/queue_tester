import time

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.scenario import ScenarioDto
from models.steps.step_dto import SleepStepDto
from services.steps.step_executor import StepExecutor


class SleepStepExecutor(StepExecutor):
    def execute(cls, connection_config: QueueConnectionConfigTypes,scenario:ScenarioDto, step: SleepStepDto) -> list[dict[str, str]]:
        time.sleep(step.duration)
        return [{"status": "slept", "duration": str(step.duration)}]