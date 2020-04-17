#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from service.stock import stockToolService
from api.cnyes import stockApi
from service.line import LineNotice

# 拿資料

source = stockApi.getTopLimitInfo()
doc = pq(source)
targets = doc('.fLtBx>tbody>tr')

# 漲停 + 80塊以上

rules = {'price': 80, 'percent': 9}
code = stockToolService.filterStockAndReturnCodes(doc, targets, rules)
message = stockToolService.appendStockInfoAndReturnMessages(stockToolService, doc, targets, rules, '漲停 + 80塊以上', code)
LineNotice.sendMessageToLine(LineNotice, message)

# 漲停 + 30塊以上

rules = {'price': 30, 'percent': 9}
code = stockToolService.filterStockAndReturnCodes(doc, targets, rules)
message = stockToolService.appendStockInfoAndReturnMessages(stockToolService, doc, targets, rules, '漲停 + 30塊以上', code)
LineNotice.sendMessageToLine(LineNotice, message)

