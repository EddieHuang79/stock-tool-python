#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from base import baseSelenium

class system(baseSelenium):

	def openBrowser(self, url):
		self.driver.get(url)
		self.time.sleep(2)
		return True

	def closeBrowser(self):
		self.driver.close()
		self.driver.quit()
		return True