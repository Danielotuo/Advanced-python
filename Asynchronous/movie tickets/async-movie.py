
import time
import asyncio

start = time.time()

# Define an asynchronous coroutine that simulates getting movie tickets.
async def get_movie_tickets():
    await asyncio.sleep(8)
    print('tickets secured')

# Define an asynchronous coroutine that simulates liking a post on Instagram while in line.  
async def like_ig():
    await asyncio.sleep(2)
    print('Pic liked')

# Define an asynchronous coroutine that simulates liking a post on Instagram.
async def main():
    
    task1 = asyncio.create_task(get_movie_tickets())
    task2 = asyncio.create_task(like_ig())
    
    await task1
    

asyncio.run(main())

end = time.time()
print('Execution time', end - start)  
