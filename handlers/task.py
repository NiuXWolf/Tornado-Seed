from tornado.web import RequestHandler
from handler import APIHandler
from tornado.options import options

from tasks import seed_tasks
from tasks import email_tasks

class TaskHandler(RequestHandler):
    #@asynchronous
    def get(self):
        seed_tasks.add_task.delay(3,8)
        subject = "[%s]Internal Server Error" % options.sitename
        body = self.render_string("errors/500_email.html",exception="exception")
        email_tasks.send_email_task.delay(options.email_from,options.admins, subject, body)
        #seed_tasks.add_task.apply_async(args=[3,3],callback=self.on_result)
        self.finish()

    def on_result(self, response):
        print response.result
        self.write(str(response.result))
        self.finish()

handlers = [
            (r"/task", TaskHandler)
            ]
