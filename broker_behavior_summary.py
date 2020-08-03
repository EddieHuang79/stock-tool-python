#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from service.broker import brokerService
from format.broker import brokerFormat
import os.path
import sys
from os import path

data = {
	'201901': 20,
	'201902': 13,
	'201903': 20,
	'201904': 20,
	'201905': 22,
	'201906': 19,
	'201907': 23,
	'201908': 21,
	'201909': 19,
	'201910': 21,
}

result = {}
mapBroker = {}

for item in data:
	fileName = '''brokerBehavior/brokerBehaviorOneDay-%s.txt'''  %(item)
	total = data[item]

	f = open(fileName, 'r')
	file = f.read()
	fileInfo = file.split('\n')
	for item2 in fileInfo:
		infoData = item2.split(',')
		if infoData[0] != '':
			if result.get(infoData[0]) == None:
				result[infoData[0]] = 0
			mapBroker[infoData[0]] = infoData[1]
			result[infoData[0]] = int(infoData[2]) + int(infoData[3])
	
	f.close()

i = 0
sort = sorted(result.items(), key=lambda d: d[1], reverse=True)
for item in sort:
	print(mapBroker[item[0]] + ': ' + str(item[1]))
	i += 1
	if i > 9:
		break
