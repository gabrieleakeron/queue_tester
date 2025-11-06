from abc import ABC, abstractmethod

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.sqs_requests.create_queue_dto import CreateQueueDto


class BrokerConnectionService(ABC):
    @abstractmethod
    def create_queue(self, connection_config:BrokerConnectionConfigTypes, q: CreateQueueDto):
        pass

    @abstractmethod
    def delete_queue(self, connection_config:BrokerConnectionConfigTypes, queue_url: str):
        pass

    def list_queues(self, connection_config:BrokerConnectionConfigTypes):
        pass
