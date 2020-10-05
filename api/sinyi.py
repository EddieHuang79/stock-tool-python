#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class sinyi:
	# def getHouse():
	# 	data = {
	# 		'apType': 3,
	# 		'browser': 1,
	# 		'deviceType': 1,
	# 		'deviceVersion': 'Mac OS X 10.14.1',
	# 		'filter': {
	# 			'area': {
	# 				'area': '14-30',
	# 				'type': '2',
	# 			},
	# 			'exludeSameTrade': False,
	# 			'houselandtype': ['A', 'B'],
	# 			'objectStatus': 0,
	# 			'retRange': ['221', '234', '235', '241'],
	# 			'retType': 2,
	# 			'room': {
	# 				'isRoofPlus': False,
	# 				'room': '2-2',
	# 			},
	# 			'totalPrice': '800-1200',
	# 			'year': '0-30',
	# 		},
	# 		'page': 1,
	# 		'pageCnt': 20,
	# 		'sort': 0,
	# 		'model': 'web',
	# 	}
	# 	response = requests.post("https://sinyiwebapi.sinyi.com.tw/searchObject.php", data = data)
	# 	return response.text
	def getHouseNewTaipeiCity(page = '1'):
		response = requests.get("https://www.sinyi.com.tw/buy/list/200-1200-price/apartment-building-type/12-30-balconyarea/0-30-year/2-3-roomtotal/sfroofplus-sfroof-exclude/NewTaipei-city/221-234-235-241-zip/Taipei-R-mrtline/03-mrt/default-desc/"+page)
		return response.text

	def getHouseTaipeiCity(page = '1'):
		response = requests.get("https://www.sinyi.com.tw/buy/list/200-1300-price/apartment-building-type/12-30-balconyarea/0-30-year/1-3-roomtotal/sfroofplus-sfroof-exclude/Taipei-city/100-103-104-105-106-108-110-111-115-zip/Taipei-R-mrtline/03-mrt/default-desc/"+page)
		return response.text

	def getDetail(link):
		response = requests.get(link)
		return response.text