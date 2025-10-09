from models.connection_configs.connection_config import ConnectionConfig


class AmazonBrokerConnectionConfig(ConnectionConfig):
    sourceType: str = "amazon-sqs"
    endpointUrl:str
    region:str
    secretsAccessKey:str
    accessKeyId:str
