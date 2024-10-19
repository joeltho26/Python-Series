import asyncio

#future doesnt wait for the entire task or coroutine to complete just for the value needed
#future is the promise of a future/later result

async def set_future_result(future, value: str) -> None:
    future.set_result(value)
    await asyncio.sleep(4)
    print(f"set the result to: {value}")
    
async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future() 
    
    task = asyncio.create_task(set_future_result(future, "Future result is ready!"))
    result = await future
    print(result)
    
    result2 = await task
    
asyncio.run(main())
    