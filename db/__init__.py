import os
import sys
from importlib import import_module

_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(_dir)

class Model(object):
    _dbs = {}

    @classmethod
    def setup_dbs(cls, dbs):
        cls._dbs = dbs

    @classmethod
    def dbs(self):
        return self._dbs

    # legacy support
    @classmethod
    def sqlite(self):
        return self._dbs["sqlite"]


def _find_modules(modules_dir):
    try:
        return [f[:-3] for f in os.listdir(modules_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []

def _load_model():
    _current_module = sys.modules[__name__]
    for m in _find_modules(_dir):
        if m.endswith("Model"):  # xxxModel.py
            try:
                mod = import_module("."+m,package="db")
                for func in dir(mod):
                    if func.endswith("_task"):
                        setattr(_current_module, func, getattr(mod, func))
            except ImportError:
                print "Error"
                #pass

_load_model()
