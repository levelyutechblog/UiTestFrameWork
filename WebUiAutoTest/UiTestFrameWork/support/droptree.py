# -*- coding: utf-8 -*-
from base import BaseItem

class Droptree(BaseItem):

	def __init__(self, item_suffix, browser_obj, xpath, p_locate):
		self._init_item(item_suffix)
		self.browser_obj = browser_obj
		self.xpath = xpath
		self.pTree = self.pTree if p_locate is None else p_locate + self.pTree

	def click(self):

		self.browser_obj.click(self.xpath)

	def _expand_tree(self):

		def wrapper():
			closeNodes = self.browser_obj.get_element(self.pTree + self.closeNode, multiple=True, timeout= 1, warming=False)
			if not closeNodes:
				return
			numbers = len(closeNodes)
			if not numbers:
				return False
			self.browser_obj.click(self.pTree + self.closeNode + '[1]')
			return True

		while True:
			if not wrapper():
				break

	def select_by_index(self, index):
		# todo
		pass

	def get_value(self):

		element = self.browser_obj.get_element(self.xpath)
		return element.get_attribute('value')

	def set_value(self, values):

		self._expand_tree()
		if isinstance(values, list):
			for val in values:
				if not self.is_selected(val):
					node_xpath = "{pTree}{treeNode}{checkBoxNode}".format(pTree=self.pTree, treeNode= self.treeNode, checkBoxNode= self.checkBoxNode).replace('$value', val)
					self.browser_obj.click(node_xpath)
		else:
			node_xpath = "{pTree}{treeNode}{checkBoxNode}".format(pTree=self.pTree, treeNode=self.treeNode, checkBoxNode= self.checkBoxNode).replace('$value', values)
			self.browser_obj.click(node_xpath)

	def is_selected(self, value):

		checkBox_xpath = "{pTree}{treeNode}{checkBoxNode}".format(pTree=self.pTree, treeNode= self.treeNode, checkBoxNode= self.checkBoxNode).replace('$value', value)
		element = self.browser_obj.get_element(checkBox_xpath)
		for k, v in self.isCheck.items():
			if v not in element.get_attribute(k):
				return False
		return True

	def type(self, value, xpath):

		item_xpath = "{pTree}{checkNode}{xpath}".format(pTree=self.pTree, checkNode= self.checkNode, xpath= xpath)
		self.browser_obj.type(item_xpath, value)

	def text(self, xpath):

		item_xpath = "{pTree}{checkNode}{xpath}".format(pTree=self.pTree, checkNode= self.checkNode, xpath= xpath)
		return self.browser_obj.get_element(item_xpath).get_attribute('value')

	value = property(get_value, set_value)

	del get_value
	del set_value