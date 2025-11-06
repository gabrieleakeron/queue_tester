import json

from fastapi import APIRouter
from genson import SchemaBuilder

router = APIRouter(prefix="/json_utils")

@router.post("/schema")
async def extract_schema(json_input:str)->str:
    try:
        data = json.loads(json_input)
        builder = SchemaBuilder()
        builder.add_object(data)
        schema = builder.to_schema()
        return json.dumps(schema, indent=2)
    except json.JSONDecodeError:
        return "Invalid JSON input."