from configurations.sqllite_config import db
from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.json_type import JsonType


def load_connection(name: str):
    payload = db.get_json_by_name_and_type(name, JsonType.CONNECTION)

    if not payload:
        raise ValueError(f"Connection config '{name}' not found")

    return QueueConnectionConfigTypes.model_validate(payload)