from tornado.web import asynchronous
from handler import APIHandler
from tornado.options import options

from db import TTModel

class CreateHandler(APIHandler):
    @asynchronous
    def get(self):
        TTModel.create_table()
        self.finish()

class InsertHandler(APIHandler):
    @asynchronous
    def get(self):
        TTModel.add()
        self.finish()

handlers = [
            (r"/create", CreateHandler),
            (r"/add",InsertHandler)
            ]
