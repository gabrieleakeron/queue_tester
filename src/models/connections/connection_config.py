from pydantic import BaseModel

class ConnectionConfig(BaseModel):
    name:str
    sourceType: str