import threading

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_type import JsonType
from models.logs.log_type import LogLevel
from models.scenario_dto import ScenarioDto
from services.sqlite.json_files_service import JsonFilesService
from services.sqlite.log_service import log
from services.sqlite.scenario_results_service import ScenarioResultsService
from services.steps.step_executor_composite import execute_step


class ScenarioExecutorThread(threading.Thread):

    def __init__(self,name:str):
        super().__init__(name=f"scenario-{name}",daemon=True)

        self.payload = JsonFilesService.get_json_by_name_and_type(name, JsonType.SCENARIO)
        if not self.payload:
            raise ValueError(f"Scenario '{name}' not found")

        self.scenario_dto = ScenarioDto.model_validate(self.payload)

        connection_cfg = self.scenario_dto.connectionConfig
        payload = JsonFilesService.get_json_by_name_and_type(connection_cfg, JsonType.CONNECTION)
        if not payload:
            raise ValueError(f"Connection config {connection_cfg} for scenario '{self.scenario_dto.name}' not found")

        self.connection_config: QueueConnectionConfigTypes = QueueConnectionConfigTypes.model_validate(payload)

        ScenarioResultsService.delete_by_scenario(self.scenario_dto.name)

    def run(self):
        print(f"Executing scenario {self.scenario_dto.name}...")

        results = []

        try:
            for step in self.scenario_dto.steps:
                print(f"Executing {step.description}")
                results.append(execute_step(self.connection_config, self.scenario_dto, step))

            log(message=f"Scenario '{self.scenario_dto.name}' executed with {len(results)} step(s)")

        except Exception as e:
            log(message=f"Error executing scenario '{self.scenario_dto.name}': {str(e)}", level=LogLevel.ERROR)



