from typing import Any

from fastapi import APIRouter

from services.sqlite.log_service import LogService

router = APIRouter(prefix="/logs")

@router.get("/")
async def get_logs() -> list[dict[str,Any]]:
    return LogService.get_logs()