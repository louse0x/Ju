#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: config
"""
from pathlib import Path

import toml

BASE_DIR = Path.cwd().parent
TOML_FILE_PATH = BASE_DIR / 'config.toml'
try:
    def config(node="", key=""):
        if node is not None and key is not None:
            return toml.load(TOML_FILE_PATH)[node][key]
        else:
            return None
except OSError as e:
    # TODO:: LOG ERROR
    print("OS Error: {0}".format(e))
except ValueError as e:
    # TODO:: LOG ERROR
    print("Value Err: {0}".format(e))
except Exception as e:
    # TODO:: LOG ERROR
    print("Unexpected Error: {0}".format(e))
