#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: Web path scanner
"""

import runpy


def _dirsearch(domain):
    pass


a = runpy.run_module('dirsearch.dirsearch', run_name='__main__', alter_sys=True)

print(a)
