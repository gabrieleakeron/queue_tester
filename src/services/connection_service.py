from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from services.file_service import create_json_file_from_model, create_json_file_from_dict, load_json_file, \
    find_files_name_in_dir

CONNECTION_DIR= "connections"

def save_connection(connection: QueueConnectionConfigTypes):
    return create_json_file_from_model(CONNECTION_DIR, connection.name, connection)

def load_connection(name: str) -> QueueConnectionConfigTypes | None:
    return QueueConnectionConfigTypes(**load_json_file(CONNECTION_DIR, name))

def find_connections()->list[str]:
    return find_files_name_in_dir(CONNECTION_DIR)