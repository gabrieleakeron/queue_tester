from abc import ABC, abstractmethod
from typing import Any

from models.connections.connection_config_types import QueueConnectionConfigTypes

class QueueConnectionService(ABC):
    @abstractmethod
    def publish_messages(
            self,
            config: QueueConnectionConfigTypes,
            messages: list[Any])->list[dict[str, Any]]:
        pass