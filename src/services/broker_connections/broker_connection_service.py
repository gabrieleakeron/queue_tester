from abc import ABC, abstractmethod

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.queue_dto import QueueDto


class BrokerConnectionService(ABC):
    @abstractmethod
    def create_queue(self, connection_config:BrokerConnectionConfigTypes, q: QueueDto):
        pass

    @abstractmethod
    def delete_queue(self, connection_config:BrokerConnectionConfigTypes, queue_url: str):
        pass

    def list_queues(self, connection_config:BrokerConnectionConfigTypes):
        pass
