from celery import Celery
from pronoun_count import analyze

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def pronoun_counter(dir: str):
    return analyze(dir)