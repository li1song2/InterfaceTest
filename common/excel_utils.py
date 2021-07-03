#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : excel_utils.py
@Author: song
@Date  : 2021/6/15 22:48
'''

import openpyxl


def read_excel(file_path, sheet_name):
    work_book = openpyxl.load_workbook(file_path)
    sheet = work_book[sheet_name]
    values = list(sheet.values)
    work_book.close()
    count = len(values)
    dates = []
    for i in range(1, count):
        data = dict(zip(values[0], values[i]))
        dates.append(data)
    return dates


