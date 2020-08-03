#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

class stockApi:
	def getTopLimitInfo():
		response = requests.get("https://www.cnyes.com/twstock/ranking2.aspx?")
		return response.text
