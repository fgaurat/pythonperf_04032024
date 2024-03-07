from celery import Celery,signature,group,chain
import requests
from bs4 import BeautifulSoup


def main():
    app = Celery('tasks', broker='amqp://guest@localhost//',backend="redis://localhost:6379/0")
    
    
    # add_task = signature('celery_tasks.add')
    # r = add_task.delay(2,3)
    # print(r.get()) 

    # tasks = app.tasks.keys()
    # print(tasks) 
    # i = app.control.inspect()
    # print(i.scheduled())

    # # Show tasks that are currently active.
    # print(i.active())

    # # Show tasks that have been claimed by workers
    # print(i.reserved())
    
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [url+l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    print(logs)
    # download = signature('celery_tasks.download')
    # r = download.delay(logs[0])
    # print(r.get())

    # #Download
    # download_tasks = [signature('celery_tasks.download',args=[url]) for url in logs]
    # download_group =group(download_tasks)
    # result = download_group()
    # all_downloads = result.get()

    # #Save
    # save_tasks = [signature('celery_tasks.save',args=[to_save]) for to_save in all_downloads]
    # save_group =group(save_tasks)
    # save_group()

    for url in logs:
         chain(
            signature('celery_tasks.download',args=[url]),
            signature('celery_tasks.save')
        )()  

if __name__=='__main__':
    main()
