#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yang 
# Created: 2017-04-21 14:28:15

import os
import urls
from pyweb import WSGIApplication

import logging
from logging.handlers import RotatingFileHandler
log_format = "%(asctime)s %(levelname)-8s %(module)s %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)
r_handler = RotatingFileHandler(filename="myapp.log", maxBytes=1024 * 1024 * 2, backupCount=2)
r_handler.setLevel(logging.DEBUG)
r_handler.setFormatter(logging.Formatter(log_format))
logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(r_handler)

app = WSGIApplication()
app.add_module(urls)
app.run()