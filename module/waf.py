#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: waf identify
"""

import re
import subprocess
import traceback
from sys import executable

import wafw00f


def waf(domain):
    """
    :desc: https://github.com/EnableSecurity/wafw00f/
    :param domain:
    :return:
    """
    try:
        res, val = subprocess.getstatusoutput(
            "{0} {1}/main.py {2} --findall".format(executable, wafw00f.__path__[0], domain))
        if res == 0:
            # 执行正常
            pattern = "The site (.*) is behind (.*)"
            result = re.search(pattern, val)
            if result:
                return result.groups()[1]
            else:
                # 无waf
                return {}
        else:
            return "Waf HttpError"
    except Exception as e:
        traceback.print_exc()
        return {}
