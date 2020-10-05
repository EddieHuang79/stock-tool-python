#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import date, timedelta, datetime
from service.base import baseService
from service.holiday import holidayService
from service.dividend import dividendService
from service.stock import stockToolService
import time
import sys
import json
from lib.log import log

class strategyService(baseService):

	def getStockPriceDiffAtDividendRange(data):
		today = datetime.strptime(datetime.today().strftime("%Y-%m-%d"), '%Y-%m-%d')
		startYear = 2016;
		endYear = int(datetime.today().strftime("%Y"))
		endDay = 3
		lang = {
			-3: '前3天',
			-2: '前2天',
			-1: '前1天',
			0: '當天',
			1: '後1天',
			2: '後2天',
			3: '後3天',
			'open': '開盤',
			'close': '收盤',
			'buyAt': '買進',
			'sellAt': '賣出',
		}
		logData = {'data': {}, 'historyDividend': {}, 'dayList': {}, 'stockData': {}, 'rules': [], 'strategyResult': {}}
		historyDividend = {}
		dayList = {}

		# 抓個股歷年除權息日程
		# historyDividend = {1590: {2020: '2020-09-03', 2019: '2019-09-03', 2018: '2018-08-30', 2017: '2017-06-15', 2016: '2016-08-29', 2015: '2015-06-15'}}
		logData['data'] = data
		log.writeLog('dividendData - 除權息清單', logData['data'])
		for item in data:
			code = int(item['code'])
			historyDividend[code] = {}
			logData['historyDividend'][code] = {}
			dividendData = dividendService.getExistDataByCode(item['code'])
			for dividendItem in dividendData['data']:
				if dividendItem['year'] >= startYear:
					historyDividend[code][dividendItem['year']] = dividendItem['dividend_date']
					logData['historyDividend'][code][dividendItem['year']] = dividendItem['dividend_date'].strftime("%Y-%m-%d")

		# 抓執行日期
		# dayList = {'2020-09-03': {-3: '2020-08-31', -2: '2020-09-01', -1: '2020-09-02', 0: '2020-09-03', 1: '2020-09-04', 2: '2020-09-07', 3: '2020-09-08'}}
		log.writeLog('historyDividend - 歷年除權息', logData['historyDividend'])
		for code in historyDividend:
			for year in historyDividend[code]:
				if year >= startYear:
					dividend_date = historyDividend[code][year]
					dividendDateString = historyDividend[code][year].strftime("%Y-%m-%d")
					if (dividend_date in dayList) == False:
						dayList[dividend_date] = {}
						logData['dayList'][dividendDateString] = {}
						excuteDay = -3
						while excuteDay <= endDay:
							if excuteDay != 0:
								type = 'add' if excuteDay > 0 else 'minus'
								dayList[dividend_date][excuteDay] = holidayService.getNextWorkDate(abs(excuteDay), type, dividend_date)
								logData['dayList'][dividendDateString][excuteDay] = dayList[dividend_date][excuteDay]
							else:
								dayList[dividend_date][excuteDay] = dividendDateString
								logData['dayList'][dividendDateString][excuteDay] = dividendDateString
							excuteDay += 1

		# 抓個股指定日期的四檔
		# {code: [date: {open: '', close: '', 'highest': '', 'lowest': ''}, ...], ...}
		log.writeLog('dayList - 除權息前後幾日日期', logData['dayList'])
		stockData = {}
		for code in historyDividend:
			dateList = {}
			dateList[code] = []
			for year in historyDividend[code]:
				dateList[code] += dayList[historyDividend[code][year]].values()
			if len(dateList[code]) > 0:
				stockData.update(stockToolService.getAssignStockData(code, "','".join(dateList[code])))
		logData['stockData'] = stockData

		# 組合策略列表 每檔有 7 * 7 條規則 賣出日要 >= 買進日
		# [{'buy': -2, 'sell', 0}, ]
		log.writeLog('dayList - 除權息前後幾日對應股價', logData['stockData'])
		rules = []
		buy = -3
		while buy < endDay:
			sell = -3
			while sell <= endDay:
				# 賣出日期不可小於買進日期，也要排除跨過除權息日程的策略，除權息價差會影響判斷
				if sell >= buy and (sell >= 0 and buy < 0) == False:
					rules.append({'buy': buy, 'sell': sell, 'buyAt': 'open', 'sellAt': 'close'})
					if buy != sell:
						rules.append({'buy': buy, 'sell': sell, 'buyAt': 'close', 'sellAt': 'open'})
						rules.append({'buy': buy, 'sell': sell, 'buyAt': 'open', 'sellAt': 'open'})
						rules.append({'buy': buy, 'sell': sell, 'buyAt': 'close', 'sellAt': 'close'})
				sell += 1
			buy += 1

		logData['rules'] = rules
		log.writeLog('rules - 執行策略', logData['rules'])

		# 各策略組合mapping歷年對應報價，計算結果
		# {'{"buy": -3, "sell": -3, "buyAt": "open", "sellAt": "close"}': -60.0}
		result = {}
		strategyResult = {}
		for item in data:
			code = int(item['code'])
			result[code] = {}
			for year in historyDividend[code]:
				dividendDate = historyDividend[code][year]
				dividendDateRangeData = dayList[dividendDate]
				for rulesItem in rules:
					buyDate = dividendDateRangeData[rulesItem['buy']]
					sellDate = dividendDateRangeData[rulesItem['sell']]
					# if datetime.strptime(sellDate, '%Y-%m-%d').timestamp() < today.timestamp() and datetime.strptime(buyDate, '%Y-%m-%d').timestamp() < today.timestamp():
					if (code in stockData) and (buyDate in stockData[code]) and (sellDate in stockData[code]):
						# print(stockData[code])
						# sys.exit()
						buyPrice = float(stockData[code][buyDate][rulesItem['buyAt']])
						sellPrice = float(stockData[code][sellDate][rulesItem['sellAt']])
						diff = sellPrice - buyPrice
						ruleKey = json.dumps(rulesItem)
						if (ruleKey in result[code]) == False:
							result[code][ruleKey] = {'sum': 0, 'len': 0, 'data': [], 'postivePercent': 0, 'negtivePercent': 0, 'postive': 0, 'negtive': 0}
						result[code][ruleKey]['sum'] += diff
						result[code][ruleKey]['len'] += 1
						result[code][ruleKey]['postive'] += 1 if diff > 0 else 0
						result[code][ruleKey]['negtive'] += 1 if diff < 0 else 0
						result[code][ruleKey]['data'].append(dividendDate.strftime("%Y%m%d") + ': ' + str(round(diff, 2)))
			# 回寫平均值、機率
			avg = {}
			for ruleKey in result[code]:
				avg[ruleKey] = result[code][ruleKey]['sum'] / result[code][ruleKey]['len']
				result[code][ruleKey]['postivePercent'] = round((result[code][ruleKey]['postive'] / result[code][ruleKey]['len']) * 100, 2)
				result[code][ruleKey]['negtivePercent'] = round((result[code][ruleKey]['negtive'] / result[code][ruleKey]['len']) * 100, 2)

			# 用 平均值 排序最佳 & 最差 策略 各3檔
			descList = sorted(avg.items(), key=lambda d: d[1], reverse=True)
			ascList = sorted(avg.items(), key=lambda d: d[1], reverse=False)
			strategyResult[code] = {}
			strategyResult[code]['best'] = descList[0:3] if len(descList) > 0 else '沒有歷年除權息資料'
			strategyResult[code]['worst'] = ascList[0:3] if len(ascList) > 0 else '沒有歷年除權息資料'

		log.writeLog('strategyResult - 計算結果', result)
		logData['strategyResult'] = strategyResult
		log.writeLog('strategyResult - 最佳三檔', logData['strategyResult'])

		# 轉成文字，update回原本dict
		for item in data:
			code = int(item['code'])
			item['best'] = '\n'
			if isinstance(strategyResult[code]['best'], list):
				for strategyItem in strategyResult[code]['best']:
					ruleKey = json.loads(strategyItem[0])
					avg = strategyItem[1]
					item['best'] += ''' 買進時機: %s(%s), 賣出時機: %s(%s), 平均獲利: %s, 勝率: %s, 歷年紀錄: %s \n'''  %(lang[ruleKey['buy']], lang[ruleKey['buyAt']], lang[ruleKey['sell']], lang[ruleKey['sellAt']], str(round(avg, 2)), result[code][strategyItem[0]]['postivePercent'], ','.join(result[code][strategyItem[0]]['data']))
			else:
				item['best'] += '沒有歷年除權息資料'
			item['worst'] = '\n'
			if isinstance(strategyResult[code]['worst'], list):
				for strategyItem in strategyResult[code]['worst']:
					ruleKey = json.loads(strategyItem[0])
					avg = strategyItem[1]
					item['worst'] += ''' 買進時機: %s(%s), 賣出時機: %s(%s), 平均獲利: %s, 勝率: %s, 歷年紀錄: %s \n'''  %(lang[ruleKey['buy']], lang[ruleKey['buyAt']], lang[ruleKey['sell']], lang[ruleKey['sellAt']], str(round(avg, 2)), result[code][strategyItem[0]]['negtivePercent'], ','.join(result[code][strategyItem[0]]['data']))
			else:
				item['worst'] += '沒有歷年除權息資料'
		return data


