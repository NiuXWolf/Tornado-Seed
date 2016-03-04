#from handler import APIHandler
import consts
from tornado.web import RequestHandler
import logging
import logging.config

logging.config.fileConfig("log.conf")
logger = logging.getLogger("example01")

class IndexHandler(RequestHandler):
	def get(self):
		logger.debug('This is debug message')
		logger.info('This is info message')
		logger.warning('This is warning message')
		greeting = self.get_argument('greeting', 'Hello')
		self.write(greeting + ', friendly user!')


handlers = [(r"/status", IndexHandler)]
