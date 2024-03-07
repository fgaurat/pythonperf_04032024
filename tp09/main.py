import requests
from bs4 import BeautifulSoup
import time
def main():
    start = time.perf_counter()
    
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    print(logs)


    for log in logs:
        url_log = f"{url}{log}"
        response = requests.get(url_log)
        text = response.text
        with open(f"./logs/{log}","w") as f:
            f.write(text)
    end = time.perf_counter()
    print(end-start,"s")

if __name__=='__main__':
    main()
