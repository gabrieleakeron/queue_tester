from fastapi import APIRouter

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.sqs_requests.sqs_request_find_dto import SQSRequestFindDto
from models.sqs_requests.sqs_request_messages_dto import SQSRequestMessagesDto
from models.sqs_requests.test_queue_dto import SQSRequestTestDto
from services.db.connection_service import load_broker_connection
from services.queue_connections.queue_connection_service_factory import QueueConnectionServiceFactory

router = APIRouter(prefix="/queue-sqs")

@router.post("/publish")
async def publish_messages(m: SQSRequestMessagesDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(m.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.publish_messages(connection_config, queue=m.queue, messages=m.messages)

@router.post("/test")
async def test_connection(t: SQSRequestTestDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(t.connectionConfig)
    if connection_config is None:
        return {"message": f"Connection {t.connectionConfig} not found"}, 404
    service = QueueConnectionServiceFactory.get_service(connection_config)
    if not service.test_connection(connection_config,t.queue):
        return {"message": f"Connection is not valid"}, 400
    return {"message": f"Connection is valid"}

@router.post("/message")
async def receive_messages(f: SQSRequestFindDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(f.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    msgs = service.receive_messages(connection_config, queue=f.queue, max_messages=f.count)
    print(msgs)
    return msgs

@router.post("/ack")
async def ack_messages(d:SQSRequestMessagesDto):
    connection_config: BrokerConnectionConfigTypes = load_broker_connection(d.connectionConfig)
    service = QueueConnectionServiceFactory.get_service(connection_config)
    return service.ack_messages(connection_config, queue=d.queue, messages=d.messages)