import asyncio
import uvloop
from arq.connections import RedisSettings
from worker.core.config import settings
from worker import tasks

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def startup(ctx: dict) -> None:
    print("start")


async def shutdown(ctx: dict) -> None:
    print("end")


class WorkerSettings:
    functions = [tasks.test_task, tasks.hello_task]
    redis_settings = RedisSettings(settings().REDIS_HOST, port=settings().REDIS_PORT)
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False
