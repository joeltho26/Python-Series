import asyncio

async def fetch_data(id,sleep_time):
    print(f"fetching data for id-{id}...")
    await asyncio.sleep(sleep_time)
    return {"data": "some data " + str(id)}

async def main():
    print("Start coroutine...")
    task1 = asyncio.create_task(fetch_data(1,5))
    task2 = asyncio.create_task(fetch_data(2,5))
    task3 = asyncio.create_task(fetch_data(3,7))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, result2, result3)
    print("End routine...")
    
asyncio.run(main())