# -*- coding: utf-8 -*-
from nose.tools import *
from config import *
import time
from custom_page.pLogin import loginPage
from dagger.page import PageFactory

class Extensions(object):

	def __init__(self, page_obj):
		self.page_obj = page_obj

	def switch_page(self, page_name):
		js = '''var alist = document.getElementsByTagName('li')
					for (var i=0, a; a=alist[i++];){
						if(a.innerText == "%s")
							a.click()
					}
			''' % page_name
		self.page_obj.browser_obj.js_executor.execute_script(js)

	def check_data_from_table(self, src_data, src_thead, table, index, tableType = '001'):
		theads = table.theads
		tdatas = table.get_by(index, tableType)
		for k, v in src_thead.items():
			for index, thead in enumerate(theads):
				if cmp(thead, v) == 0:
					if hasattr(src_data, k):
						if tdatas[index] != getattr(src_data, k):
							print (self.page_obj.browser_obj.snapshot("", ""))
							raise Exception("表格字段校验错误，错误字段为[%s]:错误数据为(%s) 期望数据为(%s)"
							                % (thead, tdatas[index], getattr(src_data, k)))
					break
	def check_str_from_table(self, cmp_str, src_data, src_thead, table, index, tableType = '001'):
		theads = table.theads
		tdatas = table.get_by(index, tableType)
		for k, v in src_thead.items():
			for index, thead in enumerate(theads):
				if cmp(thead, v) == 0:
					if hasattr(src_data, k):
						if cmp_str in tdatas[index]:
							pass
						else:
							print (self.page_obj.browser_obj.snapshot("", ""))
							raise Exception("表格字段模糊匹配错误，期望字段数据 %s 未包含在 %s (实际字段数据中)"
							                % (cmp_str, tdatas[index]))
					break
	def check_str_not_from_table(self, cmp_str, src_data, src_thead, table, index):
		theads = table.theads
		tdatas = table.get_by(index)
		for k, v in src_thead.items():
			for index, thead in enumerate(theads):
				if cmp(thead, v) == 0:
					if hasattr(src_data, k):
						if cmp_str not in tdatas[index]:
							pass
						else:
							raise AssertionError( "%s is in %s" % (cmp_str, tdatas[index]))
					break

	def cmp_date_not_from_table(self, startDate, endDate, src_thead, table, index):
		theads = table.theads
		tdatas = table.get_by(index)
		for k, v in src_thead.items():
			for index, thead in enumerate(theads):
				if cmp(thead, v) == 0:
					if thead == u'开始时间':
						if tdatas[index] <= endDate:
							pass
						else:
							raise AssertionError("StartDate is out of range: %s, Queryinfo is %s" % (tdatas[index], endDate))
					if thead == u'结束时间':
						if tdatas[index] >= startDate:
							pass
						else:
							raise AssertionError("EndDate is out of range: %s, Queryinfo is %s" % (tdatas[index], startDate))
					break

	def login(self, username=''):
		page = PageFactory(self.page_obj.browser_obj, loginPage)
		if username == 'root':
			page.elements.mobile.value = SetupInfo.mobile
			page.elements.password.value = SetupInfo.password
			page.elements.submit.click()
			page.positionForm.elements.radioGroup.value = SetupInfo.version
			page.positionForm.elements.submitBtn.click()
		else:
			page.elements.mobile.value = SetupInfo.user.mobile
			page.elements.password.value = SetupInfo.user.password
			page.elements.submit.click()
			page.positionForm.elements.radioGroup.value = SetupInfo.version
			page.positionForm.elements.submitBtn.click()
		try:
			page.browser_obj.click_the_clickable(page.positionForm.elements.submitBtn.xpath,time.time(),2)
			page.browser_obj.expect_url_content('/#/', time.time(), 30)
		except:
			page.browser_obj.expect_url_content('/#/', time.time(), 30)

	def check_is_login(self,username):
		if "/#/login" in self.page_obj.browser_obj.current_url:
			return self.login(username)
		return True

	def equal(self, actual,expect, msg):
		if not actual == expect:
			print (self.page_obj.browser_obj.snapshot("", ""))
			raise Exception(msg or "期望结果为: [%s]; 实际结果为: [%s]"
			                % (actual, expect))

	def init_test_data(self, module_name):
		pass

	def getTimestamp(self):
		return str(time.time()).replace('.','0')