#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class hiStock:
	def getDividend():
		response = requests.get("https://histock.tw/stock/dividend.aspx?")
		return response.text
	def updateHistoryDividend(code):
		response = requests.get("https://histock.tw/stock/"+code+"/%E9%99%A4%E6%AC%8A%E9%99%A4%E6%81%AF")
		return response.text
