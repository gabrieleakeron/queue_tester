import json
import sqlite3
import uuid
from typing import Any

from exceptions.app_exception import AppException
from models.json_type import JsonType


class Sqlite:

    def __init__(self):
        self._init()

    def _connect(self):
        return sqlite3.connect("data/queue_tester.db", timeout=30, check_same_thread=False)

    def _init(self):
        with self._connect() as cx:
            cx.execute("PRAGMA journal_mode=WAL;")
            cx.execute("PRAGMA synchronous=NORMAL;")
            cx.execute("PRAGMA temp_store=MEMORY;")
            cx.execute("PRAGMA cache_size=-50000;")
            cx.execute("""
                CREATE TABLE IF NOT EXISTS json_files(
                  id TEXT PRIMARY KEY,
                  name TEXT,
                  type TEXT,
                  payload TEXT,
                  processed_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cx.commit()

    def insert_json(self, name: str, j_type: str, payload:str)->str:
        id = str(uuid.uuid4())
        with self._connect() as cx:
            cursor = cx.execute("""
             SELECT COUNT(*) FROM json_files WHERE name = ? AND type = ?""",
                                (name, j_type))
            row = cursor.fetchone()
            if row and row[0] > 0:
                raise AppException(f"'{j_type}' entity with name '{name}' already exists.")
        with self._connect() as cx:
            cx.execute("""
                INSERT INTO json_files (id, name, type, payload)
                VALUES (?, ?, ?, ?)
            """, (id, name, j_type, payload))
            cx.commit()
        return id

    def get_json_by_name_and_type(self, name: str, j_type: str)->dict|None:
        with self._connect() as cx:
            cursor = cx.execute("""
                SELECT payload
                FROM json_files
                WHERE name = ? AND type = ?
            """, (name, j_type))
            row = cursor.fetchone()
            if row:
                return json.loads(row[0]) if row[0] else None
            return None

    def get_jsons_name_by_type(self,j_type: str):
        with self._connect() as cx:
            cursor = cx.execute("""
                SELECT name
                FROM json_files
                WHERE type = ?
            """, (j_type,))
            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def delete_json_by_name_and_type(self, name: str, j_type: str)->Any:
        with self._connect() as cx:
            result = cx.execute("""
                DELETE FROM json_files
                WHERE name = ? AND type = ?
            """, (name, j_type))
            cx.commit()

            return result.rowcount
