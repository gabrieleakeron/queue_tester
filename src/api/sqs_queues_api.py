from fastapi import APIRouter

from models.connection_configs.queues.queue_connection_config_types import QueueConnectionConfigTypes
from models.sqs_requests.sqs_request_dto import SQSRequestDto
from models.sqs_requests.sqs_request_find_dto import SQSRequestFindDto
from models.sqs_requests.sqs_request_messages_dto import SQSRequestMessagesDto
from services.db.connection_service import load_queue_connection
from services.queue_connections.queue_connection_service_factory import QueueConnectionServiceFactory

router = APIRouter(prefix="/queue-sqs")

@router.post("/publish")
async def publish_messages(m: SQSRequestMessagesDto):
    connection_config:QueueConnectionConfigTypes = load_queue_connection(m.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.publish_messages(connection_config, m.messages)

@router.post("/test")
async def test_connection(t: SQSRequestDto):
    connection_config: QueueConnectionConfigTypes = load_queue_connection(t.connectionConfig)
    if connection_config is None:
        return {"message": f"Connection {t.connectionConfig} not found"}, 404
    service = QueueConnectionServiceFactory.get_service(connection_config)
    if not service.test_connection(connection_config):
        return {"message": f"Connection is not valid"}, 400
    return {"message": f"Connection is valid"}

@router.post("/message")
async def receive_messages(f: SQSRequestFindDto):
    connection_config: QueueConnectionConfigTypes = load_queue_connection(f.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.receive_messages(connection_config, max_messages=f.count)

@router.post("/ack")
async def ack_messages(d:SQSRequestMessagesDto):
    connection_config: QueueConnectionConfigTypes = load_queue_connection(d.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.ack_messages(connection_config, d.messages)