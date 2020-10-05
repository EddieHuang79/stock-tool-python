#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from api.sinyi import sinyi
from service.sinyi import sinyiService
import sys
import time

# 拿資料

existData = sinyiService.getExistObjectId()
domain = 'https://www.sinyi.com.tw'
source = sinyi.getHouseTaipeiCity()
doc = pq(source)
pageNation = doc('.pagination>li.pageClassName')
for pageItem in pageNation:
	page = int(doc(pageItem).text())

times = 1
while times <= page:
	source = sinyi.getHouseTaipeiCity(str(times))
	doc = pq(source)

	targets = doc('.buy-list-frame>.buy-list-item')
	result = []
	for item in targets:
		houseItem = {}
		doc(item).find('.recommend-item').parents('a').remove()
		houseItem['link'] = domain + doc(item).find('a').attr('href')
		linkData = doc(item).find('a').attr('href').split('/')
		houseItem['object_id'] = linkData[3]

		if (houseItem['object_id'] in existData) == False:

			houseItem['name'] = doc(item).find('.LongInfoCard_Type_Name').text().replace('\n', ' ')

			i = 0
			for subItem in doc(item).find('.LongInfoCard_Type_Address>span'):
				if i == 0:
					houseItem['address'] = doc(subItem).text()
				elif i == 1:
					houseItem['age'] = doc(subItem).text()
				elif i == 2:
					houseItem['house_type'] = doc(subItem).text()
				i+=1

			i = 0
			for subItem in doc(item).find('.LongInfoCard_Type_HouseInfo>span'):
				if i == 0:
					houseItem['total_area'] = doc(subItem).text()
				elif i == 1:
					houseItem['use_area'] = doc(subItem).text()
				elif i == 2:
					houseItem['spec'] = doc(subItem).text()
				elif i == 3:
					houseItem['floor'] = doc(subItem).text()
				i+=1

			i = 0
			for subItem in doc(item).find('.LongInfoCard_Type_SpecificTags>span'):
				if i == 0:
					houseItem['has_dereactors'] = doc(subItem).text()
				elif i == 1:
					houseItem['window_in_toilet'] = doc(subItem).text()
				elif i == 2:
					houseItem['window_in_all_room'] = doc(subItem).text()
				i+=1

			sinyiService.addHouseData(houseItem)

	time.sleep(5)
	times += 1
