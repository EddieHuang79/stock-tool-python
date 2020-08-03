#!/usr/bin/python
# -*- coding: utf-8 -*-
errorCount = 0	
age_of_mine = 22
# 語法：range(start, stop[, step]) 裡面的 step 預設是 1
# for i in range(99):
while errorCount < 3:
	age = int(raw_input("guess age:"))
	if age == age_of_mine:
		print('Correct')
	else:
		print('Wrong!')
		errorCount += 1
		if errorCount > 2:
			Continue = raw_input("Continue? (y/n): ")
			if Continue == 'y':
				errorCount = 0
else:
	print('呵呵')