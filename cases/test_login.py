#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_login.py
@Author: song
@Date  : 2021/6/20 19:30
'''
import unittest
from common.excel_utils import read_excel
from Func.login import login
from unittestreport import ddt, list_data
from common.logger import log
import os
from common.db import my_DB

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "date", "testlogin.xlsx")
cases = read_excel(case_path, 'login')


@ddt
class Test_Login(unittest.TestCase):

    def setUp(self) -> None:
        with my_DB() as my_db:
            self.my_db = my_db

    @list_data(cases)
    def test_login(self, case_date):
        date = eval(case_date['date'])
        expect = eval(case_date['expect'])
        username = date['username']
        password = date['password']
        log.info(f"账号为：{username},密码为：{password}")

        result = login(username, password)
        log.info(f"运行结果为：{result}")
        log.info(f"实际结果为：{expect}")
        try:
            self.assertEqual(expect, result)
            log.info("测试用例执行通过")
        except AssertionError as e:
            log.error("测试用例执行失败")
            raise e
