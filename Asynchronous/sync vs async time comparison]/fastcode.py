import asyncio
import time

start = time.time()


async def fetch_file():
    print ('starting file fetch')
    await asyncio.sleep(1)
    print('file fetch completed')
    
async def main():
    print('Starting main')
    await asyncio.gather(
    fetch_file(),
    fetch_file(),
    fetch_file()
    )
    print('Main completed')
    
    
asyncio.run(main())

end = time.time()
print('Execution time:', (end - start))