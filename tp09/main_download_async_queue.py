import requests
from bs4 import BeautifulSoup
import time
import threading
import concurrent.futures
import asyncio
import aiohttp



async def download(url_log):
    async with aiohttp.ClientSession() as session:
        async with session.get(url_log) as response:
            log = url_log.split("/")[-1]
            text = await  response.text()
            with open(f"./logs/{log}","w") as f:
                f.write(text)

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [url+l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    tasks = [download(log) for log in logs]
    await asyncio.gather(*tasks)

    end = time.perf_counter()
    print(end-start,"s")

if __name__=='__main__':
    asyncio.run(main())
