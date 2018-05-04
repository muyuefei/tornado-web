#!/usr/bin/env python
# coding=utf-8

#####################
# this is demo
#####################

__author__ = 'lipf'

from config import route
from _base import BaseHandler


@route("/demo/(\w+)/(\d*)")
class PSlot(BaseHandler):

    def initialize(self):
        self.res = dict(status=200)

    def post(self, action, slot_id):
        self.finish(self.res)

    def get(self, action, slot_id):
        self.finish(self.res)
        





