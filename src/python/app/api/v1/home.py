from fastapi import APIRouter, Depends

from src.python.app.api.deps import get_token_data

router = APIRouter(prefix="/home", tags=["Home"])


@router.get("/", dependencies=[Depends(get_token_data)])
async def home() -> str:
    return "Welcome Home!"