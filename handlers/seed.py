from tornado.web import RequestHandler
from handler import APIHandler
from tornado.web import asynchronous
from tornado import gen
from tornado import ioloop
import time
import consts
import logging
import logging.config

logging.config.fileConfig("log.conf")
logger = logging.getLogger("example01")

class IndexHandler(RequestHandler):
	def get(self):
		logger.debug('This is debug message')
		logger.warning('This is warning message')
		greeting = self.get_argument('greeting', 'Hello')
		self.write(greeting + ', friendly user!')

class StatusHandler(APIHandler):
	def get(self):
		logger.debug('This is debug message')
		status={"status": {"items": []}}
		self.finish(status)

class SleepHandler(RequestHandler):
    @asynchronous
    @gen.coroutine
    def get(self):
        yield gen.Task(ioloop.IOLoop.instance().add_timeout, time.time() + 5)
        self.write("when i sleep 5s")

handlers = [(r"/index", IndexHandler),
			(r"/status", StatusHandler),
			(r"/sleep",SleepHandler)]
