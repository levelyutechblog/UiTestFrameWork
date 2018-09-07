# -*- coding: utf-8 -*-
from base import BaseItem

class List(BaseItem):

	def __init__(self, item_suffix, browser_obj, xpath, p_locate):
		self._init_item(item_suffix)
		self.browser_obj = browser_obj
		self.xpath = xpath
		self.pList = self.pList if p_locate is None else p_locate + self.pList

	def click(self):

		self.browser_obj.click(self.xpath)

	def len(self):

		rows_path = "{list}{row}".format(list=self.xpath, row=self.listRow).replace("[$index]", '')
		return len(self.browser_obj.get_element(rows_path, multiple=True))

	def get_value(self):

		element = self.browser_obj.get_element(self.xpath)
		return element.get_attribute('value')

	def get_moduleListStatus(self, value):

		node_xpath = "{pList}{listNode}".format(pList=self.pList, listNode= self.listNode).replace('$value', value)
		menu_path = node_xpath + '/grandparent'
		element = self.browser_obj.get_element(menu_path)
		return element.get_attribute('class')

	def set_value(self, value):

		node_xpath = "{pList}{listNode}".format(pList=self.pList, listNode= self.listNode).replace('$value', value)
		self.browser_obj.click(node_xpath)

	value = property(get_value, set_value)

	del get_value
	del set_value