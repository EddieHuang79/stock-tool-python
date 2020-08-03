#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class stockApi:
	def getWarrant(stockId, market):
		data = {
			'encodeURIComponent': 1,
			'step': 1,
			'ver': 1.9,
			'TYPEK': '',
			'market': market,
			'wrn_class': 'all',
			'stock_no': stockId,
			'wrn_no': '',
			'co_id': 'all',
			'wrn_type': 'all',
			'left_month': 'all',
			'return_rate': 'all',
			'price_down': '',
			'price_up': '',
			'price_inout': 'all',
			'newprice_down': '',
			'newprice_up': '',
			'fin_down': '',
			'fin_up': '',
			'sort': 1
		}
		response = requests.post("https://mops.twse.com.tw/mops/web/t90sbfa01", data = data)
		return response.text