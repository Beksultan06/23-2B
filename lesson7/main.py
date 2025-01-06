import aioschedule as schedule
import asyncio

async def task():
    print("Задача выполняется")

async def hello():
    print("Hello world")

async def start_task():
    schedule.every(1).second.do(task)
    schedule.every(1).second.do(hello)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(2)

asyncio.run(start_task())