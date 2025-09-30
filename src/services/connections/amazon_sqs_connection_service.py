from typing import Any

import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from models.connections.amazon_sqs_connection_config import AmazonSQSConnectionConfig
from services.connections.queue_connection_service import QueueConnectionService

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
