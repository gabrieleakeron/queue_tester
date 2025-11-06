from models.sqs_requests.sqs_request_dto import SQSRequestDto


class SQSRequestFindDto(SQSRequestDto):
    queue: str
    count: int