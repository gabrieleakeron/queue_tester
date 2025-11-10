import json

from fastapi import APIRouter
from genson import SchemaBuilder

from models.json_container_dto import JsonContainerDto

router = APIRouter(prefix="/json_utils")

@router.post("/schema")
async def extract_schema(dto:JsonContainerDto)-> dict | str:
    try:
        builder = SchemaBuilder()
        builder.add_object(dto.json_data)
        schema = builder.to_schema()
        schema['title'] = dto.name
        return schema
    except json.JSONDecodeError:
        return "Invalid JSON input."