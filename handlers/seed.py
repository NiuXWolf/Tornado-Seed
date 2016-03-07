from tornado.web import RequestHandler
from handler import APIHandler
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


handlers = [(r"/index", IndexHandler),
			(r"/status", StatusHandler)]
