# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 3:46
# @File     ：registerView.py
# @Software : PyCharm

from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
from common.common_method import CommonMethod

class RegisterView(CommonMethod):
    noLogin = (By.XPATH, '//android.widget.TextView[@text="未登录"]')
    enterLogin = (By.ID, 'com.ss.android.article.lite:id/a5r')
    registerButton = (By.ID, 'com.ss.android.article.lite:id/f0')
    telephoneButton = (By.ID, 'com.ss.android.article.lite:id/f3')
    codeButton = (By.ID, 'com.ss.android.article.lite:id/f7')
    clickRegister = (By.ID, 'com.ss.android.article.lite:id/fa')

    def register_action(self, telephone, code):
        # 确认是否有红包按钮
        self.checkRedPacket()

        # 点击未登录按钮
        self.click(self.noLogin)

        # 点击进入登录按钮的按钮
        self.click(self.enterLogin)

        # 点击注册按钮
        self.click(self.registerButton)

        # 输入手机号
        self.send_keys(self.telephoneButton, telephone)

        # 输入验证码
        self.send_keys(self.codeButton, code)

        # 点击注册
        self.click(self.clickRegister)

if __name__ == '__main__':
    driver, logger = appium_desired()
    a = RegisterView(driver, logger)
    a.register_action('12331223123', '1232155')
