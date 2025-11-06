from models.sqs_requests.sqs_request_dto import SQSRequestDto


class SQSRequestTestDto(SQSRequestDto):
    queue: str
