import asyncio

#co-routine function
async def main():
    print("start the main coroutine")
    
#await is used only inside the co-routine function
#main() -> co-routine object, we need provide co-routine object inside asyncio.run() method.
    
asyncio.run(main())

