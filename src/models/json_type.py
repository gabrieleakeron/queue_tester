from enum import Enum


class JsonType(Enum):
    BROKER_CONNECTION = "broker-connection"
    QUEUE_CONNECTION = "queue-connection"
    DATABASE_CONNECTION = "database-connection"
    SCENARIO = "scenario"
    SAMPLE = "sample"
    DATA = "data"