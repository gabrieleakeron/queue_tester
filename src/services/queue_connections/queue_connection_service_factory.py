from models.connection_configs.brokers.amazon_broker_connection_config import AmazonBrokerConnectionConfig
from models.connection_configs.connection_config import ConnectionConfig
from models.connection_configs.queues.amazon_sqs_connection_config import AmazonSQSConnectionConfig
from services.queue_connections.amazon_sqs_connection_service import AmazonSQSConnectionService
from services.queue_connections.queue_connection_service import QueueConnectionService


class QueueConnectionServiceFactory:

    _CONNECTOR_MAPPING: dict[type[ConnectionConfig], type[QueueConnectionService]] = {
        AmazonSQSConnectionConfig: AmazonSQSConnectionService,
        AmazonBrokerConnectionConfig:AmazonSQSConnectionService
    }

    @classmethod
    def get_service(cls, config: ConnectionConfig) -> QueueConnectionService:

        config_type = type(config)
        service_class = cls._CONNECTOR_MAPPING.get(config_type)

        if service_class is None:
            supported_types = list(cls._CONNECTOR_MAPPING.keys())
            raise ValueError(
                f"Unsupported connector type: {config_type}. "
                f"Supported types: {supported_types}"
            )

        return service_class()
