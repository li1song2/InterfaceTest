#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : setting.py
@Author: song
@Date  : 2021/6/27 17:24
'''
import random
import faker

host = ""

phone_list = ["130", "131", "132", "133", "134", "135", "136", "137",
              "138", "139", "150", "151", "152", "153", "155", "158",
              "159"]
phone = phone_list[random.randint(0, len(phone_list))] + str(random.randint(10000000, 99999999))


def phone_number():
    fk = faker.Faker(locale="zh_CN")
    return fk.phone_number()


db = {"host": "127.0.0.1", "port": 3306, "user": "root", "password": "root"}
