from tornado.web import RequestHandler,asynchronous
from tornado import gen
from handler import APIHandler
from tornado.options import options


#import tcelery
#tcelery.setup_nonblocking_producer()

from tasks import seed_tasks
from tasks import email_tasks

class TaskHandler(APIHandler):
    @asynchronous
    def get(self):
        response = seed_tasks.add_task.apply_async(args=[3,3])
        a=response.get(timeout=10)
        print a
        #res=seed_tasks.add_task.delay(3,8)
        #print res.get(timeout=1)
        #subject = "[%s]Internal Server Error" % options.sitename
        #body = self.render_string("errors/500_email.html",exception="exception")
        #email_tasks.send_email_task.delay(options.email_from,options.admins, subject, body)
        #seed_tasks.add_task.apply_async(args=[3,3], serializer='pickle',callback=self.on_result)
        self.finish(a)

    # def on_result(self, response):
    #     print response.result
    #     #self.write(str(response.result))
    #     self.finish()

handlers = [
            (r"/task", TaskHandler)
            ]
