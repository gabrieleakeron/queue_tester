from fastapi import FastAPI

from configurations.sqllite_config import init_db
from exceptions.app_exception import AppException
from exceptions.exception_handler import app_exception_handler

# Inizializza il database SQLite
init_db()

from api.configurations_api import router as configuration_router
from api.scenarios_api import router as procedure_router
from api.sqs_queues_api import router as queue_sqs_router

app = FastAPI()

# Includi i router delle API
app.include_router(configuration_router)
app.include_router(procedure_router)
app.include_router(queue_sqs_router)

app.add_exception_handler(AppException, app_exception_handler)
