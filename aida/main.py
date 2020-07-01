# ----------------------------
# -*- coding: utf-8 -*-
# @Author   : Ken Hou
# @Time     : 2020/6/28 12:34 上午
# @File     : main.py
# @Software : PyCharm
# @Project  : aida
# @User     : kan
# ----------------------------

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute (["scrapy","crawl","cnf"])
execute (["scrapy","crawl","events"])
# execute (["scrapy","crawl","ranking"])
# execute (["scrapy","crawl","aidaspider"])

