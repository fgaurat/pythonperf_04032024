import requests
from bs4 import BeautifulSoup
import time
import threading

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

    logs = [l['href'] for l in soup.find_all("a") if ".log" in l['href']]

    all_th = []
    for log in logs:
        url_log = f"{url}{log}"
        th = threading.Thread(target=download,args=[url_log])
        th.start()
        all_th.append(th)
    
    [th.join() for th in all_th ]
    end = time.perf_counter()
    print(end-start,"s")

if __name__=='__main__':
    main()
