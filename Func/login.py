#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : login.py
@Author: song
@Date  : 2021/6/20 22:33
'''
import random
import uuid


def login(username, password):
    if username == "zhangsan" and password == "123":
        return {"code": 200, "message": "登陆成功", "id": random.randint(1, 1000), "token": str(uuid.uuid4())}
    elif username == "" or password == "":
        return {"code": 1000, "message": "账号或者密码不允许为空！"}
    else:
        return {"code": 0, "message": "登陆失败"}



