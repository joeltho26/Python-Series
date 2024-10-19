import asyncio
#gather not efficient in error handling
# need to manually handle exceptions

async def fetch_data(id,sleep_time):
    print(f"Starting to fetch data:{id}...")
    await asyncio.sleep(sleep_time)
    print(f"Data fetched for {id}...")
    return {"data":"some data" + str(id)}

async def main():
    print("Start co-routine...")
    results = await asyncio.gather(fetch_data(1,10),fetch_data(2,5),fetch_data(3,3),fetch_data(4,1))
    for result in results:
        print(result)
    print("End co-routine...")
    
asyncio.run(main())