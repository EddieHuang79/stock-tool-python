#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from service.stock import stockToolService
import os.path
import sys
from os import path

# 取得所有股票
countType = sys.argv[1]
if countType == 'Top' or countType == 'Bottom':
	stockInfo = stockToolService.getAllStockInfo()
	year = [2020, 2019, 2018, 2017, 2016]
	fileName = countType + 'AnalyticsByYear.txt'
	fileOpMode = 'a' if path.exists(fileName) else 'x'
	f = open(fileName, fileOpMode)

	for yearItem in year:
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
		highToLowPercent = round((highToLow / total) * 100, 2)
		lowToHighPercent = round((lowToHigh / total) * 100, 2)
		equalPercent = round((equal / total) * 100, 2)
		print(yearItem)
		f.write(','.join([str(yearItem), str(total), str(highToLow), str(lowToHigh), str(equal), str(highToLowPercent), str(lowToHighPercent), str(equalPercent)]) + '\n')

	f.close()
	stockToolService.closeConnection()