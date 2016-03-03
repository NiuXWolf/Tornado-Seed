from handler import APIHandler

class IndexHandler(APIHandler):
	def get(self):
		greeting = self.get_argument('greeting', 'Hello')
		self.write(greeting + ', friendly user!')


handlers = [(r"/status", IndexHandler)]
