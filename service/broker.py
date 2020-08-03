#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta
from format.stock import stockFormat
from model.broker import brokerModel
from service.base import baseService

class brokerService(baseService):

	def setBrokerInfo(code, name):

		return brokerModel.setBrokerInfo(brokerModel, code, name)

	def getBrokerInfo():

		return brokerModel.getBrokerInfo(brokerModel)

	def setBrokerBranch(data):

		return brokerModel.setBrokerBranch(brokerModel, data)

	def getBrokerBranch():

		return brokerModel.getBrokerBranch(brokerModel)

	def getExisingtBranchId(date):

		return brokerModel.getExisingtBranchId(brokerModel, date)

	def getExecuteCode(list, existId):
		result = {}
		for id in list:
			if ((list[id]['id'] in existId) == False):
				result = {
					'id': list[id]['id'],
					'parentCode': list[id]['parentCode'],
					'code': list[id]['code']
				}
				break
		return result

	def addBrokerData(data):

		return brokerModel.addBrokerData(brokerModel, data)

	def getBrokerData(start_date, end_date, stock_id, broker_branch_id):

		return brokerModel.getBrokerData(brokerModel, start_date, end_date, stock_id, broker_branch_id)