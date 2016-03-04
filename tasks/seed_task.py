from celery.task import task

@task
def add(a,b):
    return a+b;
