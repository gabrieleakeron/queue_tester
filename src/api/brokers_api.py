from fastapi import APIRouter

from models.connection_configs.brokers.broker_connection_config_types import BrokerConnectionConfigTypes
from models.queue_dto import QueueDto
from models.sqs_requests.create_queue_dto import CreateQueueDto
from models.sqs_requests.delete_queue_dto import DeleteQueueDto
from models.sqs_requests.sqs_request_dto import SQSRequestDto
from services.broker_connections.broker_connection_service_factory import BrokerConnectionServiceFactory
from services.db.connection_service import load_broker_connection
from services.sqlite.queue_service import QueueService

router = APIRouter(prefix="/brokers")

@router.post("/queues")
async def list_queues(c: SQSRequestDto)->list[dict]:
    queues: list[QueueDto]= QueueService.get_all_by_broker(c.connectionConfig)
    result: list[dict] = []
    for queue in queues:
        result.append(queue.model_dump())
    return result

@router.post("/queue")
async def create_queue(c: CreateQueueDto):
    try:
        connection_config: BrokerConnectionConfigTypes = load_broker_connection(c.connectionConfig)
        service = BrokerConnectionServiceFactory.get_service(connection_config)
        result= service.create_queue(connection_config,c)
        QueueService.insert(QueueDto(
            broker=connection_config.name,
            name=c.name,
            url=result.get("queueUrl"),
            fifoQueue=c.fifoQueue,
            contentBasedDeduplication=c.contentBasedDeduplication,
            defaultVisibilityTimeout=c.defaultVisibilityTimeout,
            delay=c.delay,
            receiveMessageWait=c.receiveMessageWait
        ))
    except Exception as e:
        return {"error": str(e)}

    return result

@router.delete("/queue")
async def delete_queue(d: DeleteQueueDto):
    try:
        queue_dto:QueueDto|None = QueueService.get_by_name(d.name)
        if queue_dto is None:
            return {"error": f"Queue with name '{d.name}' not found"}

        connection_config: BrokerConnectionConfigTypes = load_broker_connection(d.connectionConfig)
        service = BrokerConnectionServiceFactory.get_service(connection_config)
        result = service.delete_queue(connection_config, queue_dto.url)
        QueueService.delete_by_name(queue_dto.name)

    except:
        return {"error": "Could not delete queue"}

    return result
