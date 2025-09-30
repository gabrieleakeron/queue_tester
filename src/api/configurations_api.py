from models.json_container_dto import JsonContainerDto
from fastapi import APIRouter

from models.scenario import ScenarioDto
from services.data_service import create_data, find_data
from services.scenario_service import create_scenario, find_scenarios
from services.sample_service import create_sample, find_samples

router = APIRouter(prefix="/configuration")

@router.post("/data")
async def add_data(data: JsonContainerDto):
    path = create_data(data)
    return {"message": "Data added", "path": path}

@router.get("/data")
async def get_data()->list[str]:
    return find_data()

@router.post("/sample")
async def add_sample(sample: JsonContainerDto):
    path = create_sample(sample)
    return {"message": "Sample added", "path": path}

@router.get("/sample")
async def get_samples()->list[str]:
    return find_samples()

@router.post("/scenario")
async def add_scenario(procedure: ScenarioDto):
    path = create_scenario(procedure)
    return {"message": "Procedure added", "path": path}

@router.get("/scenario")
async def get_scenarios()->list[str]:
    return find_scenarios()