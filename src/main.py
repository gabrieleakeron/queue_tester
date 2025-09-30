from fastapi import FastAPI

from api.configurations_api import router as configuration_router
from api.scenarios_api import router as procedure_router

app = FastAPI()

# Includi i router delle API
app.include_router(configuration_router)
app.include_router(procedure_router)
