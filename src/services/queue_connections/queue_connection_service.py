from abc import ABC, abstractmethod
from typing import Any

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes


class QueueConnectionService(ABC):

    @abstractmethod
    def test_connection(self, broker_connection_config:BrokerConnectionConfigTypes,queue_url:str) -> bool:
        pass

    @abstractmethod
    def publish_messages(
            self,
            broker_connection_config:BrokerConnectionConfigTypes,
            queue:str,
            messages: list[Any]) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def receive_messages(
            self,
            broker_connection_config:BrokerConnectionConfigTypes,
            queue:str,
            max_messages: int = 10,
    ) -> list[Any]:
        pass

    @abstractmethod
    def ack_messages(
            self,
            broker_connection_config:BrokerConnectionConfigTypes,
            queue:str,
            messages: list[Any]
    ) -> list[dict]:
        pass

