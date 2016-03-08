from tornado import web
from handler import APIHandler
from tasks import seed_tasks

class TaskHandler(web.RequestHandler):
    #@web.asynchronous
    def get(self):
        seed_tasks.add_task.delay(3,8)
        #seed_tasks.add_task.apply_async(args=[3,3], callback=self.on_result)

    # def on_result(self, response):
    #     print response.result
    #     self.write(str(response.result))
    #     self.finish()

handlers = [
            (r"/task", TaskHandler)
            ]
