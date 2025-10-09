
from models.json_container_dto import JsonContainerDto
from models.json_type import JsonType
from services.sqlite.json_files_service import JsonFilesService


def load_sample(sample_name: str) -> JsonContainerDto | None:
    payload = JsonFilesService.get_json_by_name_and_type(sample_name,JsonType.SAMPLE)
    if not payload:
        raise ValueError(f"Sample '{sample_name}' not found")
    return JsonContainerDto.model_validate(payload)