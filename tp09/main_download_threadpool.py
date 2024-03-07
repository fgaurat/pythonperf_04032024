import requests
from bs4 import BeautifulSoup
import time
import threading
import concurrent.futures




def download(url_log):
    response = requests.get(url_log)
    log = url_log.split("/")[-1]
    text = response.text
    with open(f"./logs/{log}","w") as f:
        f.write(text)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [url+l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    print(logs)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,logs)
    
    


    end = time.perf_counter()
    print(end-start,"s")

if __name__=='__main__':
    main()
