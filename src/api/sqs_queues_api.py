from fastapi import APIRouter

from models.connections.sqs_request_dto import SQSRequestMessagesDto, SQSRequestFindDto
from services.queue_connections.queue_connection_service_factory import QueueConnectionServiceFactory

router = APIRouter(prefix="/queue-sqs")

@router.post("/publish")
async def publish_messages(m: SQSRequestMessagesDto):
    service = QueueConnectionServiceFactory.get_service(m.config)
    return service.publish_messages(m.config, m.messages)

@router.post("/message")
async def receive_messages(f: SQSRequestFindDto):
    service = QueueConnectionServiceFactory.get_service(f.config)
    return service.receive_messages(f.config, max_messages=f.count)

@router.delete("/message")
async def delete_messages(d:SQSRequestMessagesDto):
    service = QueueConnectionServiceFactory.get_service(d.config)
    return service.delete_messages(d.config, d.messages)