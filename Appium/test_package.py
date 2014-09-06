#!/usr/bin/env python
from time import sleep

import unittest

from appium import webdriver

class mobiletest(unittest.TestCase):

	def __init__(self):
		#ios hardkey keycode
		self.android['Power']= 26
		self.android['Camera']= 27
		self.android['Volumn_Up']= 24
		self.android['Volumn_Down']= 25
		self.android['Home']= 3
		self.android['Back']= 4
		self.android['Menu']= 82
		'''
		#IOS hardkey keycodes
		ios['Power']= 
		ios['Camera']= 
		ios['Volumn_Up']= 
		ios['Volumn_Down']= 
		ios['Home']= 
		ios['Back']= 
		ios['Menu']= 
		'''

	def press(self, keyName, count=1):
		
		
