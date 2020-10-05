#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from api.good_info import stockApi
from service.stock import stockToolService
from format.stock import stockFormat
from pyquery import PyQuery as pq
from service.dividend import dividendService
import sys

# lastStockId 不要-1 帶指定目標
lastStockId = dividendService.getLastStockId() if len(sys.argv) < 2 else int(sys.argv[1])
# lastStockId = dividendService.getUpdateFailStockId() if len(sys.argv) < 2 else int(sys.argv[1])
existData = dividendService.getExistData(int(lastStockId))
# lastStockId = lastStockId if len(sys.argv) < 2 else lastStockId - 1
lastStockId = lastStockId - 1
stockInfo = stockToolService.getPartStockInfo(int(lastStockId), 1)
exist = False
for index in stockInfo:
	print(stockInfo[index]['id'])
	print(stockInfo[index]['code'])
	source = stockApi.getDividend(str(stockInfo[index]['code']))
	doc = pq(source)
	targets = doc('#divDetail>table>tr')
	for item in targets:
		info = []
		for td in item:
			info.append(doc(td).text().replace(' ', ''))

		if int(info[0]) >= 2010:
			if float(info[14]) > 0 and float(info[17]) == 0:
				type = 1
			elif float(info[14]) == 0 and float(info[17]) > 0:
				type = 2
			else:
				type = 3

			if info[3] != '' and ((int(info[0]) in existData['year']) == False):
				exist = True
				insertData = {
					'stock_id': stockInfo[index]['id'],
					'dividend_date': info[0]+'/'+info[3][3:8],
					'type': type,
					'cash': info[14],
					'stock': info[17],
				}
				dividendService.addDividend(insertData)

			if info[3] != '' and existData['data'][0]['type'] == 3 and existData['data'][0]['dividend_date'].strftime('%Y-%m-%d') == '2020-01-01':
				exist = True
				updateData = {
					'dividend_date': info[0]+'/'+info[3][3:8],
					'type': type,
					'cash': info[14],
					'stock': info[17],
				}
				dividendService.updateDividend(updateData, int(existData['data'][0]['id']))

	# if exist == False:
	# 	insertData = {
	# 		'stock_id': stockInfo[index]['id'],
	# 		'dividend_date': '2020/01/01',
	# 		'type': 0,
	# 		'cash': 0,
	# 		'stock': 0,
	# 	}
	# 	dividendService.addDividend(insertData)	

	# if exist == False:
	# 	print('No Data')
	# 	dividendService.updateDividendToNoData(int(existData['data'][0]['id']))	
