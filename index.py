# -*- coding: utf-8 -*-
import os
import sys
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.autoreload
from config import route, DEBUG
from tornado.options import define, options
import urls

__author__ = 'lipf'

reload(sys)  # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

class Application(tornado.web.Application):
    def __init__(self, handlers=None, default_host="", transforms=None,
                 **settings):
        tornado.web.Application.__init__(self, handlers, default_host,
                                         transforms, **settings)

app = Application(
    handlers=route.handlers,
)
define("port", default=9999, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    if DEBUG:
        tornado.autoreload.start()
    for dir, _, files in os.walk('./'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files
         if not f.startswith('.')]
    tornado.ioloop.IOLoop.instance().start()
