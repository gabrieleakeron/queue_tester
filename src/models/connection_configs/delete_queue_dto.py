from models.connection_configs.sqs_request_dto import SQSRequestDto


class DeleteQueueDto(SQSRequestDto):
    name:str