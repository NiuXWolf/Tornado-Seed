BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
# CELERY_ACCEPT_CONTENT=['pickle']
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'add-every-monday-morning': {
        'task': 'tasks.seed_tasks.add_task',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
    'add-every-60-seconds': {
            'task': 'tasks.seed_tasks.add_task',
            'schedule':crontab(hour='*', minute='*', day_of_week='*'),
            'args': (16, 1)
        },
}
