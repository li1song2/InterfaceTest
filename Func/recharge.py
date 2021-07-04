#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : recharge.py
@Author: song
@Date  : 2021/7/4 22:29
'''


def recharge(user_id, token, money):
    try:
        if user_id > 0 and user_id is not None and token is not None and money > 0 and money is not None:
            print({"code": 0, "message": "充值成功"})
        elif user_id is not None or token is not None or money is not None:
            print({"code": 1, "message": "请正确输入参数"})
    except Exception as e:
        print("参数有误")
