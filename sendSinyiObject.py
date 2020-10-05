#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from api.sinyi import sinyi
from service.sinyi import sinyiService
from format.house import houseFormat
import sys
import time
from service.line import LineNotice

# 拿資料

sinyiService.updateNotNeedHouseData(sinyiService)

updateId = []
message = ['房屋物件']

data = sinyiService.getSendData()
for dataItem in data:
	updateId.append(str(dataItem['id']))
	message.append(houseFormat.getHouseFormat(houseFormat, dataItem).replace('\n\t\t\t\t', '\n'))

LineNotice.sendMessageToLineForMutilpeHouse(LineNotice, message)
sinyiService.updateSendData(updateId)
