from tornado.web import RequestHandler
from handler import APIHandler
import consts
import logging
import logging.config
from tasks import seed_task
#from mail import send_email

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

class TaskHandler(APIHandler):
	def get(self):
		s=seed_task.delay(1,2)
		#send_email('Y.Yu@thomsonreuters.com','Y.Yu', 'Copyright', '@author: Felinx Lee <felinx.lee@gmail.com>')
		status={"status": {"items": []}}
		self.write(status)

handlers = [(r"/index", IndexHandler),
			(r"/task", TaskHandler),
			(r"/status", StatusHandler)]
