#from handler import APIHandler
import consts
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
	def get(self):
		greeting = self.get_argument('greeting', 'Hello')
		self.write(greeting + ', friendly user!')


handlers = [(r"/status", IndexHandler)]
