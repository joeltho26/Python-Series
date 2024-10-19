import asyncio

async def fetch_data(delay, id):
    print(f"Fetching data for {id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched for {id}...")
    return {"data": "some data:" + str(id)}

async def main():
    print("Start the main coroutine...")
    
    result1 = await fetch_data(5,1)
    print(f"Received result: {result1}")
    result2 = await fetch_data(5,2)
    print(f"Received result: {result2}")
    
    print("End of coroutine...")
    
asyncio.run(main())