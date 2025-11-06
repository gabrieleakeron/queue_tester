from typing import Any

from models.sqs_requests.sqs_request_dto import SQSRequestDto


class SQSRequestMessagesDto(SQSRequestDto):
    queue:str
    messages: list[Any]