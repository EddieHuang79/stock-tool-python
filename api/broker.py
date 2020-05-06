#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class brokerApi:
	def getBrokerData(parentCode, code, start, end):
		response = requests.get("http://5850web.moneydj.com/z/zg/zgb/zgb0.djhtm?a="+parentCode+"&b="+code+"&c=E&e="+start+"&f="+end)
		return response.text