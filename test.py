# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
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
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url ='https://login.live.com/'
		#self.base_url ='http://www.renren.com/'
		self.verificationErrors = []
		self.accept_next_alert = True
		self.displayed_links=[]
		self.driver.get(self.base_url)
		self.driver.set_page_load_timeout(10)
		self.manual_check_count=0
	
	
	def is_link_open(self,link_item):
		#global displayed_links
		pre_win_handles=self.driver.window_handles[:]
		pre_url=self.driver.current_url
		#pdb.set_trace()
		link_item.click()
		after_win_handles=self.driver.window_handles
		after_url=self.driver.current_url
		#Open new page in same window
		if pre_win_handles==after_win_handles:
			if pre_url==after_url:
				#pdb.set_trace()
				print 'Manual check that [ID is "%s", Text is "%s", Title is "%s", href is "%s", Onclick is "%s".' %(link_item.get_attribute('id'),link_item.text,link_item.get_attribute('title'),link_item.get_attribute('href'),link_item.get_attribute('onclick'))
				self.manual_check_count+=1
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
		print '%d links need to be MANUAL CHECK.' %self.manual_check_count
		
		
	#print check_links()

	def test_test(self):
		self.assertEqual(1,2,'not equal')

	'''
	link1=driver.find_element_by_partial_link_text('这是什么')
	print driver.title
	tem=link1.click()
	print driver.title
	type(tem)
	print tem
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


if __name__ == "__main__":
    unittest.main(verbosity=2)		
#Test('test_test').run()
#a.run()		
#suite = unittest.TestLoader().loadTestsFromTestCase(Test)
#names=unittest.TestLoader().getTestCaseNames(Test)
#print names
#unittest.TextTestRunner(verbosity=2).run(suite)
