#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from datetime import date, timedelta, datetime
from model.base import baseModel

class stock(baseModel):

	def getPercentBAndSellBuyPercent(self, stock_id_array, date):

		stock_id_array = ','.join(stock_id_array)

		cur = self.conn.cursor() 
		sql = '''
			SELECT 
				stock_info.code,
				technical_analysis.percentB,
				sell_buy_percent.result
			FROM stock_info
			LEFT JOIN technical_analysis ON stock_info.id = technical_analysis.stock_id
			LEFT JOIN sell_buy_percent ON stock_info.id = sell_buy_percent.stock_id
			WHERE stock_info.code IN (%s)
			AND technical_analysis.data_date = '%s'
			AND sell_buy_percent.data_date = '%s';
		''' %(stock_id_array, date, date)
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['code']] = {
				'percentB': item['percentB'],
				'sellBuyPercent': item['result'],
			}

		cur.close() 
		self.conn.close()
		return info

	def getAllStockInfo(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT id, code, name, category FROM stock_info
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['id']] = item

		cur.close() 
		return info

	def getAllStockCategory(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT category FROM stock_info WHERE category != '' GROUP BY category
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item['category'])

		cur.close() 
		return info

	def getAllStockInfoByCategory(self, category):

		cur = self.conn.cursor() 
		sql = '''
			SELECT id, code, name, category FROM stock_info WHERE category = '%s'
		''' %(category)
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['id']] = item

		cur.close() 
		return info

	def getAllStockInfoByPrice(self, year, priceRule):

		nowYear = 2019
		table = 'stock_data' + '_' + str(year) if nowYear > year else 'stock_data'
		start = str(year) + '-01-01'
		end = str(year) + '-12-31'
		cur = self.conn.cursor() 
		sql = '''
			SELECT
				stock_info.id,
				stock_info.code,
				stock_info.name,
				stock_info.category 
			FROM stock_info
			LEFT JOIN %s as stock_data ON stock_info.id = stock_data.stock_id
			WHERE data_date between '%s' and '%s' %s
		''' %(table, start, end, priceRule)

		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['id']] = item

		cur.close() 
		return info

	def getStockData(self, id, year):

		nowYear = 2019
		cur = self.conn.cursor()
		table = 'stock_data' + '_' + str(year) if nowYear > year else 'stock_data'
		start = str(year) + '-01-01'
		end = str(year) + '-12-31'
		sql = '''
			SELECT 
				id, 
				stock_id, 
				data_date, 
				open, 
				highest, 
				lowest, 
				close 
			FROM %s 
			WHERE stock_id = %d 
			AND data_date between '%s' and '%s'
			AND close != ''
			ORDER BY data_date
		''' %(table, id, start, end)
		
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		i = 0
		for item in cur:
			info[i] = item
			i += 1

		cur.close() 
		return info

	def getPartStockInfo(self, begin, limit):

		cur = self.conn.cursor() 
		sql = '''
			SELECT id, code, type FROM stock_info
			WHERE id > %d
			ORDER BY id
			LIMIT %d
		''' %(begin, limit)

		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		i = 0
		for item in cur:
			info[i] = item
			i += 1

		cur.close() 
		return info

	def getAssignStockData(self, code, dateList):

		cur = self.conn.cursor()
		sql = '''
			SELECT 
				stock_info.code, 
				data_date,
				open,
				highest,
				lowest,
				close
			FROM stock_data
			LEFT JOIN stock_info ON stock_info.id = stock_data.stock_id
			WHERE stock_info.code = %d
			AND data_date in ('%s')
			ORDER BY data_date
		''' %(int(code), dateList)
		
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			if (item['code'] in info) == False:
				info[item['code']] = {}
			if item['data_date'] != '':
				info[item['code']].update({item['data_date'].strftime("%Y-%m-%d"): {'open': item['open'], 'highest': item['highest'], 'lowest': item['lowest'], 'close': item['close']}})

		cur.close() 
		return info
