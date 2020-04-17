#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta
from format.stock import stockFormat
from model.stock import stockToolModel

class stockToolService:

	# 設定日期、資料

	one_days_ago = (date.today() - timedelta(days = 1)).strftime('%Y-%m-%d')

	# 找目標code
	# [0] => 代號, [1] => 名稱, [2] => 漲幅, [3] => 股價

	def filterStockAndReturnCodes(doc, targets, rules):
		code = []
		for item in targets:
			data = doc(item)('td').text().split(' ')
			if float(data[3]) >= rules['price'] and float(data[2]) >= rules['percent'] and data[0].isdecimal():
				code.append(data[0])
		return code

	# 用code，拿DB資料

	def appendStockInfoAndReturnMessages(self, doc, targets, rules, title, code):
		result = []
		message = []
		message.append(title)

		limit = 5;
		index = 1;

		if len(code) > 0:
			message.append('')
			stock_data = stockToolModel.getPercentBAndSellBuyPercent(stockToolModel, code, self.one_days_ago)
			for item in targets:
				data = doc(item)('td').text().split(' ')
				if float(data[3]) >= rules['price'] and float(data[2]) >= rules['percent'] and data[0].isdecimal():
					if index > limit:
						index = 1
						result = []
						message.append('')

					result.append(stockFormat.getPercentBAndSellBuyPercentFormat(stockFormat, data, stock_data))
					index += 1
					message[len(message)-1] = ''.join(result)

		else:
			message.append('沒有符合目標')

		return message
