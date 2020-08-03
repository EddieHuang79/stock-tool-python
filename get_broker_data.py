#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from service.broker import brokerService
from api.broker import brokerApi
from api.stock import stockApi
from service.line import LineNotice
from service.stock import stockToolService
from format.stock import stockFormat
from datetime import date, datetime
from service.redis import redisService
import time
import os

i = 0
while i < 15: 
	time.sleep(3)
	# print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))

	# 取得執行日期
	excuteDate = redisService.getExcuteDate(redisService)
	if excuteDate is None:
		excuteDate = stockApi.getNextWorkDate('2019-01-01')
		redisService.setExcuteDate(redisService, excuteDate)

	# 執行日期超過今天就退出
	if date.today() < datetime.strptime(excuteDate, "%Y-%m-%d").date():
		os._exit(0)

	# 拿DB Mapping

	stock = stockToolService.getAllStockInfo()
	stockIdMapping = stockFormat.stockCodeIdMapping(stock)
	brokerBranch = brokerService.getBrokerBranch()
	canExcute = False

	# 判斷該日期是否可以執行
	while canExcute == False:
		# exisingtBranchId = brokerService.getExisingtBranchId(excuteDate)
		exisingtBranchId = redisService.getExcutedBroker(redisService)
		executeBranchCode = brokerService.getExecuteCode(brokerBranch, exisingtBranchId)
		if executeBranchCode == {}:
			excuteDate = stockApi.getNextWorkDate(excuteDate)
			redisService.delExcutedBroker(redisService)
			redisService.setExcuteDate(redisService, excuteDate)
		else:
			canExcute = True
			print(executeBranchCode)
			redisService.setExcutedBroker(redisService, executeBranchCode['id'])

	# 拿資料

	source = brokerApi.getBrokerData(executeBranchCode['parentCode'], executeBranchCode['code'], excuteDate, excuteDate)
	doc = pq(source)
	targets = doc('.t0>tr')
	for item in targets:
		data = doc(item)('td').text()
		data = data.replace("<!-- GenLink2stk('AS", '')
		data = data.replace("'); //-->", '')
		data = data.replace("','", ' ')
		opt = data.split(' ');
		if(len(opt) >= 5 and opt[0].isnumeric() and (int(opt[0]) in stockIdMapping) == True):
			insertData = {
				'stock_id': stockIdMapping[int(opt[0])],
				'broker_branch_id': executeBranchCode['id'],
				'data_date': excuteDate,
				'is_total': 1 if executeBranchCode['parentCode'] == executeBranchCode['code'] else 0,
				'buy_number': int(opt[2].replace(',', '')),
				'sell_number': int(opt[3].replace(',', ''))
			}
			brokerService.addBrokerData(insertData)

	# print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
	i+=1

