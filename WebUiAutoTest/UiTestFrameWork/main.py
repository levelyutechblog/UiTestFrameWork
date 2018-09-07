# -*- coding: utf-8 -*-
import nose
from nose.loader import defaultTestLoader
import os, time
from nose.plugins.plugintest import run_buffered as run
from testcase._setup import custom_setup as browser_setup
from data._setup import custom_setup as data_setup
from util.mail import *
import sys, HTMLTestRunner, unittest

reload(sys)
sys.setdefaultencoding('utf8')

def setup_module():
	# setup_module before anything in this file
	browser_setup()
	data_setup()

def teardown_module():
	# teardown_module after everything in this file
	pass

if __name__ == '__main__':

	setup_module()
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = 'report/' + now + '_UiTestResult.html'

	dis = nose.loader.defaultTestLoader()
	case = dis.discover('testcase/', pattern='test_*.py')
	fp = open(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
							title ='Ui自动化测试报告',
							description ='用例执行情况：',
							tester ='')
	runner.run(case)
	fp.close()





