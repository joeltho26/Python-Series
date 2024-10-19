import asyncio

async def access_resources(semaphore, resource_id):
    async with semaphore:
        print(f"Accessing resources {resource_id}")
        await asyncio.sleep(2)
        
        
async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resources(semaphore,i) for i in range(5)))
    
asyncio.run(main())