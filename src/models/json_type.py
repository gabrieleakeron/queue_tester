from enum import Enum


class JsonType(str,Enum):
    BROKER_CONNECTION = "broker-connection"
    QUEUE_CONNECTION = "queue-connection"
    DATABASE_CONNECTION = "database-connection"
    SCENARIO = "scenario"
    SAMPLE = "sample"
    DATA = "data"