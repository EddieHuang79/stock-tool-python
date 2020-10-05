#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import *
import os
import json

class log:

	def writeLog(title, data):
		today = datetime.today().strftime("%Y%m%d")
		fileName = '/Users/huangjiancheng/Projects/stock-tool-python/log/%s.txt' %('log_'+today)
		opType = 'a' if os.path.isfile(fileName) else 'x'
		content = '[%s] %s\n\n' %(title, json.dumps(data))

		f = open(fileName, opType)
		f.write(content)
		f.close()

		return True
