#!/usr/bin/env python
from time import sleep
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class mobiletest(unittest.TestCase):

	def setUp(self):
		self.android = {}
		self.android['Power']= 26
		self.android['Camera']= 27
		self.android['Volumn_Up']= 24
		self.android['Volumn_Down']= 25
		self.android['Home']= 3
		self.android['Back']= 4
		self.android['Menu']= 82

	#press hardkey, if double press, pass in 'count = 2'
	def press(self, keyName, count=1):
		self.assertIn(keyName, self.android.keys(), 'Hard key name is wrong.')
		while count > 0:
			self.driver.press_keycode(self.android[keyName])
			count-=1
			sleep(0.5)
		return self
		
	#long press hardkey
	def long_press(self, keyName):
		self.assertIn(keyName, self.android.keys(), 'Hard key name is wrong.')
		self.driver.long_press_keycode(self.android[keyName])
		return self
		
	#find an item, return webelement object
	def focus(self, text):
		try:
			item = self.driver.find_element_by_android_uiautomator('text("%s")' %text)
			return item
		except NoSuchElementException:
			pass
			
		try:
			item = self.driver.find_element_by_android_uiautomator('description("%s")' %text)
			return item
		except NoSuchElementException:
			pass
			
		try:
			item = self.driver.find_element_by_android_uiautomator('textContains("%s")' %text)
			return item
		except NoSuchElementException:
			pass
			
		try:
			item = self.driver.find_element_by_android_uiautomator('descriptionContains("%s")' %text)
			return item
		except NoSuchElementException:
			raise NoSuchElementException
		
	#tap some item with text or description attribute
	def click(self, text, count=1):
		item = self.focus(text)
		while count > 0:
			item.click()
			count-=1
			sleep(0.5)
			
	#long tap some item with text or description attribute
	def long_click(self, text):
		item = self.focus(text)
		action = TouchAction(self.driver)
		action.long_press(el = item).release()
		action.perform()
		
	#tap a coordinates (x,y)
	def tap(self, x = None, y = None, count = 1):
		if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
			self.assertTrue(0, 'Please input a correct coordinate')
		while count > 0:
			action = TouchAction(self.driver)
			action.press(x = x, y = y).release()
			action.perform()
			count-=1
			sleep(0.5)
		
	#long tap a coordinates (x,y)
	def long_tap(self, x = None, y = None):
		if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
			self.assertTrue(0, 'Please input correct coordinates')
		action = TouchAction(self.driver)
		action.long_press(x = x, y = y).release()
		action.perform()
		
	#input something into edit field
	def enter(self, what, where):
		where.send_keys(what)
		
	#clear the edit field
	def clear(self, where):
		where.clear()
		
	#drag something to somewhere
	def drag(self, origin_el = None, target_el = None, x = None, y = None):
		if not (target_el is None):
			action = TouchAction(self.driver)
			action.\
				long_press(origin_el).\
				move_to(target_el).\
				release().\
				perform()
		elif (x == None) | (y == None) | (x > self.X) | (y > self.Y):
			self.assertTrue(0, 'Please input correct coordinates')
		else:
			action = TouchAction(self.driver)
			action.\
				long_press(origin_el).\
				move_to(x = x, y = y).\
				release().\
				perform()
			
	#swip from somewhere to somewhere
	def swip(self, start_x = None, start_y = None, end_x = None, end_y = None):
		if (start_x == None) | (start_y == None) | \
			(start_x > self.X) | (start_y > self.Y) | \
			(end_x == None) | (end_y == None) | \
			(end_x > self.X) | (end_y > self.Y):
				self.assertTrue(0, 'Please input correct coordinates')
		action = TouchAction(self.driver)
		action.\
			press(x = start_x, y = start_y).\
			move_to(x = end_x, y = end_y).\
			release().\
			perform()
			
	#zoom in
	def zoom_in(self, element = None, percent = 200, steps = 50):
		self.driver.zoom(element, percent, steps)
		
	#zoom out
	def zoom_out(self, element = None, percent = 200, steps = 50):
		self.driver.pinch(element, percent, steps)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
