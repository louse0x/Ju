#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: Web path scanner
"""

import subprocess
from sys import executable

import dirsearch

from header import header


def _dirsearch(domain):
    """
    :desc: https://github.com/maurosoria/dirsearch
    :param domain
    :return:
    """
    try:
        res, val = subprocess.getstatusoutput(
            "{0} {1}/dirsearch.py -u {2} --recursion-depth 3 --recursion-status 200-399 --exclude-texts='Not found','Error' --no-color --user-agent={3} --retries=1 --format=json --quiet-mode -e php,htm,js,bak,zip,tgz,txt -t 20 --max-rate 100".format(
                executable, dirsearch.__path__[0], domain, header()))

        if res == 0:
            # 执行正常
            print(val)


        else:
            # TODO:: LOG ERROR
            return "dirsearch Error"



    except Exception as e:
        # TODO:: LOG ERROR
        print(e)
        return -1


print(_dirsearch('www.tjhzyl.com'))
