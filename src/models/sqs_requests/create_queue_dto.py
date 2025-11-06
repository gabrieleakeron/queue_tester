from models.sqs_requests.sqs_request_dto import SQSRequestDto
from models.queue_dto import QueueDto

class CreateQueueDto(SQSRequestDto):
    name: str
    fifoQueue: bool = False
    contentBasedDeduplication: bool = False
    defaultVisibilityTimeout: int = 30
    delay: int = 0
    receiveMessageWait: int = 0