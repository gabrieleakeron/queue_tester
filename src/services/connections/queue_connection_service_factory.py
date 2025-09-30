from models.connections.amazon_sqs_connection_config import AmazonSQSConnectionConfig
from models.connections.connection_config import ConnectionConfig
from services.connections.amazon_sqs_connection_service import AmazonSQSConnectionService
from services.connections.queue_connection_service import QueueConnectionService


class QueueConnectionServiceFactory:

    _CONNECTOR_MAPPING: dict[type[ConnectionConfig], type[QueueConnectionService]] = {
        AmazonSQSConnectionConfig: AmazonSQSConnectionService,
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
