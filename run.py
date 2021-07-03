#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : run.py
@Author: song
@Date  : 2021/6/21 22:38
'''

from unittestreport import TestRunner
import unittest


suit = unittest.defaultTestLoader.discover("cases")
runner = TestRunner(suit, filename="")
runner.run()