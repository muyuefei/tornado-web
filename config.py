# -*- coding: utf-8 -*-

import os
import sys
from route import Route
__author__ = 'lipf'

route = Route()
DEBUG = True 

PREFIX = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ''
    )
)
if PREFIX not in sys.path:
    sys.path.append(PREFIX)

