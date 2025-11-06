from fastapi import FastAPI

from configurations.elasticmq_config import init_elasticmq
from configurations.sqllite_config import init_db
from exceptions.app_exception import AppException
from exceptions.exception_handler import app_exception_handler, generic_exception_handler

init_db()
init_elasticmq()

from api.configurations_api import router as configurations_router
from api.scenarios_api import router as scenarios_router
from api.sqs_queues_api import router as queue_sqs_router
from api.logs_api import router as logs_router
from api.brokers_api import router as brokers_router
from api.json_utils_api import router as json_utils_router

app = FastAPI()

# Includi i router delle API
app.include_router(configurations_router)
app.include_router(scenarios_router)
app.include_router(queue_sqs_router)
app.include_router(logs_router)
app.include_router(brokers_router)
app.include_router(json_utils_router)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
