#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from datetime import date, timedelta
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
