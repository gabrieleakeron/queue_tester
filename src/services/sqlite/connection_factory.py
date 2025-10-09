import sqlite3

DB_PATH = "data/queue_tester.db"

class ConnectionFactory:
    @classmethod
    def create_connection(cls):
        return sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False, autocommit=True)