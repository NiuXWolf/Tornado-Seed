from celery import Celery
from .seed_task import add

app = Celery('tasks')
app.config_from_object('tasks.celeryconfig')

# @app.task
# def add(a,b):
#     print a+b

if __name__ == '__main__':
    app.start()
