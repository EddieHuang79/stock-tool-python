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
	def stockCodeIdMapping(data):
		result = {}
		for id in data:
			result[data[id]['code']] = id
		return result
	def getDividendFormat(self, data):
		return '''	代號: %s
					名稱: %s
					除權息日期: %s
					是否有權證: %s

					多方最佳3組獲利
					%s

					空方最佳3組獲利
					%s
				''' %(data['code'], data['name'], data['dividend_date'], data['exist'], data['best'], data['worst'])