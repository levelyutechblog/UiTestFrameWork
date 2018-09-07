# -*- coding: utf-8 -*-
from base import BaseItem

class Select(BaseItem):

	def __init__(self, item_suffix, browser_obj, xpath, p_locate):
		self._init_item(item_suffix)
		self.browser_obj = browser_obj
		self.xpath = xpath
		self.pSelect = self.pSelect if p_locate is None else p_locate + self.pSelect

	def click(self):

		self.browser_obj.click(self.xpath)

	def get_value(self):

		element = self.browser_obj.get_element(self.xpath)
		return element.get_attribute('value')

	def set_value(self, value):

		def wrap(value):
			node_xpath = "{pSelect}{selectNode}".format(pSelect=self.pSelect, selectNode= self.selectNode).replace('$value', value)
			if not self.is_selected(value):
				self.browser_obj.click(node_xpath)

		if isinstance(value, list):
			for val in value:
				wrap(val)
		else:
			wrap(value)

	def is_selected(self, value):

		checkNode_xpath = "{pSelect}{selectNode}{checkNode}".format(pSelect=self.pSelect, selectNode= self.selectNode, checkNode=self.checkNode)
		checkNode_xpath = checkNode_xpath.replace('$value', value)
		element = self.browser_obj.get_element(checkNode_xpath)
		for k, v in self.isCheck.items():
			if v not in element.get_attribute(k):
				return False
		return True

		
		
	value = property(get_value, set_value)

	del get_value
	del set_value