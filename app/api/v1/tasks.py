from arq.jobs import Job
from fastapi import APIRouter
from arq import create_pool
from arq.connections import RedisSettings

from app.core import redis
from app.schemas.job import Job

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=Job, status_code=201)
async def create_task(message: str):
    redis = await create_pool(RedisSettings())
    job = await redis.enqueue_job(message)
    return {"id": job.job_id}

@router.get("/{task_id}/")
async def get_task(task_id: str):
    job = Job(task_id, redis.pool)
    return await job.info()