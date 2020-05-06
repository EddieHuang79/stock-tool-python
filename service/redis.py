#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis
from service.base import baseService

class redisService(baseService):

	pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379)
	redisOperator = redis.Redis(connection_pool = pool)

	def setExcuteDate(self, date):
		self.redisOperator.set('excuteDate', date)

	def getExcuteDate(self):
		return self.redisOperator.get('excuteDate').decode()

	def delExcuteDate(self):
		self.redisOperator.delete('excuteDate')

	def setExcutedBroker(self, brokerBranchId):
		self.redisOperator.rpush('excutedBroker', int(brokerBranchId))

	def getExcutedBroker(self):
		data = self.redisOperator.lrange('excutedBroker', 0, -1)
		result = []
		for item in data:
			result.append(int(item.decode()))
		return result

	def delExcutedBroker(self):
		self.redisOperator.delete('excutedBroker')