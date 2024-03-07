import requests
from bs4 import BeautifulSoup
import time
import threading
import concurrent.futures
import asyncio
import aiohttp



async def download(download_queue:asyncio.Queue,save_queue:asyncio.Queue):
    while True:
        url_log = await download_queue.get()
        async with aiohttp.ClientSession() as session:
            async with session.get(url_log) as response:
                text = await  response.text()
                d = {
                    "url_log":url_log,
                    "text":text
                }
                save_queue.put_nowait(d)
        download_queue.task_done()

async def save(save_queue:asyncio.Queue):
    while True:
        d = await save_queue.get()
        url_log = d['url_log']
        text = d['text']
        log = url_log.split("/")[-1]
        with open(f"./logs/{log}","w") as f:
            f.write(text)
        save_queue.task_done()


async def olddownload(url_log):
   
            with open(f"./logs/{log}","w") as f:
                f.write(text)

async def main():
    start = time.perf_counter()
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()



    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [url+l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    nb_download_workers = 10
    nb_save_workers = 5

    tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(download_queue,save_queue))
        tasks.append(task)
    
    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        tasks.append(task)


    for url in logs:
        download_queue.put_nowait(url)
    
    await download_queue.join()
    await save_queue.join()
    
    for task in tasks:
        task.cancel()


    end = time.perf_counter()
    print(end-start,"s")

if __name__=='__main__':
    asyncio.run(main())
