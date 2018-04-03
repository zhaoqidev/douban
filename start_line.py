# coding=utf-8
""" 
@author:Administrator 
@file: start_line.py 
@time: 2018/03/{DAY} 
"""

"""
程序执行脚本
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl douban_spider".split())
