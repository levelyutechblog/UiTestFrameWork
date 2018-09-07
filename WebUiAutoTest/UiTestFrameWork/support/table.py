# -*- coding: utf-8 -*-
from base import BaseItem
import chardet
import re
from lxml import etree

inner_js_getLen = '''
			var eles = document.evaluate("{0}",document,null,XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,null);
			return eles.snapshotLength;
			'''

inner_js_getText = '''
			var eles = document.evaluate("{0}",document,null,XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,null);
			var result = eles.snapshotItem({1}).innerHTML;
			return result;
			'''
class Table(BaseItem):

	def __init__(self, item_suffix, browser_obj, xpath, p_locate):
		self._init_item(item_suffix)
		self.browser_obj = browser_obj
		self.xpath = xpath

	def click(self, index):

		if not hasattr(self, "clickableCol"):
			raise Exception("The table %s is not support to click." % str(self))
		clickable_xpath = "{clickableCol}".format(clickableCol=self.clickableCol)
		clickable_xpath = clickable_xpath.replace("$index", str(index))
		self.browser_obj.click(clickable_xpath)

	@property
	def len(self):

		rows_path = "{table}{row}".format(table=self.xpath, row=self.tableRow).replace("[$index]", '')
		return len(self.browser_obj.get_element(rows_path, multiple=True))

	@property
	def theads(self):
		theads = []
		js = inner_js_getLen.format(self.xpath + self.titleRow + self.titleCol)
		title_lens = self.browser_obj.js_executor.execute_script(js)
		for index in range(title_lens):
			js = inner_js_getText.format(self.xpath + self.titleRow + self.titleCol, index)
			head = self.browser_obj.js_executor.execute_script(js)
			# 保证heads内为unicode编码,避免中文乱码
			if isinstance(head, str):
				encode = chardet.detect(head).get('encoding')
				head = head.decode(encode)
			theads.append(head)
		return theads

	def get_by(self, index, tableType = '001'):
		def wraper(index):
			data = []
			row_path = "{table}{row}".format(table=self.xpath, row=self.tableRow).replace("$index", str(index))
			js = inner_js_getLen.format(self.xpath + self.titleRow + self.titleCol)
			title_lens = self.browser_obj.js_executor.execute_script(js)

			js = inner_js_getText.format(row_path, 0)
			col_text = self.browser_obj.js_executor.execute_script(js)

			doc = etree.HTML(col_text, parser=etree.HTMLParser(encoding='utf-8'))

			if tableType == '001':
				elements = doc.findall("")
				for element in elements:
					if element.get('class') == '' or element.get('class') == '':
						continue
					else:
						data.append(element.xpath('string(.)').strip())
			else:
				elements = doc.xpath("")
				for element in elements:
					if element.get('class') == '' or element.get('class') == '':
						continue
					else:
						data.append(element.xpath('string(.)').strip())
			return data

		if isinstance(index, int):
			return wraper(index)
		elif isinstance(index, list):
			data = []
			for i in index:
				data.append(wraper(i))
			return data

	def select_all(self):

		xpath = "{table}{checkAll}".format(table=self.xpath, checkAll=self.checkAll)
		self.browser_obj.click(xpath)	

	def select_by(self, index):

		def wraper(index, multiple=False):
			if multiple:
				select_xpath = "{table}{row}{checkbox}".format(table=self.xpath, row=self.tableRow, checkbox=self.checkBox)
			else:
				select_xpath = "{table}{row}{radio}".format(table=self.xpath, row=self.tableRow, radio=self.radio)
			select_xpath = select_xpath.replace("$index", str(index))
			self.browser_obj.click(select_xpath)

		if isinstance(index, int):
			wraper(index)
		elif isinstance(index, list):
			for i in index:
				wraper(i, True)
	# 注：
	# 仅限于订单表格
	def type(self, value, item_xpath, locate_value, locate_xpath):

		xpath = "{table}{locate}{item}".format(table=self.xpath, locate=locate_xpath, item=item_xpath).replace('$value',locate_value)
		self.browser_obj.type(xpath, value)

	# 注：
	# 仅限于订单表格
	def text(self, item_xpath, locate_value, locate_xpath):

		xpath = "{table}{locate}{item}".format(table=self.xpath, locate=locate_xpath, item=item_xpath).replace('$value',locate_value)
		return self.browser_obj.get_element(xpath).text

	# 注：
	# 仅限于订单表格
	def value(self, item_xpath, locate_value, locate_xpath):

		xpath = "{table}{locate}{item}".format(table=self.xpath, locate=locate_xpath, item=item_xpath).replace('$value',locate_value)
		return self.browser_obj.get_element(xpath).get_attribute('value')

	@property
	def pagination(self):

		page_xpath = "{table}{pageNumber}".format(table=self.xpath, pageNumber=self.pageNumber)
		element = self.browser_obj.get_element(page_xpath)
		return re.findall("\d+", element.text)[0] if element.text else None

	@property
	def current_pagination(self):

		curPage_xpath = "{table}{currentPage}".format(table=self.xpath, currentPage=self.currentPage)
		element = self.browser_obj.get_element(curPage_xpath)
		return element.get_attribute('value')

	@property
	def numbers(self):

		numbers_xpath = "{table}{wholeNumber}".format(table=self.xpath, wholeNumber=self.wholeNumber)
		element = self.browser_obj.get_element(numbers_xpath)
		return re.findall("\d+", element.text)[0] if element.text else None

	def next(self):

		next_xpath = "{table}{next}".format(table=self.xpath, next=self.nextBtn)
		self.browser_obj.click(next_xpath)

	def previous(self):

		previous_xpath = "{table}{previous}".format(table=self.xpath, previous=self.previousBtn)
		self.browser_obj.click(previous_xpath)

	def first(self):

		first_xpath = "{table}{first}".format(table=self.xpath, first=self.firstBtn)
		self.browser_obj.click(first_xpath)

	def last(self):

		last_xpath = "{table}{last}".format(table=self.xpath, last=self.lastBtn)
		self.browser_obj.click(last_xpath)

