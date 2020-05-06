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