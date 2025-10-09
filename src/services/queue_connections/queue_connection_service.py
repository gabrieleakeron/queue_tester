from abc import ABC, abstractmethod
from typing import Any

from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.queue_dto import QueueDto


class QueueConnectionService(ABC):

    @abstractmethod
    def test_connection(self, config: QueueConnectionConfigTypes) -> bool:
        pass

    @abstractmethod
    def publish_messages(
            self,
            config: QueueConnectionConfigTypes,
            messages: list[Any]) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def receive_messages(
            self,
            config: QueueConnectionConfigTypes,
            max_messages: int = 10,
    ) -> list[Any]:
        pass

    @abstractmethod
    def ack_messages(
            self,
            config: QueueConnectionConfigTypes,
            messages: list[Any]
    ) -> list[str]:
        pass

    @abstractmethod
    def create_queue(self, connection_config:QueueConnectionConfigTypes, q: QueueDto):
        pass

    @abstractmethod
    def delete_queue(self, connection_config:QueueConnectionConfigTypes):
        pass

    def list_queues(self, connection_config:QueueConnectionConfigTypes):
        pass
