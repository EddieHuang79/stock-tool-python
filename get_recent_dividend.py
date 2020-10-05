#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from api.stock import stockApi
from service.dividend import dividendService
from format.stock import stockFormat
from service.line import LineNotice
from datetime import datetime
from service.stock import stockToolService
from service.strategy import strategyService

today = datetime.today().strftime("%Y-%m-%d")
today = '2020-09-01'

# 拿資料
excuteDate = stockApi.getNextWorkDate(today, 3)
# {0: {'code': 1590, 'name': '亞德客-KY', 'dividend_date': datetime.date(2020, 9, 3), 'exist': '是'}, ...}
data = dividendService.getRecentStock(excuteDate, today)

# 最佳進出點
# 1. 前X天 + 開/收進 <=> 前X天 + 開/收出: 平均價差, 歷年價差: 2015 - xxx, 2016 - xxx ...
# 2. ..
# 3. ..
# {0: {'code': 1590, 'name': '亞德客-KY', 'dividend_date': datetime.date(2020, 9, 3), 'exist': '是', 'best': '', 'worst': ''}, ...}
data = strategyService.getStockPriceDiffAtDividendRange(data)

print(data)
sys.exit(0)
		
message = ['最近除權息']
for item in data:
	message.append(stockFormat.getDividendFormat(stockFormat, data[item]).replace('\n\t\t\t\t', '\n'))

# LineNotice.sendMessageToLineForMutilpe(LineNotice, message)
