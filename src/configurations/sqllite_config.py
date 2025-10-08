from services.sqlite.sqlite_json_service import Sqlite

db:Sqlite|None = None

def init_db():
    global db
    db = Sqlite()