import asyncio

async def square(num):
    return num * num


async def main():
    x = await square(5)
    print(x)
    
    y = await square(10)
    print(y)
    
    z = x + y
    print(z)
    
asyncio.run(main())