#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class stockApi:
	def getNextWorkDate(date, days = 1, type = 'add'):
		response = requests.get("http://local.stock-tool.com/api/getHoliday?days="+str(days)+"&type="+type+"&date="+date)
		return response.text