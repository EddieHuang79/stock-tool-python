#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.dividend import dividendModel
from service.base import baseService

class dividendService(baseService):

	def addDividend(data):

		return dividendModel.addDividend(dividendModel, data)

	def updateDividend(data, id):

		return dividendModel.updateDividend(dividendModel, data, id)

	def getLastStockId():

		return dividendModel.getLastStockId(dividendModel)

	def getRecentStock(date, today):

		return dividendModel.getRecentStock(dividendModel, date, today)

	def getExistData(stockId):

		existData = dividendModel.getExistData(dividendModel, stockId)
		result = {
			'year': [],
			'data': [],
		}

		for item in existData:
			result['year'].append(item['year'])
			result['data'].append(item)

		return result

	def getExistDataByCode(code):

		existData = dividendModel.getExistDataByCode(dividendModel, code)
		result = {
			'year': [],
			'data': [],
		}

		for item in existData:
			result['year'].append(item['year'])
			result['data'].append(item)

		return result

	def getUpdateFailStockId():

		return dividendModel.getUpdateFailStockId(dividendModel)

	def updateDividendToNoData(stockId):

		return dividendModel.updateDividendToNoData(dividendModel, stockId)

	def deleteDefaultDividend(stockId):

		return dividendModel.deleteDefaultDividend(dividendModel, stockId)