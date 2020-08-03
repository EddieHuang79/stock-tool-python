#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.warrant import warrantModel
from service.base import baseService

class warrantService(baseService):

	def addWarrantInfo(data):

		return warrantModel.addWarrantInfo(warrantModel, data)

	def getLastStockId():

		return warrantModel.getLastStockId(warrantModel)