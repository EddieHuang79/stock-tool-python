#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from model.base import baseModel

class dividendModel(baseModel):

	def addDividend(self, data):

		cur = self.conn.cursor()
		sql = '''
			INSERT INTO dividend (stock_id, dividend_date, type, cash, stock, created_at, updated_at) VALUES ("%d", "%s", "%d", "%s", "%s", NOW(), NOW());
		''' %(data['stock_id'], data['dividend_date'], data['type'], data['cash'], data['stock'])
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 

		return True

	def getLastStockId(self):

		cur = self.conn.cursor()
		sql = '''
			SELECT stock_id FROM dividend ORDER BY stock_id DESC LIMIT 1;
		'''
		
		cur.execute(sql.replace('\n\t\t', ' '))
		cur.close() 

		result = 0

		for item in cur:
			result = item['stock_id']

		return result

	def getExistData(self, stockId):

		cur = self.conn.cursor()
		sql = '''
			SELECT id, stock_id, YEAR(dividend_date) as year FROM dividend WHERE stock_id = %d ORDER BY dividend_date DESC;
		''' %(stockId)
		
		cur.execute(sql.replace('\n\t\t', ' '))
		cur.close() 

		info = []

		for item in cur:
			info.append(item['year'])

		return info

	def getRecentStock(self, date):

		cur = self.conn.cursor()
		sql = '''
			SELECT 
				stock_info.code,
				stock_info.name,
				dividend.dividend_date,
				CASE WHEN warrant.exist = 1 THEN '是'
					 ELSE '否' 
				END 'exist'
			FROM dividend
			LEFT JOIN stock_info ON dividend.stock_id = stock_info.id
			LEFT JOIN warrant ON dividend.stock_id = warrant.stock_id
			WHERE dividend.dividend_date > NOW() AND dividend.dividend_date <= '%s';
		''' %(date)

		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		i = 0
		for item in cur:
			info[i] = item
			i += 1

		cur.close() 
		return info
