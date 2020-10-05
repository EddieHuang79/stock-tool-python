#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from base import baseSelenium

class user(baseSelenium):

	def login(self):
		# 輸入帳號
		account = self.driver.find_element_by_id('inputEmail')
		account.click()
		account.send_keys("eddie.huang@kkday.com")
		# 輸入密碼
		password = self.driver.find_element_by_id('inputPassword')
		password.click()
		password.send_keys("123456")
		# 按登入
		loginBtn = self.driver.find_element_by_id('loginBtn')
		loginBtn.click()
		self.time.sleep(5)
		return True

	def chooseSupplier(self):
		# 展開供應商選單
		selectSupplier = self.driver.find_element_by_id('select2-supplierID-container')
		selectSupplier.click()
		self.time.sleep(2)
		# 選供應商
		supplierList = self.driver.find_element_by_css_selector('li.select2-results__option:first-child')
		supplierList.click()
		# 確認
		confirmBtn = self.driver.find_element_by_id('confirmBtn')
		confirmBtn.click()
		self.time.sleep(5)
		return True	

	def logout(self):
		# 點公告
		ann = self.driver.find_element_by_link_text('我知道了')
		ann.click()
		# 點頭像
		photo = self.driver.find_element_by_css_selector('li.user-menu.system-alert')
		photo.click()
		self.time.sleep(1)
		# 點登出
		logout = self.driver.find_element_by_id('logoutBtn')
		logout.click()
		self.time.sleep(2)
		return True