#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import logging
import time
from time import ctime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:

    log_dir_path = os.path.join(BASE_DIR, "../log/")


    def log(target_name="", error_msg=""):
        if not target_name:
            return
        # 传入target_name生成日志
        # 检测log文件夹
        if not os.path.exists(log_dir_path):
            # 创建log文件夹
            os.mkdir(log_dir_path)
        # logging 逻辑

        LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S %a'

        logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT,
                            filename=r'_'.join(
                                ['l',log_dir_path, target_name, time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()),
                                 '.log']))

        return logging.error(error_msg)





except Exception as e:
    print("Unexpected Error: {0}".format(e))
