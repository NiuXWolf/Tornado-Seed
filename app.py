import os
import platform
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options


from options import parse_options;

class Application(tornado.web.Application):
    def __init__(self):
        from urls import handlers, ui_modules
        #from db import Model

        settings = dict(debug=options.debug,
                        template_path=os.path.join(os.path.dirname(__file__),"templates"),
                        static_path=os.path.join(os.path.dirname(__file__),"static"),
                        login_url=options.login_url,
                        xsrf_cookies=options.xsrf_cookies,
                        cookie_secret=options.cookie_secret,
                        ui_modules=ui_modules,
                        )

        #  db connection
        # self.db = Connection(host=options.mysql["host"] + ":" +
        #                         options.mysql["port"],
        #                      database=options.mysql["database"],
        #                      user=options.mysql["user"],
        #                      password=options.mysql["password"],
        #                      )
        #
        # Model.setup_dbs({"db": self.db})

        super(Application, self).__init__(handlers, **settings)


def main():
    parse_options()
    http_server = tornado.httpserver.HTTPServer(Application(),xheaders=True)
    http_server.bind(int(options.port), "127.0.0.1")  # listen local only
    http_server.start(1)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
