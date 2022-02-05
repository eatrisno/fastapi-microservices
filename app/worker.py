import asyncio

from dotenv import load_dotenv
from arq import create_pool

import uvloop
from arq.connections import RedisSettings
from app.core.config import settings
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def test_task(ctx, word: str):
    await asyncio.sleep(10)
    return f"test task return {word}"

async def startup(ctx):
    print("start")

async def shutdown(ctx):
    print("end")
class WorkerSettings:
    functions = [test_task]
    redis_settings = RedisSettings(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False
    max_jobs = settings.MAX_JOBS