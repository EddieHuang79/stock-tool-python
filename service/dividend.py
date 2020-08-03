#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.dividend import dividendModel
from service.base import baseService

class dividendService(baseService):

	def addDividend(data):

		return dividendModel.addDividend(dividendModel, data)

	def getLastStockId():

		return dividendModel.getLastStockId(dividendModel)

	def getRecentStock(date):

		return dividendModel.getRecentStock(dividendModel, date)

	def getExistData(stockId):

		return dividendModel.getExistData(dividendModel, stockId)