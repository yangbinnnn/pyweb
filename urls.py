#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: yang 
# Created: 2017-04-21 14:22:37

import os
import time
import json
from pyweb import ctx, get, put, post, jsonapi, badrequest

@get("/welcome")
def welcome():
    return json.dumps({"msg": "hello world!", "date": time.ctime()})

@get("/sayhi/:name")
def sayhi(name):
    return json.dumps({"msg": "hi, %s!" % name, "date": time.ctime()})

@jsonapi
@get("/date")
def date():
    return {"date": time.ctime()}

@jsonapi
@get("/")
def entry():
    resp = {"headers": ctx.request.headers, "params": ctx.request.params, "query_string": ctx.request.query_string}
    resp.update({"request_method": ctx.request.request_method, "path_info": ctx.request.path_info})
    return resp

@jsonapi
@get("/add/:a/:b")
def add(a, b):
    resp = {"add": "%s + %s = %s" % (a, b, int(a) + int(b))}
    return resp

@jsonapi
@post("/login")
def login():
    name = ctx.request.params.get("name")
    password = ctx.request.params.get("password")
    if not name or not password:
        raise badrequest()
    resp = {"msg": "welcome %s!" % name}
    return resp
