#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
from pathlib import Path

import toml

BASE_DIR = Path.cwd().parent
TOML_FILE_PATH = BASE_DIR / 'result'

try:
    def config(node="", key=""):
        return toml.load(TOML_FILE_PATH)[node][key]
except OSError as e:
    # TODO LOG ERROR
    print("OS Error: {0}".format(e))
except ValueError as e:
    # TODO LOG ERROR
    print("Value Err: {0}".format(e))
except Exception as e:
    # TODO LOG ERROR
    print("Unexpected Error: {0}".format(e))
