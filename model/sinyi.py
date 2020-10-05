#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql
from datetime import date, timedelta, datetime
from model.base import baseModel
import sys

class sinyiModel(baseModel):

	def addHouseData(self, item):

		cur = self.conn.cursor()
		sql = '''
			INSERT INTO sinyi (
				object_id, 
				type, 
				name, 
				age, 
				house_type, 
				total_area, 
				use_area, 
				spec, 
				floor, 
				has_dereactors, 
				window_in_toilet, 
				window_in_all_room, 
				link, 
				get_list_time, 
				get_detail_time, 
				send_time, 
				created_at, 
				updated_at,
				address) VALUES ("%s", 1, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", NOW(), '0000-00-00 00:00:00', '0000-00-00 00:00:00', NOW(), NOW(), "%s");
		''' %(
			item['object_id'], 
			item['name'], 
			item['age'], 
			item['house_type'], 
			item['total_area'], 
			item['use_area'], 
			item['spec'], 
			item['floor'], 
			item['has_dereactors'], 
			item['window_in_toilet'], 
			item['window_in_all_room'],
			item['link'],
			item['address'])
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 

		return True

	def getExistObjectId(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT object_id FROM sinyi
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item['object_id'])

		cur.close() 
		return info

	def getUpdateData(self):

		cur = self.conn.cursor() 
		sql = '''
			SELECT id, link FROM sinyi WHERE type = 1
		'''
		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item)

		cur.close() 
		return info

	def updateHouseData(self, item, id):

		cur = self.conn.cursor()
		sql = '''
			UPDATE sinyi SET
				type = 2, 
				public_area = '%s', 
				management_fee = '%s', 
				park = '%s', 
				use_for = '%s', 
				notice = '%s', 
				address = '%s', 
				get_detail_time = NOW()
			WHERE id = %d;
		''' %(
			item['public_area'], 
			item['management_fee'], 
			item['park'], 
			item['use_for'], 
			item['notice'],
			item['address'],
			int(id))
		
		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 
		return True

	def findByAddress(self, item):
		cur = self.conn.cursor() 
		sql = 'SELECT id, address FROM sinyi WHERE type != 4 AND address like "%' + item['section'] + '%"'
		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item)

		cur.close() 
		return info

	def updateNotNeedHouseData(self, data):

		cur = self.conn.cursor()
		sql = '''
			UPDATE sinyi SET type = 4 WHERE id in (%s);
		''' %(','.join(data))

		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 
		return True

	def getSendData(self, limit):

		cur = self.conn.cursor()
		sql = '''
			SELECT * FROM sinyi WHERE type = 2 LIMIT %d;
		''' %(limit)

		cur.execute(sql.replace('\n\t\t', ' '))

		info = []

		for item in cur:
			info.append(item)

		cur.close() 
		return info

	def updateSendData(self, id):

		cur = self.conn.cursor()
		sql = '''
			UPDATE sinyi SET type = 3 WHERE id in (%s);
		''' %(','.join(id))

		cur.execute(sql.replace('\n\t\t', ' '))

		self.conn.commit()
		cur.close() 
		return True
