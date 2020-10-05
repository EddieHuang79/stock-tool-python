#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from api.hi_stock import hiStock
from service.stock import stockToolService
from format.stock import stockFormat
from pyquery import PyQuery as pq
from service.dividend import dividendService
import time

limit = 3

# lastStockId 不要-1 帶指定目標
# lastStockId = dividendService.getLastStockId() if len(sys.argv) < 2 else int(sys.argv[1])
# existData = dividendService.getExistData(int(lastStockId))
# lastStockId = lastStockId - 1
# stockInfo = stockToolService.getPartStockInfo(int(lastStockId), 1)
# 取得更新失敗的stockId
start = 1
lastStockId = dividendService.getUpdateFailStockId()
stockInfo = stockToolService.getPartStockInfo(int(lastStockId) - 1, limit) # 會回傳後一筆，查當下的話要-1
for index in stockInfo:
	print('stock id')
	print(stockInfo[index]['id'])
	print('code')
	print(stockInfo[index]['code'])
	hasData = False
	source = hiStock.updateHistoryDividend(str(stockInfo[index]['code']))
	doc = pq(source)
	targets = doc('.row-stock table>tr') 
	for item in targets:
		info = []
		for td in item:
			info.append(doc(td).text().replace(' ', ''))
		if len(info) > 0 and info[1].isnumeric() and int(info[1]) >= 2016:
			if info[2] != '':
				insertData = {
					'stock_id': stockInfo[index]['id'],
					'dividend_date': info[1] + '/' + info[2],
					'type': 2,
					'cash': 0,
					'stock': info[5],
				}
				dividendService.addDividend(insertData)
				hasData = True
			if info[3] != '':
				insertData = {
					'stock_id': stockInfo[index]['id'],
					'dividend_date': info[1] + '/' + info[3],
					'type': 1,
					'cash': info[6],
					'stock': 0,
				}
				dividendService.addDividend(insertData)
				hasData = True
			if hasData == True:
				dividendService.deleteDefaultDividend(int(stockInfo[index]['id']))
	if hasData == False:
		dividendService.updateDividendToNoData(int(stockInfo[index]['id']))
	if start < limit:
		time.sleep(10)
		start += 1