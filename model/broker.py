#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from model.base import baseModel
from datetime import date

class brokerModel(baseModel):

	def setBrokerInfo(self, code, name):

		cur = self.conn.cursor()
		sql = '''
			INSERT INTO broker (code, name, created_at, updated_at) VALUES ("%s", "%s", NOW(), NOW());
		''' %(code, name)
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 

		return True

	def getBrokerInfo(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT * FROM broker;
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['id']] = item

		cur.close() 
		return info

	def setBrokerBranch(self, data):

		cur = self.conn.cursor()
		sql = '''
			INSERT INTO broker_branch (parent_id, is_total, code, name, created_at, updated_at) VALUES ("%d", "%d", "%s", "%s", NOW(), NOW());
		''' %(data['parent_id'], data['is_total'], data['code'], data['name'])
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 

		return True

	def getBrokerBranch(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT broker.code as 'parentCode', broker_branch.id, broker_branch.code FROM broker LEFT JOIN broker_branch ON broker.id = broker_branch.parent_id;
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = {}

		for item in cur:
			info[item['id']] = item

		cur.close() 
		return info

	def getExisingtBranchId(self, date):

		nowYear = date.today().year
		year = date.year
		table = 'broker_data' + '_' + year if nowYear > year else 'broker_data'

		cur = self.conn.cursor() 
		sql = '''
			SELECT broker_branch_id FROM %s WHERE `data_date` = '%s' GROUP BY `broker_branch_id`;
		''' %(table, date.strftime('%Y-%m-%d'))

		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item['broker_branch_id'])

		cur.close() 
		return info

	def addBrokerData(self, item):

		cur = self.conn.cursor()
		sql= '''
			INSERT INTO broker_data (stock_id, broker_branch_id, data_date, is_total, buy_number, sell_number, created_at, updated_at) VALUES ("%d", "%d", "%s", "%d", "%d", "%d", NOW(), NOW());
		''' %(item['stock_id'], item['broker_branch_id'], item['data_date'], item['is_total'], item['buy_number'], item['sell_number'])

		cur.execute(sql.replace('\n\t\t', ''))

		self.conn.commit()
		cur.close() 

		return True
