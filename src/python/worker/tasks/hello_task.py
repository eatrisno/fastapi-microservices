import asyncio

async def hello_task(ctx: dict, word: str) -> str:
    return f"Hello {word}"