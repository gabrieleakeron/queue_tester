from models.connection_configs.brokers.amazon_broker_connection_config import AmazonBrokerConnectionConfig
from models.connection_configs.connection_config import ConnectionConfig
from services.broker_connections.amazon_broker_connection_service import AmazonBrokerConnectionService
from services.broker_connections.broker_connection_service import BrokerConnectionService


class BrokerConnectionServiceFactory:

    _CONNECTOR_MAPPING: dict[type[ConnectionConfig], type[BrokerConnectionService]] = {
        AmazonBrokerConnectionConfig:AmazonBrokerConnectionService
    }

    @classmethod
    def get_service(cls, config: ConnectionConfig) -> BrokerConnectionService:

        config_type = type(config)
        service_class = cls._CONNECTOR_MAPPING.get(config_type)

        if service_class is None:
            supported_types = list(cls._CONNECTOR_MAPPING.keys())
            raise ValueError(
                f"Unsupported connector type: {config_type}. "
                f"Supported types: {supported_types}"
            )

        return service_class()
