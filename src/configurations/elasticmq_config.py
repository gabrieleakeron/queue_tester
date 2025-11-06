from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.json_container_dto import JsonContainerDto
from models.json_type import JsonType
from services.broker_connections.broker_connection_service_factory import BrokerConnectionServiceFactory
from services.sqlite.json_files_service import JsonFilesService
from services.sqlite.queue_service import QueueService

def init_elasticmq():
    brokers : list[JsonContainerDto] = JsonFilesService.get_jsons_by_type(JsonType.BROKER_CONNECTION)
    for b in brokers:
        queues = QueueService.get_all_by_broker(b.name)
        brokers_connection:BrokerConnectionConfigTypes = BrokerConnectionConfigTypes.model_validate(b.json_data)
        service = BrokerConnectionServiceFactory.get_service(brokers_connection)
        for q in queues:
            service.create_queue(brokers_connection,q)

