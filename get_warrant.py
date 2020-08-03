#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from api.twse import stockApi
from service.stock import stockToolService
from format.stock import stockFormat
from pyquery import PyQuery as pq
from service.warrant import warrantService

lastStockId = warrantService.getLastStockId()
stockInfo = stockToolService.getPartStockInfo(lastStockId, 1)
for index in stockInfo:
	print(stockInfo[index]['code'])
	source = stockApi.getWarrant(stockInfo[index]['code'], stockInfo[index]['type'])
	doc = pq(source)
	targets = doc('table.hasBorder>tr')
	i = 0
	exist = False
	bull_type_count = 0
	bear_type_count = 0
	for item in targets:
		if i > 7:
			exist = True
			data = doc(item)('td').text()
			opt = data.split(' ');
			bull_type_count += 1 if opt[3] == '認購' else 0 
			bear_type_count += 1 if opt[3] == '認售' else 0
		i += 1
	insertData = {
		'stock_id': stockInfo[index]['id'],
		'exist': exist,
		'bull_type_count': bull_type_count,
		'bear_type_count': bear_type_count,
	}
	warrantService.addWarrantInfo(insertData)
