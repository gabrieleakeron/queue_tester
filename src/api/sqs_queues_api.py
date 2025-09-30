from fastapi import APIRouter

from models.connections.connection_config_types import QueueConnectionConfigTypes
from models.connections.sqs_request_dto import SQSRequestMessagesDto, SQSRequestFindDto
from services.connection_service import load_connection
from services.queue_connections.queue_connection_service_factory import QueueConnectionServiceFactory

router = APIRouter(prefix="/queue-sqs")

@router.post("/publish")
async def publish_messages(m: SQSRequestMessagesDto):
    connection_config:QueueConnectionConfigTypes = load_connection(m.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.publish_messages(connection_config, m.messages)

@router.post("/message")
async def receive_messages(f: SQSRequestFindDto):
    connection_config: QueueConnectionConfigTypes = load_connection(f.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.receive_messages(connection_config, max_messages=f.count)

@router.delete("/message")
async def delete_messages(d:SQSRequestMessagesDto):
    connection_config: QueueConnectionConfigTypes = load_connection(d.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.delete_messages(connection_config, d.messages)