#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : db.py
@Author: song
@Date  : 2021/6/30 22:10
'''
import pymysql
from pymysql.cursors import DictCursor
from config.setting import db


class my_DB():
    def __init__(self):
        self.conn = pymysql.connect(**db)

    def fetchone(self, sql):
        cursor = self.conn.cursor(DictCursor)
        cursor.execute(sql)
        res = cursor.fetchone()
        cursor.close()
        # self.close()
        return res

    def fetchall(self, sql):
        cursor = self.conn.cursor(DictCursor)
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        # self.close()
        return res

    def fetch(self, sql, one=True):
        if one:
            return self.fetchone(sql)
        else:
            return self.fetchall(sql)

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()


# db1 = my_DB()
# date = db1.fetch("select * from bookmanger.app01_book", one=False)
# print(date)
with my_DB() as db1:
    res = db1.fetch("select * from bookmanger.app01_book")
    print(res)