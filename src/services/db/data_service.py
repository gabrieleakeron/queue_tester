from models.json_container_dto import JsonContainerDto

from models.json_type import JsonType
from services.sqlite.json_files_service import JsonFilesService


def load_data(name: str) -> JsonContainerDto | None:
    payload = JsonFilesService.get_json_by_name_and_type(name, JsonType.DATA)
    if not payload:
        raise ValueError(f"Data '{name}' not found")
    return JsonContainerDto.model_validate(payload)
