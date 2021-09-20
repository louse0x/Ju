#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: waf identify
"""

import re
import subprocess

import wafw00f


def waf(domain):
    """
    :desc: https://github.com/EnableSecurity/wafw00f/
    :param domain:
    :return:
    """
    try:
        res, val = subprocess.getstatusoutput(
            "python {0}/main.py {1} --findall".format(wafw00f.__path__[0], domain))
        if res == 0:
            # 执行正常
            pattern = "The site (.*) is behind (.*)"
            result = re.search(pattern, val)
            if result:
                return result.groups()[1]
            else:
                # 无waf
                return "no waf"
        else:
            return None
    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1



