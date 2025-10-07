from pydantic import BaseModel

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes


class SQSRequestDto(BaseModel):
    config:QueueConnectionConfigTypes