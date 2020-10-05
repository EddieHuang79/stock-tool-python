#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from api.hi_stock import hiStock
from api.stock import stockApi
from pyquery import PyQuery as pq
from datetime import *
from service.warrant import warrantService
from format.stock import stockFormat
from service.line import LineNotice
from service.strategy import strategyService
import sys

today = datetime.today().strftime("%Y-%m-%d")
excuteDate = stockApi.getNextWorkDate(today, 5)
source = hiStock.getDividend()
doc = pq(source)
targets = doc('#CPHB1_gv>tr')
codeList = []
result = []
for item in targets:
	if doc(item).attr('align') == None:
		i = 0
		match = False
		info = []
		for td in item:
			if i == 0:
				dateFromData = datetime.strptime(doc(td).text(), '%Y/%m/%d')
				dateCompare = datetime.strptime(excuteDate, '%Y-%m-%d')
				if datetime.today() < dateFromData and dateFromData < dateCompare:
					match = True
			if match == True:
				info.append(doc(td).text());
			i += 1
		if match == True and info[1].isnumeric():
			result.append(info)
			codeList.append(info[1])
# 拿權證資料

warrentData = warrantService.getWarrantData(codeList)

# mapping data
data = []
for item in result:
	if int(item[1]) in warrentData:
		isExist = '是' if warrentData[int(item[1])] == 1 else '否'
		if warrentData[int(item[1])] == 1:
			data.append({'code': item[1],'name': item[2],'dividend_date': item[0], 'exist': isExist})
	else:
		isExist = '不知道'

# 加入歷年分析
data = strategyService.getStockPriceDiffAtDividendRange(data)

message = ['最近除權息']
for item in data:
	message.append(stockFormat.getDividendFormat(stockFormat, item).replace('\n\t\t\t\t', '\n'))

LineNotice.sendMessageToLineForMutilpe(LineNotice, message)
