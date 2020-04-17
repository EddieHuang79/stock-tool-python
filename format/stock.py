#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta

class stockFormat:
	one_days_ago = (date.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
	two_days_ago = (date.today() - timedelta(days = 2)).strftime('%Y-%m-%d')
	def getPercentBAndSellBuyPercentFormat(self, data, stock_data):
		if int(data[0]) in stock_data: 
			result = '''
					代號: %s
					名稱: %s
					漲跌幅: %s
					股價(%s): %s
					股價(%s): %s
					percentB: %s
					買賣壓力: %s
				''' %(data[0], data[1], data[2], self.one_days_ago, data[3], self.two_days_ago, data[4], stock_data[int(data[0])]['percentB'], stock_data[int(data[0])]['sellBuyPercent'])
		else:
			result = ''
		return result