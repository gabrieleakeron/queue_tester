from models.sqs_requests.sqs_request_dto import SQSRequestDto
from models.queue_dto import QueueDto

class CreateQueueDto(SQSRequestDto):
    queue:QueueDto