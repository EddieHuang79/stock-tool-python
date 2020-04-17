#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

payload = {'response':'csv', 'date':'20200415', 'stockNo':2330}
# response = requests.get("https://www.kkday.com/zh-tw/product/2844", params = payload)
response = requests.get("https://www.twse.com.tw/exchangeReport/STOCK_DAY?", params = payload)

source = response.text
source = source.replace('"', '')
result = source.split("\r\n")

total = len(result)
last_key = result.index(result[-6])

for item in result:
	key = result.index(item)
	if (key > 1 and key < last_key) or key == 1:
		sub = item.split(",")
		sub.pop()
		print(sub)



