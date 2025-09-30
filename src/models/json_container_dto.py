from pydantic import BaseModel

class JsonContainerDto(BaseModel):
    name: str
    json_data: dict | list[dict]