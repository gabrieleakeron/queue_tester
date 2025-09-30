from typing import Any

import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from models.connections.amazon_sqs_connection_config import AmazonSQSConnectionConfig
from services.queue_connections.queue_connection_service import QueueConnectionService

SHORT_VISIBILITY_TIMEOUT = 5
DEFAULT_VISIBILITY_TIMEOUT = 30
MAX_NUMBER_OF_MESSAGES = 10
WAIT_TIME_SECONDS = 20

def client(config: AmazonSQSConnectionConfig)->BaseClient:
    return boto3.client(
        "sqs",
        region_name=config.region,
        aws_access_key_id=config.accessKeyId,
        aws_secret_access_key=config.secretsAccessKey,
    )

def test_connection(sqs,config: AmazonSQSConnectionConfig):
    try:
        sqs.get_queue_attributes(QueueUrl=config.queueUrl, AttributeNames=["All"])
    except ClientError as e:
        raise Exception(f"Error accessing SQS queue: {e}")

class AmazonSQSConnectionService(QueueConnectionService):

    def publish_messages(self,config:AmazonSQSConnectionConfig, messages:list[Any]) -> list[dict[str, Any]]:

        sqs = client(config)
        test_connection(sqs,config)
        results = []

        for msg in messages:

            try:
                msg = str(msg)

                resp = sqs.send_message(
                    QueueUrl=config.queueUrl,
                    MessageBody=msg,
                )

                mid = resp.get("MessageId")
                http_status = resp.get("ResponseMetadata", {}).get("HTTPStatusCode")

                results.append({"status": "ok", "message_id": mid, "http_status": http_status})

            except Exception as e:
                results.append({"status": "error", "error": str(e), "message": msg})

        return results

    def receive_messages(self,config: AmazonSQSConnectionConfig, max_messages: int = 10) -> list[Any]:
        sqs: BaseClient = client(config)
        test_connection(sqs,config)

        all_msgs = []

        to_receive = min(MAX_NUMBER_OF_MESSAGES, max_messages - len(all_msgs))
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

        return all_msgs

    def delete_messages(self,config: AmazonSQSConnectionConfig, messages: list[Any]) -> list[str]:
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
