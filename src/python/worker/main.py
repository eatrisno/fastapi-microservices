import asyncio
from cmath import log

import uvloop
from arq.connections import RedisSettings

from worker.core.config import settings
from worker.tasks import test_task, hello_task

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def startup(ctx: dict) -> None:
    print("start")


async def shutdown(ctx: dict) -> None:
    print("end")


class WorkerSettings:
    functions = [test_task, hello_task]
    redis_settings = RedisSettings(settings().REDIS_HOST, port=settings().REDIS_PORT)
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False