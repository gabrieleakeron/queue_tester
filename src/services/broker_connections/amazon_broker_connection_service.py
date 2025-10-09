import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from models.connection_configs.brokers.amazon_broker_connection_config import AmazonBrokerConnectionConfig
from models.queue_dto import QueueDto
from services.broker_connections.broker_connection_service import BrokerConnectionService

DEFAULT_VISIBILITY_TIMEOUT = 30

def client(config: AmazonBrokerConnectionConfig)->BaseClient:
    return boto3.client(
        "sqs",
        region_name=config.region,
        endpoint_url=config.endpointUrl,
        aws_access_key_id=config.accessKeyId,
        aws_secret_access_key=config.secretsAccessKey,
    )

class AmazonBrokerConnectionService(BrokerConnectionService):

    def create_queue(self,config:AmazonBrokerConnectionConfig, q: QueueDto):
        sqs: BaseClient = client(config)

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

    def delete_queue(self, config:AmazonBrokerConnectionConfig, queueUrl:str):
        sqs: BaseClient = client(config)
        try:
            sqs.delete_queue(QueueUrl=queueUrl)
            print(f" Coda eliminata: {queueUrl} ")
            return {"message": f"Queue {queueUrl} deleted successfully"}
        except ClientError as e:
            raise Exception(f"Error deleting SQS queue: {e}")

    def list_queues(self, config:AmazonBrokerConnectionConfig):
        sqs: BaseClient = client(config)
        try:
            resp = sqs.list_queues()
            queue_urls = resp.get("QueueUrls", [])
            print(f" Code trovate: {len(queue_urls)} ")
            return {"queueUrls": queue_urls}
        except ClientError as e:
            raise Exception(f"Error listing SQS queues: {e}")
