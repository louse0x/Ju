#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:desc: beian
"""
import json
import traceback
import urllib.error
from urllib import request

from module.header import header


def beian(domain):
    """
    :desc: ICP主体备案查询
    :param domain:
    :return:
    """
    try:
        req = request.Request("https://tapi.66sj.cn/api/url_icp?url={0}".format(domain),
                              headers={'User-Agent': header()})
        res = json.loads(request.urlopen(req).read().decode('utf-8'))

        return res['data']
    except TypeError:
        return 'Beian Response TypeError'
    except urllib.error.HTTPError:
        return 'Beian HTTPError'
    except Exception as e:
        traceback.print_exc()
        return {}
