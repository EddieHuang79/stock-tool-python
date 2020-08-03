#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class stockApi:
	def getDividend(code):
		response = requests.get("https://goodinfo.tw/StockInfo/StockDividendSchedule.asp?STOCK_ID="+code, headers={'User-Agent':'test'})
		return response.text