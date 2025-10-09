from fastapi import APIRouter

from services.db.scenario_service import execute_scenario
from services.sqlite.scenario_results_service import ScenarioResultsService

router = APIRouter(prefix="/scenario")

@router.get("/execute/{name}")
async def execute(name):
    execute_scenario(name)
    return {"message": "Scenario started"}

@router.get("/results/{name}")
async def results(name:str):
    return ScenarioResultsService.get_results_by_scenario(name)

@router.delete("/clean/{name}")
async def clean(name:str):
    result = ScenarioResultsService.delete_by_scenario(name)
    return {"message": f"{result} result(s) deleted"}

