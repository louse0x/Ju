#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: waf识别
"""

import subprocess

def waf(domain):
    """
    :desc: https://github.com/EnableSecurity/wafw00f/
    :param domain:
    :return:
    """
    try:
        data = dict()
        ret, val = subprocess.getstatusoutput("python")

        return data


    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1

















waf('https://su.baidu.com/')
