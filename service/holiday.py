#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from model.holiday import holidayModel
from service.base import baseService
import datetime

class holidayService(baseService):
	def getNextWorkDate(days, type, nowDate):
		limit = days
		holidayList = holidayModel.getHoliday(holidayModel)
		date = nowDate
		while limit > 0:
			if type == 'minus':
				date = date - datetime.timedelta(1)
			else:
				date = date + datetime.timedelta(1)
			if (date in holidayList) == False and date.weekday() != 6 and date.weekday() != 5:
				limit -= 1;

		return date.strftime("%Y-%m-%d")
