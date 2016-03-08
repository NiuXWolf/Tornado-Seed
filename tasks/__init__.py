import os
import sys
from importlib import import_module
from celery import Celery

#from .seed_tasks import add_task

_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(_dir)

app = Celery('tasks')
app.config_from_object('tasks.celeryconfig')


def _find_modules(modules_dir):
    try:
        return [f[:-3] for f in os.listdir(modules_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []

def _load_tasks():
    _current_module = sys.modules[__name__]
    for m in _find_modules(_dir):
        if m.endswith("_tasks"):  # xxx_tasks.py
            try:
                mod = import_module("."+m,package="tasks")
                for func in dir(mod):
                    if func.endswith("_task"):
                        setattr(_current_module, func, getattr(mod, func))
            except ImportError:
                print "Error"
                #pass

_load_tasks()
