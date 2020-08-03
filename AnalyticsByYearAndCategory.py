#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from service.stock import stockToolService
import os.path
import sys
from os import path

# 取得所有股票分類
countType = sys.argv[1]
if countType == 'Top' or countType == 'Bottom':
	stockInfoCategory = stockToolService.getAllStockCategory()
	year = [2020, 2019, 2018, 2017, 2016]
	fileName = countType + 'AnalyticsByYearAndCategory.txt'
	fileOpMode = 'a' if path.exists(fileName) else 'x'
	f = open(fileName, fileOpMode)

	for yearItem in year:
		for category in stockInfoCategory:
			stockInfo = stockToolService.getAllStockInfoByCategory(category)
			total = 0
			highToLow = 0
			lowToHigh = 0
			equal = 0
			highToLowPercent = 0
			lowToHighPercent = 0
			equalPercent = 0
			for stockId in stockInfo:
				data = stockToolService.getTopLimitData(stockId, yearItem) if countType == 'Top' else stockToolService.getBottomLimitData(stockId, yearItem)
				total += data['total']
				highToLow += data['highToLow']
				lowToHigh += data['lowToHigh']
				equal += data['equal']
			highToLowPercent = round((highToLow / total) * 100, 2) if total > 0 else 0
			lowToHighPercent = round((lowToHigh / total) * 100, 2) if total > 0 else 0
			equalPercent = round((equal / total) * 100, 2) if total > 0 else 0
			print(yearItem, category)
			f.write(','.join([str(yearItem), str(category), str(total), str(highToLow), str(lowToHigh), str(equal), str(highToLowPercent), str(lowToHighPercent), str(equalPercent)]) + '\n')

	f.close()
	stockToolService.closeConnection()