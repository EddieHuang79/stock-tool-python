#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.sinyi import sinyiModel
from service.base import baseService
import sys

class sinyiService(baseService):

	def addHouseData(data):

		return sinyiModel.addHouseData(sinyiModel, data)

	def getExistObjectId():

		return sinyiModel.getExistObjectId(sinyiModel)

	def getUpdateData():

		return sinyiModel.getUpdateData(sinyiModel)

	def updateHouseData(data, id):

		return sinyiModel.updateHouseData(sinyiModel, data, id)

	def findByAddress(data):

		return sinyiModel.findByAddress(sinyiModel, data)

	def updateNotNeedHouseData(self):

		rules = [
			{
				'section': '汐止',
				'road': ['勤進', '汐碇', '汐萬', '八連', '茄安', '中興', '明峰', '康寧', '保一', '伯爵', '新台五路二', '保福一路', '樟樹', '民族五', '福德', '長興街', '汐平', '湖前', '大同路三段', '長江', '水源', '瑞松', '秀山', '東勢', '鄉長', '湖東', '建成', '保長']
			},
			{
				'section': '三重',
				'road': ['永安北', '仁美', '仁義', '三信', '集英', '仁勇', '五華', '民生']
			},
			{
				'section': '中和',
				'road': ['民德', '莒光', '員山', '民享', '民安', '金城', '建一', '建八', '自立', '國光', '忠孝']
			},
		]

		notNeedItem = []
		for item in rules:
			data = self.findByAddress(item)
			for dataItem in data:
				for road in item['road']:
					if dataItem['address'].find(road) > -1:
						notNeedItem.append(str(dataItem['id']))

		if len(notNeedItem) > 0:
			sinyiModel.updateNotNeedHouseData(sinyiModel, notNeedItem)
		
		return True

	def getSendData(limit = 5):

		return sinyiModel.getSendData(sinyiModel, limit)

	def updateSendData(id):

		return sinyiModel.updateSendData(sinyiModel, id)