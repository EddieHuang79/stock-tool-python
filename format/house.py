#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta

class houseFormat:
	one_days_ago = (date.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
	two_days_ago = (date.today() - timedelta(days = 2)).strftime('%Y-%m-%d')
	def getHouseFormat(self, data):
		result = '''
				名稱: %s
				地址: %s
				屋齡: %s
				類型: %s
				%s
				%s
				%s
				%s
				%s
				%s
				%s
				%s
				%s
				%s
				連結: %s
			''' %(data['name'], 
				data['address'], 
				data['age'], 
				data['house_type'], 
				data['total_area'], 
				data['use_area'], 
				data['public_area'], 
				data['floor'], 
				data['management_fee'], 
				data['use_for'], 
				data['notice'], 
				data['has_dereactors'], 
				data['window_in_toilet'], 
				data['window_in_all_room'],
				data['link'])
		return result