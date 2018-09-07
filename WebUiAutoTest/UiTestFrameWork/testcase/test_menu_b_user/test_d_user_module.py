# -*- coding: utf-8 -*-
from dagger.browser_emulator import BrowserEmulator
from dagger.common import GloableSettings as gs
from dagger.page import PageFactory
from testcase._setup import be
from custom_page.extensions import Extensions
from nose.tools import *
from custom_page.pUser import userPage
from custom_page.pAccount import accountPage
from data import test_user as tu
from data._setup import init_data_by_script
import time
from config import SetupInfo

def setup_module(module):
    # setup_module before anything in this file
    pass

def teardown_module(module):
    # teardown_module after everything in this file
    pass

class TestUserModule:

    def setup(self):
        # setup() before each test method
        init_data_by_script("USER_INIT")
        self.page.browser_obj.refresh()

    def teardown(self):
        # teardown() after each test method
        log = self.page.browser_obj.snapshot("", "")
        print log

    @classmethod
    def setup_class(cls):

        cls.page = PageFactory(be, userPage, Extensions)
        cls.page.extensions.check_is_login(tu.login_user)
        cls.page.browser_obj.maximize_window()
        cls.page.browser_obj.expect_element_visibleOrNot(False, cls.page.not_visable, 5)
        moduleStatus = cls.page.browser_obj.get_element(cls.page.elements.moduleStatus)
        cls.page.browser_obj.logger.info(moduleStatus.get_attribute('class'))
        if 'is-opened' not in moduleStatus.get_attribute('class'):
            cls.page.elements.moduleList.value = cls.page.elements.module_name

        cls.page.elements.menuList.value = cls.page.page_name.lstrip()
        cls.page.browser_obj.expect_element_visibleOrNot(False, cls.page.not_visable, 5)

    @classmethod
    def teardown_class(cls):
        init_data_by_script('DATA_CLEAR')

    def test_a_user_add(self):

        page = self.page
        data = tu.test_user_add
        tb1 = page.elements.userTable

        numbers_before_add = tb1.numbers
        page.elements.addBtn.click()
        page.addForm.elements.userName.value        = data.userName
        page.addForm.elements.mobilePhone.value     = data.mobilePhone
        page.addForm.elements.saleAreaName.click()
        page.addForm.elements.saleAreaName.value    = data.saleAreaNameAdd
        page.addForm.elements.mainPost.click()
        page.addForm.elements.mainPost.value        = data.mainPost
        page.addForm.elements.workCode.value        = data.workcode
        page.addForm.elements.sex.click()
        page.addForm.elements.sex.value             = data.sex
        page.addForm.elements.entryDate.click()
        page.addForm.elements.entryDate.value       = data.entryDate
        page.addForm.elements.shortCode.value       = data.shortCode
        page.addForm.elements.email.value           = data.email
        page.addForm.elements.idcard.value          = data.idcard
        page.addForm.elements.QQ.value              = data.QQ
        page.addForm.elements.tel.value             = data.tel
        page.addForm.elements.address.value         = data.address
        page.addForm.elements.weChat.value          = data.weChat
        page.addForm.elements.remark.value          = data.remark
        page.addForm.elements.ifGenAccount.value    = data.ifGenAccount
        page.addForm.elements.saveBtn.click()

        alertInfo = page.elements.actionAlert.text.encode("utf-8")
        page.extensions.equal(alertInfo,data.saveInfo.encode("utf-8"),
                              " :%s :%s"
                              % (alertInfo, data.saveInfo.encode("utf-8")))
        page.browser_obj.expect_element_visibleOrNot(False, page.not_visable, 5)

        numbers_after_add = str(int(tb1.numbers) -1 )
        page.extensions.equal(numbers_after_add, numbers_before_add ,
                              "，:%s :%s"
                              %(str(int(numbers_after_add)+1), numbers_before_add ))

        page.extensions.check_data_from_table(data, tu.thead, tb1, 1)