from fastapi import APIRouter

from services.db.scenario_service import execute_scenario

router = APIRouter(prefix="/scenario")

@router.get("/execute/{name}")
async def execute(name):
    result = execute_scenario(name)
    return {"message": "Scenario executed", "result": result}

