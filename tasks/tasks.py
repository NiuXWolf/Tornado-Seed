"""Celery tasks center

Setup env for celery tasks and import them.
"""

import os
import platform
import sys
from importlib import import_module
from celery import Celery

_dir = os.path.dirname(os.path.abspath(__file__))
_root = os.path.join(_dir, "..")
sys.path.append(os.path.join(_root, ".."))
sys.path.append(_dir)

def find_modules(modules_dir):
    try:
        return [f[:-3] for f in os.listdir(modules_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []

def _load_tasks():
    _current_module = sys.modules[__name__]
    for m in find_modules(os.path.dirname(__file__)):
        if m.endswith("_tasks"):  # xxx_tasks.py
            try:
                mod = import_module("." + m, package="d3status.tasks")
                for func in dir(mod):
                    if func.endswith("_task"):
                        setattr(_current_module, func, getattr(mod, func))
            except ImportError:
                pass

_load_tasks()
