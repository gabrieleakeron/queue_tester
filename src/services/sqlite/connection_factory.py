import sqlite3
import os

DB_PATH = "data/queue_tester.db"

class ConnectionFactory:
    @classmethod
    def create_connection(cls):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        return sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False, autocommit=True)