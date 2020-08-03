#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from service.broker import brokerService
from format.broker import brokerFormat
import os.path
import sys
from os import path

fileName = 'brokerBehavior/brokerBehaviorOneDay-201910.txt'
fileOpMode = 'a' if path.exists(fileName) else 'x'
f = open(fileName, fileOpMode)

# 當沖計算
start_date = '2019-10-01'
end_date = '2019-10-31'
brokerData = brokerService.getBrokerData(start_date, end_date, '', '')
brokerDataFormat = brokerFormat.getBrokerData(brokerData)

result = {}
for data_date in brokerDataFormat:
	for stock_id in brokerDataFormat[data_date]:
		for item in brokerDataFormat[data_date][stock_id]:
			if result.get(item['branch_code']) == None:
				result[item['branch_code']] = {
					# 'date': data_date,
					'branch_code': item['branch_code'],
					'branch_name': item['branch_name'],
					'absolute_count': 0,
					'relative_count': 0,
					'absolute_sum': 0,
					'relative_sum': 0
				}
			if item['buy_number'] > 0 and item['buy_number'] == item['sell_number']:
				result[item['branch_code']]['absolute_count'] += 1
				result[item['branch_code']]['absolute_sum'] += item['buy_number']
			if item['buy_number'] > 0 and item['sell_number'] > 0 and item['buy_number'] != item['sell_number']:
				result[item['branch_code']]['relative_count'] += 1
				result[item['branch_code']]['relative_sum'] += item['sell_number'] if item['buy_number'] > item['sell_number'] else item['buy_number']

# 券商code, 券商name, 完全當沖次數, 部分當沖次數, 完全當沖張數, 部分當沖張數
# code, name, 1, 0, 100, 0 
# code, name, 0, 1, 0, 15

text = ''
for item in result:
	data = result[item]
	# text+= data['date'] + ',' + data['branch_code'] + ',' + data['branch_name'] + ',' + str(data['absolute_count']) + ',' + str(data['relative_count']) + ',' + str(data['absolute_sum']) + ',' + str(data['relative_sum']) + '\n';
	text+= data['branch_code'] + ',' + data['branch_name'] + ',' + str(data['absolute_count']) + ',' + str(data['relative_count']) + ',' + str(data['absolute_sum']) + ',' + str(data['relative_sum']) + '\n';

f.write(text)
f.close()
