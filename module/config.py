#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import toml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    toml_file_path = os.path.join(BASE_DIR, "../config.toml")


    def config(node="", key=""):
        return toml.load(toml_file_path)[node][key]

except OSError as e:
    print("OS Error: {0}".format(e))
except ValueError as e:
    print("Value Err: {0}".format(e))
except Exception as e:
    print("Unexpected Error: {0}".format(e))
