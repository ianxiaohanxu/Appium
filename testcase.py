# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
import unittest, time, re, pdb
import test_package

class testcase(test_package.Test):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.domain='gatherhealth.com'
		self.base_url ='https://gatherhealth.com'
		#self.base_url ='http://www.kaixin001.com/'
		self.verificationErrors = []
		self.accept_next_alert = True
		self.displayed_links=[]
		self.driver.get(self.base_url)
		self.driver.set_page_load_timeout(30)
		self.manual_check_count=0
		#pdb.set_trace()
		
	def test_check_all_links(self):
		'''
		check all pages and links in the website are worked.
		'''
		self.check_all_links()
		
	@unittest.skip('skip')	
	def test_check_links(self):
		'''
		check all the links on the page is worked.
		'''
		#pdb.set_trace()
		self.check_links()
	
	@unittest.skip('skip')	
	def test_sign_up(self):
		'''
		make a new account.
		'''
		self.enter('alex-aaa011','user[login]','name')
		self.enter('alex-aaa011@163.com','user[email]','name')
		self.enter('abcd1234','user[password]','name')
		self.click('//button','xpath')
		self.click('//button[@data-org-text]','xpath')
		self.click('account_settings')
		self.click('Account settings','link text')
		self.enter('abcd1234','user_old_password')
		self.enter('abcd1234','user_new_password')
		self.enter('abcd1234','user_confirm_new_password')
		self.click('//button[@tabindex="2"]','xpath')
		self.click('//button','xpath')
		
		'''
		self.click('Delete your account','link text')
		self.enter('alex-aaa003','sudo_login')
		self.enter('delete my account','confirmation_phrase')
		self.click('Cancel plan and delete this account','link text')
		'''
		self.assertEqual('https://github.com/',self.driver.current_url)
	
	
	
	
if __name__ == "__main__":
    unittest.main(verbosity=2)
