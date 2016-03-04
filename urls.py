from tornado.options import options
from tornado.web import url
import sys

handlers = []
ui_modules = {}

# the module names in handlers folder
handler_names = ["status"]

def _resolve_name(name, package, level):
    """Return the absolute name of the module to be imported."""
    if not hasattr(package, 'rindex'):
        raise ValueError("'package' not set to a string")
    dot = len(package)
    for x in xrange(level, 1, -1):
        try:
            dot = package.rindex('.', 0, dot)
        except ValueError:
            raise ValueError("attempted relative import beyond top-level "
                              "package")
    return "%s.%s" % (package[:dot], name)

def import_module(name, package=None):
    """Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != '.':
                break
            level += 1
        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]

def _generate_handler_patterns(root_module, handler_names, prefix=options.app_url_prefix):
    for name in handler_names:
        module = import_module(".%s" % name, root_module)
        module_hanlders = getattr(module, "handlers", None)
        if module_hanlders:
            _handlers = []
            for handler in module_hanlders:
                try:
                    patten = r"%s%s" % (prefix, handler[0])
                    if len(handler) == 2:
                        _handlers.append((patten,
                                          handler[1]))
                    elif len(handler) == 3:
                        _handlers.append(url(patten,
                                             handler[1],
                                             name=handler[2])
                                         )
                    else:
                        pass
                except IndexError:
                    pass

            handlers.extend(_handlers)

_generate_handler_patterns("handlers", handler_names)

# Override Tornado default ErrorHandler
#handlers.append((r".*", APIErrorHandler))
