#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from stock_data import stock
from line import LineNotice
from datetime import date, timedelta
from pyquery import PyQuery as pq

# 設定日期、資料

one_days_ago = (date.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
two_days_ago = (date.today() - timedelta(days = 2)).strftime('%Y-%m-%d')

def stringFormat(data, stock_data):
	if int(data[0]) in stock_data: 
		result = '''
				代號: %s
				名稱: %s
				漲跌幅: %s
				股價(%s): %s
				股價(%s): %s
				percentB: %s
				買賣壓力: %s
			''' %(data[0], data[1], data[2], one_days_ago, data[3],two_days_ago, data[4], stock_data[int(data[0])]['percentB'], stock_data[int(data[0])]['sellBuyPercent'])
	else:
		result = ''
	return result

# 拿資料
response = requests.get("https://www.cnyes.com/twstock/ranking2.aspx?")
source = response.text
doc = pq(source)

# 取code，拿DB資料

code = []
result = []
message = '漲停 + 80塊以上\r\n'

for item in doc('.fLtBx>tbody>tr'):
	data = doc(item)('td').text().split(' ')
	if float(data[3]) >= 80 and float(data[2]) >= 9 and data[0].isdecimal():
		code.append(data[0])

if len(code) > 0:		

	stock_data = stock.find_data(stock, code, one_days_ago)

	# format
	for item in doc('.fLtBx>tbody>tr'):
		data = doc(item)('td').text().split(' ')
		if float(data[3]) >= 80 and float(data[2]) >= 9 and data[0].isdecimal():
			result.append(stringFormat(data, stock_data))

	message+= ''.join(result)

else:

	message+= '沒有符合目標\r\n'

# 送到Line
LineNotice.sendMessageToLine(LineNotice, message)

code = []
result = []
message = '漲停 + 30塊以上\r\n'

for item in doc('.fLtBx>tbody>tr'):
	data = doc(item)('td').text().split(' ')
	if float(data[3]) >= 30 and float(data[2]) >= 9 and data[0].isdecimal():
		code.append(data[0])

if len(code) > 0:		

	stock_data = stock.find_data(stock, code, one_days_ago)

	# format
	for item in doc('.fLtBx>tbody>tr'):
		data = doc(item)('td').text().split(' ')
		if float(data[3]) >= 30 and float(data[2]) >= 9 and data[0].isdecimal():
			result.append(stringFormat(data, stock_data))

	message+= ''.join(result)

else:

	message+= '沒有符合目標\r\n'

# 送到Line
LineNotice.sendMessageToLine(LineNotice, message)
