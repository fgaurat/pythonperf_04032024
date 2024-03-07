import asyncio
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()

    # print('Hello ...')
    # asyncio.sleep(1)
    # print('... World!')
    # a = await add(5,6)
    # b = await add(59,6)
    # print(a)
    # print(b)
    c = [add(1,6),add(2,6),add(3,6),add(4,6),add(5,6)]

    r = await asyncio.gather(*c)
    print(r)
    end = time.perf_counter()
    print(end-start,"s")
if __name__=='__main__':
    asyncio.run(main())

