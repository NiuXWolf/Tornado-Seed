
CELERY_IMPORTS = ("seed_task")

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 9

BROKER_URL = "redis://%s:%s/%s" % (CELERY_REDIS_HOST, CELERY_REDIS_PORT,
                                   CELERY_REDIS_DB)
