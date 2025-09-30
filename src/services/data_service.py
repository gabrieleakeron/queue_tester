from models.json_container_dto import JsonContainerDto
from services.file_service import create_json_file_from_dict, load_json_file, find_files_name_in_dir

DATA_DIR = "data"

def save_data(data: JsonContainerDto):
    return create_json_file_from_dict(DATA_DIR, data.name, data.json_data)

def read_data(name: str) -> JsonContainerDto | None:
    return JsonContainerDto(name=name,json_data=load_json_file(DATA_DIR, name))

def find_data()->list[str]:
    return find_files_name_in_dir(DATA_DIR)