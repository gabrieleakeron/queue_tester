from models.json_container_dto import JsonContainerDto
from services.configurations.file_service import create_json_file_from_dict, load_json_file, find_files_name_in_dir, delete_file

SAMPLES_DIR = "samples"

def save_sample(sample: JsonContainerDto):
    return create_json_file_from_dict(SAMPLES_DIR, sample.name, sample.json_data)

def load_sample(sample_name: str) -> JsonContainerDto | None:
    json_data = load_json_file(SAMPLES_DIR, sample_name)
    return JsonContainerDto(name=sample_name, json_data=json_data)

def find_samples()->list[str]:
    return find_files_name_in_dir(SAMPLES_DIR)

def find_sample_json(name:str)->dict | list[dict]:
    return load_json_file(SAMPLES_DIR, name)

def delete_sample(name: str) -> bool:
    return delete_file(SAMPLES_DIR,name)