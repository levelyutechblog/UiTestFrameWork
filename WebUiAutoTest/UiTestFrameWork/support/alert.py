# -*- coding: utf-8 -*-

class Alert(object):

	def __init__(self, browser_obj, xpath, p_locate):
		self.browser_obj = browser_obj
		self.xpath = xpath

	@property
	def text(self):

		element = self.browser_obj.get_element(self.xpath)
		return element.text