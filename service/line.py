#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import json

class LineNotice:

	config = {
		'url': 'https://api.line.me/v2/bot/message/push',
		'myLineId': 'U1f4fa85618159c967669af63259916ba',
		'token': 'J5bHn4HEVHZURUysjPAMfVzHLiHdVYFYId+kw5W1BeqoCtE0ascEpbzaCerh/Z+6ygRK9mlRr4lsS9ujl01aBIBxpWKZcrBBrJkJ3uRgOFkd/kKTeD0x7/FngJHi6F8nso+n0JfOjjRGzNPDjsUYuAdB04t89/1O/w1cDnyilFU=',
		'mutilpeUrl': 'https://api.line.me/v2/bot/message/multicast',
		'allLineId': ['U1f4fa85618159c967669af63259916ba', 'U3fef27ace9791b9b6f01592c0c86bd0f', 'U1a19e56ced37a863a4a489749dad71a8'],
	}

	myHeaders = {
		'Authorization': 'Bearer ' + config['token'],
		'Content-Type': 'application/json'
	}

	def sendMessageToLine(self, message):
		if len(message) > 0:

			messages = []
			
			for item in message:
				messages.append({'type': 'text', 'text': item})
			
			myParams = {
				'to': self.config['myLineId'], 
				'messages': messages
			}
			a = requests.post(self.config['url'], headers = self.myHeaders, data = json.dumps(myParams))
		return True

	def sendMessageToLineForMutilpe(self, message):
		if len(message) > 0:

			limit = 5
			subArray = [message[i:i + limit] for i in range(0, len(message), limit)]  

			for item in subArray:
				messages = []

				for item2 in item:
					messages.append({'type': 'text', 'text': item2})

				myParams = {
					'to': self.config['allLineId'], 
					'messages': messages
				}
				a = requests.post(self.config['mutilpeUrl'], headers = self.myHeaders, data = json.dumps(myParams))

		return True