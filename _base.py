#!/usr/bin/env python
# coding=utf-8
import tornado.web
import json
import tornado.gen
import sys
import redis
from pymongo import Connection
from utils.util import StripJsOb
sys.path.insert(0, "..")


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
    
    @property
    def json(self):
        if self.request.method == 'POST':
            body = self.request.body
        elif self.request.method == 'GET':
            body = self.get_argument("query")
        return StripJsOb(**json.loads(body.decode('utf-8', 'ignore')))

    
    @tornado.gen.coroutine
    def response_as_json(self, res):
        self.set_header("Content-Encoding","gzip")
        self.set_header("Content-Type", 'text/html; charset=UTF-8')
        pass

    @tornado.gen.coroutine
    def response_error(self, error_name, status_code=0):
        """
        write error message
        :param error_name:
        :param status_code
        """
