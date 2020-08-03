#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class brokerFormat:
	def getCodeIdDicOfBroker(data):
		result = {}
		for id in data:
			result[data[id]['code']] = id
		return result
	def getCodeIdDicOfBrokerBranch(data):
		result = {}
		for id in data:
			result[data[id]['code']] = id
		return result
	def getBrokerData(data):
		result = {}
		for item in data:
			if (result.get(item['data_date']) == None):
				result[item['data_date']] = {}
			if (result[item['data_date']].get(item['stock_id']) == None):
				result[item['data_date']][item['stock_id']] = []
			result[item['data_date']][item['stock_id']].append(item)
		return result