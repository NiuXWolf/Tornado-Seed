from tornado import web
from handler import APIHandler
from tasks import add
import tcelery

tcelery.setup_nonblocking_producer()

class TaskHandler(web.RequestHandler):
    @web.asynchronous
    def get(self):
        add.apply_async(args=[3,3], callback=self.on_result)

    def on_result(self, response):
        print response.result
        self.write(str(response.result))
        self.finish()

handlers = [
            (r"/task", TaskHandler)
            ]
