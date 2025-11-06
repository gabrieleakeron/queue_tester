import json
import uuid
from typing import Any

from exceptions.app_exception import AppException
from models.json_type import JsonType
from models.queue_dto import QueueDto
from services.sqlite.connection_factory import ConnectionFactory


class QueueService:
    @classmethod
    def insert(cls,queue_dto:QueueDto)->str:
        id = str(uuid.uuid4())
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
             SELECT COUNT(*) FROM queues WHERE broker = ? AND name = ?""",(queue_dto.broker, queue_dto.name))
            row = cursor.fetchone()
            if row and row[0] > 0:
                raise AppException(f"Queue with name '{queue_dto.name}' already exists. In broker '{queue_dto.broker}'")
        with ConnectionFactory.create_connection() as cx:
            cx.execute("""
                INSERT INTO queues (id, broker, name, payload)
                VALUES (?, ?, ?, ?)
            """, (id, queue_dto.broker, queue_dto.name, queue_dto.model_dump_json()))
        return id

    @classmethod
    def get_by_name(cls,name:str)->QueueDto|None:
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
                SELECT payload
                FROM queues
                WHERE name = ?
            """, (name,))
            row = cursor.fetchone()
            if row:
                return QueueDto.model_validate(json.loads(row[0]))
            return None

    @classmethod
    def get_all_by_broker(cls,broker:str)->list[QueueDto]:
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
                SELECT payload
                FROM queues
                WHERE broker = ?
            """, (broker,))
            rows = cursor.fetchall()
            return [QueueDto.model_validate(json.loads(row[0])) for row in rows]

    @classmethod
    def delete_by_name(cls, name: str)->Any:
        with ConnectionFactory.create_connection() as cx:
            result = cx.execute("""
                DELETE FROM queues
                WHERE name = ?
            """, (name,))
            return result.rowcount

    @classmethod
    def delete_by_broker(cls, broker: str)->Any:
        with ConnectionFactory.create_connection() as cx:
            result = cx.execute("""
                DELETE FROM queues
                WHERE broker = ?
            """, (broker,))
            return result.rowcount