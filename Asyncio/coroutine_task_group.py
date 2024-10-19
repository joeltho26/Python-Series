import asyncio

async def fetch_data(id,sleep_time):
    print(f"starting to fetch data:{id}")
    await asyncio.sleep(sleep_time)
    print(f"fetched data{id}...")
    return {"data":"some data " + str(id)}

async def main():
    tasks=[]
    print("starting routine...")
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
            
    results = [task.result() for task in tasks]
    
    for result in results:
        print(result)
        
asyncio.run(main())