#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from api.sinyi import sinyi
from service.sinyi import sinyiService
import sys
import time

# 拿資料

data = sinyiService.getUpdateData()
for dataItem in data:
	source = sinyi.getDetail(dataItem['link'])
	doc = pq(source)
	targets = doc('.buy-content-title-address')
	addressData = doc(targets).text().split(' ')
	address = addressData[-1]
	targets = doc('.buy-content-basic>.buy-content-body')
	for item in targets:
		# print(doc(item).find('.basic-title').text().split(' '))
		basicTitle = doc(item).find('.basic-title').text().split(' ')
		basicValue = doc(item).find('.basic-value').text().split(' ')
		index = 0
		for key in basicTitle:
			if key == '公共設施':
				public_area = basicValue[index]
			elif key == '管理費':
				management_fee = basicValue[index] + basicValue[index+1]
			elif key == '車位':
				park = basicValue[index]
			index += 1
		break

	targets = doc('.buy-content-obj-detail>.buy-content-body')
	for item in targets:
		# print(doc(item).find('.obj-title').text().split(' '))
		basicTitle = doc(item).find('.obj-title').text().split(' ')
		basicValue = doc(item).find('.obj-value').text().split(' ')
		index = 0
		for key in basicTitle:
			if key == '謄本用途':
				use_for = basicValue[index]
			elif key == '注意事項':
				notice = basicValue[index]
			index += 1
		break		

	updateData = {
		'public_area': public_area,
		'management_fee': management_fee,
		'park': park,
		'use_for': use_for,
		'notice': notice,
		'address': address,
	}
	sinyiService.updateHouseData(updateData, dataItem['id'])
	time.sleep(5)
