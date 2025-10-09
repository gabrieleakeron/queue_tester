import json
import uuid
from typing import Any

from exceptions.app_exception import AppException
from services.sqlite.connection_factory import ConnectionFactory


class JsonFilesService:
    @classmethod
    def insert_json(cls, name: str, j_type: str, payload:str)->str:
        id = str(uuid.uuid4())
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
             SELECT COUNT(*) FROM json_files WHERE name = ? AND type = ?""",
                                (name, j_type))
            row = cursor.fetchone()
            if row and row[0] > 0:
                raise AppException(f"'{j_type}' entity with name '{name}' already exists.")
        with ConnectionFactory.create_connection() as cx:
            cx.execute("""
                INSERT INTO json_files (id, name, type, payload)
                VALUES (?, ?, ?, ?)
            """, (id, name, j_type, payload))
        return id

    @classmethod
    def get_json_by_name_and_type(cls, name: str, j_type: str)->dict|None:
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
                SELECT payload
                FROM json_files
                WHERE name = ? AND type = ?
            """, (name, j_type))
            row = cursor.fetchone()
            if row:
                return json.loads(row[0]) if row[0] else None
            return None

    @classmethod
    def get_jsons_name_by_type(cls,j_type: str):
        with ConnectionFactory.create_connection() as cx:
            cursor = cx.execute("""
                SELECT name
                FROM json_files
                WHERE type = ?
            """, (j_type,))
            rows = cursor.fetchall()
            return [row[0] for row in rows]

    @classmethod
    def delete_json_by_name_and_type(cls, name: str, j_type: str)->Any:
        with ConnectionFactory.create_connection() as cx:
            result = cx.execute("""
                DELETE FROM json_files
                WHERE name = ? AND type = ?
            """, (name, j_type))
            return result.rowcount
