from tornado.options import options
from tornado.web import url
import sys
from  importlib import import_module

handlers = []
ui_modules = {}

# the module names in handlers folder
handler_names = ["seed","task","data"]

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
