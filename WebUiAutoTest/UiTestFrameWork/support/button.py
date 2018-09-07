# -*- coding: utf-8 -*-
class Button(object):

	def __init__(self, browser_obj, xpath, p_locate):
		self.browser_obj = browser_obj
		self.xpath = xpath

	def click(self):

		self.browser_obj.click(self.xpath)

