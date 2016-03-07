#from tasks import app

from celery.task import task

# import logging
# import logging.config

# logging.config.fileConfig("log.conf")
# logger = logging.getLogger("example02")

@task
def add(a,b):
    # logger.debug('This is task add')
    # logger.warning('This is task add')
    print a+b
