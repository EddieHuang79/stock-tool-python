#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from model.base import baseModel

class warrantModel(baseModel):

	def addWarrantInfo(self, data):

		cur = self.conn.cursor()
		sql = '''
			INSERT INTO warrant (stock_id, exist, bull_type_count, bear_type_count, created_at, updated_at) VALUES ("%d", "%d", "%d", "%d", NOW(), NOW());
		''' %(data['stock_id'], data['exist'], data['bull_type_count'], data['bear_type_count'])
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 

		return True

	def getLastStockId(self):

		cur = self.conn.cursor()
		sql = '''
			SELECT stock_id FROM warrant ORDER BY stock_id DESC LIMIT 1;
		'''
		
		cur.execute(sql)
		cur.close() 

		result = 0

		for item in cur:
			result = item['stock_id']

		return result

	def getWarrantData(self, data):

		cur = self.conn.cursor()
		sql = '''
			SELECT warrant.exist, stock_info.code FROM warrant LEFT JOIN stock_info ON warrant.stock_id = stock_info.id WHERE stock_info.code IN (%s);
		''' %(','.join(data))

		cur.execute(sql)
		cur.close() 

		result = {}

		for item in cur:
			result[item['code']] = item['exist']

		return result
