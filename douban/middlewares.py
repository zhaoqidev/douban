# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
import random

from settings import PROXIES
from settings import USER_AGENTS

"""
在settings里的配置一定要正确
"""
class RandomUserAgent(object):

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", user_agent)
        print user_agent


class RandomProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            request.neta['proxy'] = "http://" + proxy['ip_port']

        else:
            base64_userpasswd = base64.b16encode(proxy['user_passwd'])
            request.headers['Proxy-Authorization'] = 'Basic  ' + base64_userpasswd

            request.meta['proxy'] = "http://" + proxy['ip_port']
