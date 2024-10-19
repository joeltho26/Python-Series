import asyncio

async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched...")
    return {"data": "some data"}

async def main():
    print("Start the main coroutine...")
    task = fetch_data(5)
    result = await task
    print(f"Received result: {result}")
    print("End of coroutine...")
    
asyncio.run(main())