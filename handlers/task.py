from tornado.web import asynchronous
from handler import APIHandler
from tornado.options import options
from tornado import gen

from tasks import seed_tasks
from tasks import email_tasks

class TaskHandler(APIHandler):
    @asynchronous
    def get(self):
        #seed_tasks.add_task.apply_async(args=[100,0], callback=self.on_success)
        # task=seed_tasks.long_task.delay()
        # res=response.get(timeout=10)
        # response = seed_tasks.add_task.apply_async(args=[3,3])
        # res=response.get(timeout=10)
        response = seed_tasks.add_task.delay(3,8)
        res=response.get(timeout=10)
        print res
        self.finish({"sc":res})

    def on_success(self, response):
        users = response.result
        self.write(users)
        self.finish()

class LongCallHandler(APIHandler):
    @asynchronous
    #@gen.coroutine
    def get(self):
        seed_tasks.add_task.apply_async(args=[3,6], callback=self.on_result)
        #response = yield gen.Task(seed_tasks.add_task.delay,(8,8))
        #self.write(response.result)
        #self.finish()

    def on_result(self, response):
        self.write(str(response.result))
        self.finish()

class LongTHandler(APIHandler):
    @asynchronous
    def get(self):
        task=seed_tasks.long_task.delay()
        self.finish({'RE':"OK",'TID':task.id})

class LongSHandler(APIHandler):
    @asynchronous
    def get(self,task_id):
        task = seed_tasks.long_task.AsyncResult(task_id)
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        self.finish(response)

handlers = [
            (r"/task", TaskHandler),
            (r"/tasklong",LongTHandler),
            (r"/taskstatus/(.*)",LongSHandler),
            (r"/longcall",LongCallHandler)
            ]
