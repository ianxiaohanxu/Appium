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


def list_minus(small,big):
		try:
			assert (isinstance(small,list) & isinstance(big,list))
		except AssertionError:
			print 'list_minus argument must be list.'
		
		newlist=[]
		for item in big:
			if item not in small:
				newlist.append(item)
				
		return newlist
		
		
class Test(unittest.TestCase):
	def setUp(self):
		#self.driver = webdriver.Firefox()
		#self.driver.implicitly_wait(30)
		#self.base_url ='https://login.live.com/'
		#self.base_url ='http://www.renren.com/'
		self.verificationErrors = []
		self.accept_next_alert = True
		self.displayed_links=[]
		#self.driver.get(self.base_url)
		#self.driver.set_page_load_timeout(10)
		self.manual_check_count=0
		#self.current_window=self.driver.current_window_handle
	
	
	def close_window(self, close, To_window=None):
		if To_window==None:
			To_window=self.driver.current_window_handle
		
		# close current window		
		if close==self.driver.current_window_handle:
			self.driver.close()
		
		# close other window
		else:
			try:
				self.driver.switch_to_window(close)
				self.driver.close()
			except NoSuchWindowException:
				#pdb.set_trace()
				print '%s not found.' %close
			
		
		# switch to target window
		self.driver.switch_to_window(To_window)
		
		
	def focus(self, what, how='id'):
		'''
		Default find mode is 'by id'
		'''
		self.assertTrue(self.is_element_present(how, what), 'Element not found, %s is %s' %(how, what))
		element=self.driver.find_element(by=how, value=what)
		return element
		
		
	def click(self, what, how='id'):
		'''
		Default find mode is 'by id'
		'''
		element=self.focus(what, how)
		self.assertTrue(element.is_displayed(),'The item you focus is not displayed, %s is %s' %(how, what))
		self.assertNotEqual(element.click(), TimeoutException, 'Time out when click this: %s is %s' %(how, what))
		
	def open(self, what, how='id'):
		'''
		Default find mode is 'by id'
		'''
		pre_window_handles=self.driver.window_handles[:]
		self.click(what, how)
		if not self.driver.window_handles==pre_window_handles:
			self.driver.switch_to_window(self.driver.window_handles[-1])
			
		
	def clear(self, what, how='id'):
		element=self.focus(what, how)
		self.assertTrue(element.is_displayed(),'The item you focus is not displayed, %s is %s' %(how, what))
		element.clear()
		
		
	def enter(self, what, where, how='id'):
		'''
		Default find mode is 'by id'
		'''
		element=self.focus(where, how)
		self.assertTrue(element.is_displayed(),'The item you focus is not displayed, %s is %s' %(how, where))
		element.send_keys(what)
		
		
	def switch(self,title=None):
		if title==None:
			return
			
		else:
			windows_list=self.driver.window_handles
			windows_list.reverse()
			for window in windows_list:
				try:
					self.driver.switch_to_window(window)
				except NoSuchWindowException:
					print '%s not found.' %window
					continue
				if self.driver.title==title:
					break
		
		
	def select(self, what, where, how='id'):
		element=self.focus(where, how)
		self.assertTrue(element.is_displayed(),'The item you focus is not displayed, %s is %s' %(how, where))
		Select(element).select_by_visible_text(what)
		
		
	def is_link_open(self,link_item):
		#global displayed_links
		text=link_item.text
		href=link_item.get_attribute('href')
		pre_win_handles=self.driver.window_handles[:]
		pre_url=self.driver.current_url
		#pdb.set_trace()
		try:
			#pdb.set_trace()
			link_item.click()
		except TimeoutException:
			print 'Page not loaded completely in 30s, [Text is "%s", href is "%s".' %(text, href)
			self.manual_check_count+=1
			self.driver.get(self.base_url)
			self.displayed_links=[item for item in self.driver.find_elements_by_xpath('//a[@href]') if item.is_displayed()]
			return
		after_win_handles=self.driver.window_handles
		after_url=self.driver.current_url
		#Open new page in same window
		if pre_win_handles==after_win_handles:
			if pre_url==after_url:
				#pdb.set_trace()
				try:
					print 'Manual check that [Text is "%s", href is "%s".' %(link_item.text, link_item.get_attribute('href'))
				except StaleElementReferenceException:
					self.driver.get(self.base_url)
					self.displayed_links=[item for item in self.driver.find_elements_by_xpath('//a[@href]') if item.is_displayed()]
					return
				self.manual_check_count+=1
				#self.driver.get(self.base_url)
				#self.displayed_links=[item for item in self.driver.find_elements_by_xpath('//a[@href]') if item.is_displayed()]
				return
			else:
				#driver.back()
				self.driver.get(self.base_url)
				self.displayed_links=[item for item in self.driver.find_elements_by_xpath('//a[@href]') if item.is_displayed()]
				return

		#Open new page in a new window	
		new_open=list_minus(pre_win_handles,after_win_handles)

		# Modify according to different criterion
		if len(new_open) >0:
			for i in new_open:
				self.close_window(i)
		
		'''
		for window in new_open:
			driver.switch_to_window(window)
		'''
		
		
	#@unittest.skip('skip')
	def check_links(self):
		#global displayed_links
		print ''
		links=self.driver.find_elements_by_xpath('//a[@href]')
		if len(links)==0:
			print 'No link on the page!'
			return
		self.displayed_links=[item for item in links if item.is_displayed()]	
		links_len=len(self.displayed_links)
		if links_len==0:
			print 'No displayed link on the page!'
			return
				
		for i in range(links_len-1):
			#pdb.set_trace()
			self.is_link_open(self.displayed_links[i])
			
		print ''
		print ''
		print 'Totally %d links on the page, %d links need to be MANUAL CHECK.' %(links_len, self.manual_check_count)
	'''
	def runTest(self):
		pdb.set_trace()
		self.click('这是什么', 'partial link text')
		self.close_window(self.driver.window_handles[1])
		self.enter('1234567890', 'i0116')
		self.click('idSIButton9')
	'''

	def is_element_present(self, how, what):
		try: 
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException: 
			return False
		return True
    
	def is_alert_present(self):
		try: 
			self.driver.switch_to_alert()
		except NoAlertPresentException, e: 
			return False
		return True
    
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
    
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		
		
