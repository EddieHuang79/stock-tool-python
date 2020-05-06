#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class stockApi:
	def getNextWorkDate(date):
		response = requests.get("http://local.stock-tool.com/api/getHoliday?days=1&type=add&date="+date)
		return response.text