from typing import Optional
from arq import create_pool
from arq.connections import RedisSettings, ArqRedis

pool: Optional[ArqRedis] = None

async def enqueue_job(key, message):
    redis = await create_pool(RedisSettings())
    return await redis.enqueue_job(key, message)