"""Celery tasks center

Setup env for celery tasks and import them.
"""

import os
import platform
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
_root = os.path.join(_dir, "..")
sys.path.append(os.path.join(_root, ".."))
sys.path.append(_dir)

from  importlib import import_module find_modules

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
