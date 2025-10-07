from fastapi import FastAPI

from api.configurations_api import router as configuration_router
from api.scenarios_api import router as procedure_router
from api.sqs_queues_api import router as queue_sqs_router

app = FastAPI()

# Includi i router delle API
app.include_router(configuration_router)
app.include_router(procedure_router)
app.include_router(queue_sqs_router)
