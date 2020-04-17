#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

class stockToolModel:

	conn = pymysql.connect(
		host = '127.0.0.1', 
		user = 'root',
		passwd = "root",
		db = 'stock-tool',
		charset = 'utf8mb4',
		cursorclass = pymysql.cursors.DictCursor
	)

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
