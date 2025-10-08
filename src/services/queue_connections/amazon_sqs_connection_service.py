import json
from typing import Any

import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError
from urllib.parse import urlparse

from models.connection_configs.amazon_sqs_connection_config import AmazonSQSConnectionConfig
from models.connection_configs.connection_config_types import QueueConnectionConfigTypes
from models.connection_configs.create_queue_dto import CreateQueueDto
from models.queue_dto import QueueDto
from services.queue_connections.queue_connection_service import QueueConnectionService

SHORT_VISIBILITY_TIMEOUT = 5
DEFAULT_VISIBILITY_TIMEOUT = 30
MAX_NUMBER_OF_MESSAGES = 10
WAIT_TIME_SECONDS = 20

def extract_endpoint_from_queue_url(queue_url: str) -> str:
    parsed = urlparse(queue_url)
    return f"{parsed.scheme}://{parsed.hostname}:{parsed.port}" if parsed.port else f"{parsed.scheme}://{parsed.hostname}"

def client(config: AmazonSQSConnectionConfig)->BaseClient:
    return boto3.client(
        "sqs",
        region_name=config.region,
        endpoint_url=extract_endpoint_from_queue_url(config.queueUrl),
        aws_access_key_id=config.accessKeyId,
        aws_secret_access_key=config.secretsAccessKey,
    )

def test_connection(sqs,config: AmazonSQSConnectionConfig):
    try:
        sqs.get_queue_attributes(QueueUrl=config.queueUrl, AttributeNames=["All"])
    except ClientError as e:
        raise Exception(f"Error accessing SQS queue: {e}")

class AmazonSQSConnectionService(QueueConnectionService):

    def test_connection(self, config: QueueConnectionConfigTypes) -> bool:
        sqs = client(config)
        test_connection(sqs,config)
        return True

    def publish_messages(self,config:AmazonSQSConnectionConfig, messages:list[Any]) -> list[dict[str, Any]]:

        sqs = client(config)
        test_connection(sqs,config)
        results = []

        for msg in messages:

            try:
                resp = sqs.send_message(
                    QueueUrl=config.queueUrl,
                    MessageBody=json.dumps(msg),
                )

                mid = resp.get("MessageId")
                http_status = resp.get("ResponseMetadata", {}).get("HTTPStatusCode")

                results.append({"status": "ok", "message_id": mid, "http_status": http_status})
                print(f" Messaggio pubblicato  MessageId={mid} ")

            except Exception as e:
                results.append({"status": "error", "error": str(e), "message": msg})

        return results

    def receive_messages(self,config: AmazonSQSConnectionConfig, max_messages: int = 10) -> list[Any]:
        sqs: BaseClient = client(config)
        test_connection(sqs,config)

        all_msgs = []

        to_receive = min(MAX_NUMBER_OF_MESSAGES, max_messages)
        resp = sqs.receive_message(
            QueueUrl=config.queueUrl,
            MaxNumberOfMessages=to_receive,
            WaitTimeSeconds=WAIT_TIME_SECONDS,
            VisibilityTimeout=SHORT_VISIBILITY_TIMEOUT
        )

        msgs = resp.get("Messages", []) or []

        if not msgs:
            return all_msgs

        for m in msgs:
            all_msgs.append(m)

        print(f" Messaggi ricevuti: {len(msgs)} ")

        return all_msgs

    def ack_messages(self, config: AmazonSQSConnectionConfig, messages: list[Any]):
        sqs: BaseClient = client(config)
        test_connection(sqs,config)

        deleted_msgs:list[str] = []
        for m in messages:
            try:
                sqs.delete_message(
                    QueueUrl=config.queueUrl,
                    ReceiptHandle=m["ReceiptHandle"]
                )
                mid = m["MessageId"]
                deleted_msgs.append(mid)
                print(f" Messaggio eliminato  MessageId={mid} ")
            except ClientError as e:
                mid = m.get("MessageId", "unknown")
                print(f" Errore eliminazione messaggio  MessageId={mid} Error={e}")

        return deleted_msgs

    def create_queue(self,config:AmazonSQSConnectionConfig, q: QueueDto):
        sqs: BaseClient = client(config)
        test_connection(sqs,config)

        attributes = self.create_attributes(q)

        try:
            resp = sqs.create_queue(
                QueueName=q.name,
                Attributes=attributes
            )
            queue_url = resp.get("QueueUrl")
            print(f" Coda creata: {queue_url} ")
            return {"queueUrl": queue_url}

        except ClientError as e:
            raise Exception(f"Error creating SQS queue: {e}")

    def create_attributes(self, q:QueueDto):
        attributes = {
            "VisibilityTimeout": str(q.defaultVisibilityTimeout or DEFAULT_VISIBILITY_TIMEOUT),
            "DelaySeconds": str(q.delay or 0),
            "ReceiveMessageWaitTimeSeconds": str(q.receiveMessageWait or 0),
        }

        if q.fifoQueue:
            attributes["FifoQueue"] = "true"
            if not q.name.endswith(".fifo"):
                q.name += ".fifo"
            if q.contentBasedDeduplication:
                attributes["ContentBasedDeduplication"] = "true"

        return attributes

    def delete_queue(self,config:AmazonSQSConnectionConfig, name:str):
        sqs: BaseClient = client(config)
        test_connection(sqs,config)

        try:
            sqs.delete_queue(QueueUrl=config.queueUrl)
            print(f" Coda eliminata: {config.queueUrl} ")
            return {"message": f"Queue {name} deleted successfully"}
        except ClientError as e:
            raise Exception(f"Error deleting SQS queue: {e}")
