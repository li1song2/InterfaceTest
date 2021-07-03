#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : login.py
@Author: song
@Date  : 2021/6/20 22:33
'''

def login(username, password):
    if username == "zhangsan" and password == "123":
        return {"code": 200, "message": "登陆成功"}
    elif username == "" or password == "":
        return {"code": 1000, "message": "账号或者密码不允许为空！"}
    else:
        return {"code": 0, "message": "登陆失败"}