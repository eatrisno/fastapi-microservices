from arq.jobs import Job as ArqJob
from fastapi import APIRouter, Depends

from app.api.deps import on_user
from app.core import redis
from app.schemas.job import Job

router = APIRouter(prefix="/tasks", tags=["Tasks"], dependencies=[Depends(on_user)])


@router.post("/", response_model=Job, status_code=201)
async def create_task(message: str):
    resp = await redis.enqueue_job("test_task", message)
    return {"id": resp.job_id}


@router.post("/hello", response_model=Job, status_code=201)
async def create_task(message: str):
    resp = await redis.enqueue_job("hello_task", message)
    return {"id": resp.job_id}


@router.get("/{task_id}/")
async def get_task(task_id: str):
    job = ArqJob(task_id, redis.pool)
    return str(await job.info())
