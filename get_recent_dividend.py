#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from api.stock import stockApi
from service.dividend import dividendService
from format.stock import stockFormat
from service.line import LineNotice
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

# 拿資料
excuteDate = stockApi.getNextWorkDate(today, 10)
data = dividendService.getRecentStock(excuteDate)
message = ['最近除權息']
for item in data:
	message.append(stockFormat.getDividendFormat(stockFormat, data[item]).replace('\n\t\t\t\t', '\n'))

LineNotice.sendMessageToLineForMutilpe(LineNotice, message)
