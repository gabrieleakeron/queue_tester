from pydantic import BaseModel


class SQSRequestDto(BaseModel):
    connectionConfig:str