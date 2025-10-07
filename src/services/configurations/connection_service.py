from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from services.configurations.file_service import create_json_file_from_model, load_json_file, \
    find_files_name_in_dir, delete_file

CONNECTION_DIR= "connections"

def save_connection(connection: QueueConnectionConfigTypes):
    return create_json_file_from_model(CONNECTION_DIR, connection.name, connection)

def load_connection(name: str) -> QueueConnectionConfigTypes | None:
    return QueueConnectionConfigTypes(**load_json_file(CONNECTION_DIR, name))

def find_connections()->list[str]:
    return find_files_name_in_dir(CONNECTION_DIR)

def find_connection_json(name: str) -> dict | list[dict]:
    return load_json_file(CONNECTION_DIR, name)

def delete_connection(name: str) -> bool:
    return delete_file(CONNECTION_DIR,name)