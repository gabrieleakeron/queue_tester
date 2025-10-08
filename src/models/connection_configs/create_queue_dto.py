from models.connection_configs.sqs_request_dto import SQSRequestDto
from models.queue_dto import QueueDto

class CreateQueueDto(SQSRequestDto):
    queue:QueueDto