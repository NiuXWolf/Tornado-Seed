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

# from cron.writer import note
# # A periodic task that will run every minute (the symbol "*" means every)
# @periodic_task(run_every=(crontab(hour="*", minute="2", day_of_week="*")))
# def note_example():
#     logger.info("Start task")
#     result = note(1,1)
#     logger.info("Task finished: result = %i" % result)
