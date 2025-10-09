import copy

from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.scenario_dto import ScenarioDto
from models.steps.step_dto import DataFromSampleStepDto
from services.operations.operation_executor_composite import execute_operation
from services.db.sample_service import load_sample
from services.steps.step_executor import StepExecutor

def set_nested(d: dict, dotted_key: str, value):
    keys = dotted_key.split(".")

    current = d
    for k in keys[:-1]:
        if k.startswith("[") != -1 and k.endswith("]"):
            array = k[:k.index("[")]
            index = int(k[k.index("[")+1:-1])
            if array not in current or not isinstance(current[array], list):
                current[array] = []
            while len(current[array]) <= index:
                current[array].append({})
            current = current[array][index]
        else:
            if k not in current or not isinstance(current[k], (dict, list)):
                current[k] = {}
            current = current[k]

    last_key = keys[-1]
    if last_key.startswith("[") != -1 and last_key.endswith("]"):
        array = last_key[:last_key.index("[")]
        index = int(last_key[last_key.index("[")+1:-1])
        if array not in current or not isinstance(current[array], list):
            current[array] = []
        while len(current) <= index:
            current.append(None)
        current[array][index] = value
    else:
        current[last_key] = value

class DataFromSampleExecutor(StepExecutor):
    def execute(self, connection_config: QueueConnectionConfigTypes,scenario:ScenarioDto, step: DataFromSampleStepDto) -> dict[str, str]:
        sample = load_sample(step.sample_name)

        input_data = []
        for row in step.data:
            new_json = copy.deepcopy(sample.json_data)
            for key, value in row.items():
                set_nested(new_json, key, value)
            input_data.append(new_json)

        return execute_operation(connection_config,scenario, step,step.operation,input_data)