import asyncio


async def test_task(ctx: dict, word: str) -> str:
    await asyncio.sleep(10)
    return f"test task return {word}"
