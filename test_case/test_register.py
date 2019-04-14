# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 6:50
# @File     ：test_register.py
# @Software : PyCharm

from businessView.registerView import RegisterView
from common.desired_caps import appium_desired
from common.myunit import StartEnd
from time import sleep

class TestRegister(StartEnd):
    def testRegister(self):
        register = RegisterView(self.driver, self.logger)
        register.register_action('123231213', '5677')
        sleep(2)



