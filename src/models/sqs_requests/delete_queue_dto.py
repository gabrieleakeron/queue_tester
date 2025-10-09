from models.sqs_requests.sqs_request_dto import SQSRequestDto

class DeleteQueueDto(SQSRequestDto):
    queue_url:str