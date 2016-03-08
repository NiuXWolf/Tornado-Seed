# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
from celery.task import task
import logging
import logging.config

logging.config.fileConfig("log.conf")
logger = logging.getLogger("example01")

@task
def add_task(a,b):
    logger.debug('This is task add')
    logger.warning('This is task add')
    print a+b
