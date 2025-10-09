from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.json_type import JsonType
from services.sqlite.json_files_service import JsonFilesService


def load_queue_connection(name: str):

    payload = JsonFilesService.get_json_by_name_and_type(name, JsonType.QUEUE_CONNECTION)

    if not payload:
        raise ValueError(f"Connection config '{name}' not found")

    return QueueConnectionConfigTypes.model_validate(payload)

def load_broker_connection(name: str):

    payload = JsonFilesService.get_json_by_name_and_type(name, JsonType.BROKER_CONNECTION)

    if not payload:
        raise ValueError(f"Connection config '{name}' not found")

    return BrokerConnectionConfigTypes.model_validate(payload)