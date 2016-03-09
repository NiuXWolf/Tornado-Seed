in root path run `celery -A tasks worker -l INFO` and `celery -A tasks beat`  
`python manage.py runserver`  
`siege -c 100 -t 10 -b http://127.0.0.1:8888/dse/v1/tasks`
