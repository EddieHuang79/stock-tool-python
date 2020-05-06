#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

class baseModel:

	conn = pymysql.connect(
		host = '127.0.0.1', 
		user = 'root',
		passwd = "root",
		db = 'stock-tool',
		charset = 'utf8mb4',
		cursorclass = pymysql.cursors.DictCursor
	)

	def closeConnection(self):
		self.conn.close()
		return True
