#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta
from format.stock import stockFormat
from model.base import baseModel

class baseService(baseModel):

	def closeConnection(self):

		return baseModel.closeConnection(self)

