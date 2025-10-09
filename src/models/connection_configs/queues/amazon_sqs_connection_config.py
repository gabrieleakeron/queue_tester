from models.connection_configs.connection_config import ConnectionConfig


class AmazonSQSConnectionConfig(ConnectionConfig):
    sourceType: str = "amazon-sqs"
    region:str
    queueUrl:str
    secretsAccessKey:str
    accessKeyId:str
