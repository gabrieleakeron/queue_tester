from fastapi import APIRouter

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.sqs_requests.create_queue_dto import CreateQueueDto
from models.sqs_requests.delete_queue_dto import DeleteQueueDto
from models.sqs_requests.sqs_request_dto import SQSRequestDto
from services.broker_connections.broker_connection_service_factory import BrokerConnectionServiceFactory
from services.db.connection_service import load_broker_connection

router = APIRouter(prefix="/brokers")

@router.post("/queues")
async def list_queues(c: SQSRequestDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(c.connectionConfig)
    service = BrokerConnectionServiceFactory.get_service(connection_config)
    return service.list_queues(connection_config)

@router.post("/queue")
async def create_queue(c: CreateQueueDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(c.connectionConfig)
    service = BrokerConnectionServiceFactory.get_service(connection_config)
    return service.create_queue(connection_config,c.queue)

@router.delete("/queue")
async def delete_queue(d: DeleteQueueDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(d.connectionConfig)
    service = BrokerConnectionServiceFactory.get_service(connection_config)
    return service.delete_queue(connection_config,d.queue_url)
