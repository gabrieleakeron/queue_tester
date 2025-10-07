from typing import Any

from models.connection_configs.sqs_request_dto import SQSRequestDto


class SQSRequestMessagesDto(SQSRequestDto):
    messages: list[Any]