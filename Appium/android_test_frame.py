#!/usr/bin/env python
from time import sleep
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction


character_keycode = {'0': 7, '1' : 8, '2' : 9, '3' : 10, '4' : 11, '5' : 12, '6' : 13, '7' : 14, '8' : 15, '9' : 16,'a': 29, 'b' : 30, 'c' : 31, 'd' : 32, 'e' : 33, 'f' : 34, 'g' : 35, 'h' : 36, 'i' : 37, 'j' : 38, 'k' : 39, 'l' : 40, 'm' : 41, 'n' : 42, 'o' : 43, 'p' : 44, 'q' : 45, 'r' : 46, 's' : 47, 't' : 48, 'u' : 49, 'v' : 50, 'w' : 51, 'x' : 52, 'y' : 53, 'z' : 54, ' ' : 62, '-' : 69, "'" : 75, ',' : 55, '.' : 56, '/' : 76, ';' : 74, '=' : 70, '[' : 71, '\\' : 73, ']' : 72, '`' : 68, ')': 7, '!' : 8, '@' : 9, '#' : 10, '$' : 11, '%' : 12, '^' : 13, '&' : 14, '*' : 15, '(' : 16,'A': 29, 'B' : 30, 'C' : 31, 'D' : 32, 'E' : 33, 'F' : 34, 'G' : 35, 'H' : 36, 'I' : 37, 'J' : 38, 'K' : 39, 'L' : 40, 'M' : 41, 'N' : 42, 'O' : 43, 'P' : 44, 'Q' : 45, 'R' : 46, 'S' : 47, 'T' : 48, 'U' : 49, 'V' : 50, 'W' : 51, 'X' : 52, 'Y' : 53, 'Z' : 54, '_' : 69, '"' : 75, '<' : 55, '>' : 56, '?' : 76, ':' : 74, '+' : 70, '{' : 71, '|' : 73, '}' : 72, '~' : 68}
upper_key = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ':', '<', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '^', '_', '{', '|', '}', '~']
lower_key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '-', "'", ',', '.', '/', ';', '=', '[', '\\', ']', '`']


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
		self.letter_list= list(map(chr, range(32, 127)))
		
		
	def keyout(self, what = None):
		if (what is None) | (what == ''):
			return
		assert len(what) == 1, 'The parameter of keyout() must be one character.'
		if what in lower_key:
			self.driver.press_keycode(character_keycode[what])
		elif what in upper_key:
			self.driver.press_keycode(character_keycode[what], 193)
		else:
			assert 0, 'The character %s cannot be handled by keyout()' %what
		

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
		if text in self.letter_list:
			try:
				item = self.driver.find_element_by_android_uiautomator('text("%s").focused(false)' %text)
				return item
			except NoSuchElementException:
				pass
			
			try:
				item = self.driver.find_element_by_android_uiautomator('description("%s").focused(false)' %text)
				return item
			except NoSuchElementException:
				pass
				
			try:
				item = self.driver.find_element_by_id(text)
				return item
			except NoSuchElementException:
				pass
				
			try:
				item = self.driver.find_element_by_android_uiautomator('textContains("%s").focused(false)' %text)
				return item
			except NoSuchElementException:
				pass
			
			try:
				item = self.driver.find_element_by_android_uiautomator('descriptionContains("%s").focused(false)' %text)
				return item
			except NoSuchElementException:
				raise NoSuchElementException
		else:
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
				item = self.driver.find_element_by_id(text)
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
	def long_click(self, text, duration = 1000):
		item = self.focus(text)
		action = TouchAction(self.driver)
		action.long_press(el = item, duration = duration)
		action.release()
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
	def long_tap(self, x = None, y = None, duration = 1000):
		if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
			self.assertTrue(0, 'Please input correct coordinates')
		action = TouchAction(self.driver)
		action.long_press(x = x, y = y, duration = duration).release()
		action.perform()
		
	#input something into edit field
	def enter(self, what, where):
		where.click()
		sleep(1)
		self.driver.press_keycode(123)
		for letter in what:
			self.keyout(letter)
		
		'''
		try:
			where.set_text(what)
		except NoSuchElementException:
			pass
		'''
		
	#clear the edit field
	def clear(self, where):
		
		#pdb.set_trace()
		#start_time = time.time()
		where.click()
		sleep(1)
		self.driver.press_keycode(29,28672)
		#pdb.set_trace()
		self.driver.press_keycode(112)
		
		
		'''
		try:
			where.clear()
		except NoSuchElementException:
			pass
		end_time = time.time()
		duration = end_time - start_time
		pdb.set_trace()
		'''
		
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
		
	#capture a picture for an element
	def capture(self, what):
		begin = what.location
		size = what.size
		start_x = begin['x']
		start_y = begin['y']
		end_x = start_x + size['width']
		end_y = start_y + size['height']
		name = str(start_x)+'_'+str(start_y)+'_'+str(end_x)+'_'+str(end_y)
		box = (start_x, start_y, end_x, end_y)
		self.driver.get_screenshot_as_file(tmp + '/' + 'full_screen.png')
		image = Image.open(tmp + '/' + 'full_screen.png')
		newimage = image.crop(box)
		newimage.save(tmp + '/' + name + '.png')
		os.popen('rm %s/full_screen.png' %tmp)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
