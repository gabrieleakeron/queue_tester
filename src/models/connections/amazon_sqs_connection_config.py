from models.connections.connection_config import ConnectionConfig


class AmazonSQSConnectionConfig(ConnectionConfig):
    sourceType: str = "amazon-sqs"
    region:str
    queueUrl:str
    secretsAccessKey:str
    accessKeyId:str
    consume:bool = False
    payloadSchema: str | None = None
    payloadSample: str | None = None
