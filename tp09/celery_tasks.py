from celery import Celery
import requests

app = Celery('tasks', broker='amqp://guest@localhost//',backend="redis://localhost:6379/0")

@app.task
def add(x, y):
    return x + y

@app.task
def download(url):
    response = requests.get(url)
    d = {
        "url":url,
        "content":response.text
    }
    return d

@app.task
def save(d):
    log_file = d['url'].split("/")[-1]
    content = d['content']
    with open(f"./logs/{log_file}",'w') as f:
        f.write(content)
