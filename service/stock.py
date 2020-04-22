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

	# 取得所有股票資料

	def getAllStockInfo():

		return stockToolModel.getAllStockInfo(stockToolModel)

	def getAllStockCategory():

		return stockToolModel.getAllStockCategory(stockToolModel)

	def getAllStockInfoByCategory(category):

		return stockToolModel.getAllStockInfoByCategory(stockToolModel, category)

	def getAllStockInfoByPrice(year, priceRule):

		return stockToolModel.getAllStockInfoByPrice(stockToolModel, year, priceRule)

	def getTopLimitData(codeId, year):

		result = {}

		total = 0
		highToLow = 0
		lowToHigh = 0
		equal = 0

		data = stockToolModel.getStockData(stockToolModel, codeId, year)
		for today in data.keys():
			yesterday = today - 1
			tomorrow = today + 1
			if yesterday in data and float(data[yesterday]['close']) > 1:
				percent = ((float(data[today]['close']) - float(data[yesterday]['close'])) / float(data[yesterday]['close'])) * 100
				# 漲停數
				if round(percent, 2) >= 9:
					total += 1
					# 漲停的隔天 開盤 > 收盤
					if tomorrow in data and float(data[tomorrow]['open']) > float(data[tomorrow]['close']):
						highToLow += 1

					elif tomorrow in data and float(data[tomorrow]['open']) < float(data[tomorrow]['close']):
						lowToHigh += 1

					else:
						equal += 1

		return {'total': total, 'highToLow': highToLow, 'lowToHigh': lowToHigh, 'equal': equal}

	def getBottomLimitData(codeId, year):

		result = {}

		total = 0
		highToLow = 0
		lowToHigh = 0
		equal = 0

		data = stockToolModel.getStockData(stockToolModel, codeId, year)
		for today in data.keys():
			yesterday = today - 1
			tomorrow = today + 1
			if yesterday in data and float(data[yesterday]['close']) > 1:
				percent = ((float(data[today]['close']) - float(data[yesterday]['close'])) / float(data[yesterday]['close'])) * 100
				# 跌停數
				if round(percent, 2) <= -9:
					total += 1
					# 跌停的隔天 開盤 > 收盤
					if tomorrow in data and float(data[tomorrow]['open']) > float(data[tomorrow]['close']):
						highToLow += 1

					elif tomorrow in data and float(data[tomorrow]['open']) < float(data[tomorrow]['close']):
						lowToHigh += 1

					else:
						equal += 1

		return {'total': total, 'highToLow': highToLow, 'lowToHigh': lowToHigh, 'equal': equal}

	# 關閉連線

	def closeConnection():

		return stockToolModel.closeConnection(stockToolModel)

