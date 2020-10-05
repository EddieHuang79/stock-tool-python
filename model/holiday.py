#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from model.base import baseModel

class holidayModel(baseModel):

	def getHoliday(self):

		cur = self.conn.cursor()
		sql = '''
			SELECT holiday_date FROM holiday;
		'''
		
		cur.execute(sql.replace('\n\t\t', ' '))
		cur.close() 

		result = []

		for item in cur:
			result.append(item['holiday_date'])

		return result
