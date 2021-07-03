#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : logger.py
@Author: song
@Date  : 2021/6/21 22:05
'''
import logging
import os

path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(path, "log", "logs.log")


def get_logger(name="root", file=file_path):
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel("DEBUG")
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(file, encoding="utf-8")
    file_handler.setLevel("DEBUG")
    logger.addHandler(file_handler)

    fmt = logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s")
    stream_handler.setFormatter(fmt)
    file_handler.setFormatter(fmt)

    return logger


log = get_logger()
