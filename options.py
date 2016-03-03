import logging
import os

from tornado.options import parse_command_line, options, define



def parse_setting_file(path):
    config = {}
    execfile(path, config, config)
    for name in config:
        if name in options:
            options[name].set(config[name])
        else:
            define(name, config[name])


def parse_options():
    _root = os.path.dirname(os.path.abspath(__file__))
    _settings = os.path.join(_root, "settings.py")

    try:
        parse_setting_file(_settings)
        logging.info("Using settings.py as default settings.")
    except Exception, e:
        logging.error("No any default settings, are you sure? Exception: %s" % e)


    parse_command_line()
