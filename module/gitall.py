#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: git / svn /  ...
"""
import subprocess
from sys import executable

import dumpall
from cffi.setuptools_ext import execfile

#print(dumpall.__path__)


def gitall(domain):
    """
    :desc: https://pypi.org/project/dumpall/
    :param domain:
    :return:
    """
    exec("dumpall -h")
    # proc = subprocess.Popen("{0} {1}/dumper.py -u {2}/.git".format(executable, dumpall.__path__[0], domain), shell=False)
    #
    # try:
    #     outs, errs = proc.communicate(timeout=30)
    #     return outs, errs
    # except subprocess.TimeoutExpired:
    #     proc.kill()
    #     outs, errs = proc.communicate()
    #     return -1


    # proc = subprocess.run(["dumpall", '-u', "{0}/.git".format(domain)],
    #                       check=True, stdout=subprocess.PIPE,shell=True)
    # print(proc.stdout)


print(gitall('http://testphp.vulnweb.com/'))
