# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 上午 10:44
# @File     ：common_method.py
# @Software : PyCharm


from appium.webdriver.common.touch_action import TouchAction
from common.desired_caps import appium_desired
from common.get_time import GetTime
from selenium.webdriver.common.by import By
from time import sleep
import os
from baseView.baseView import BaseView

class CommonMethod(BaseView):
    getTime = GetTime()
    redPacket = (By.ID, 'com.ss.android.article.lite:id/yk')
    touchAction = TouchAction()

    def checkRedPacket(self):
        try:
            redPacket = self.eleIsPresence(self.redPacket)
        except:
            self.logger.info('没有红包按钮')
        else:
            redPacket.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 左滑
    def swipeLeft(self):
        size = self.get_size()
        x1 = int(size[0] * 0.9)
        y = int(size[1] * 0.5)
        x2 = int(size[0] * 0.2)
        self.driver.swipe(x1, y, x2, y, 1000)

    # 右滑
    def swipeRight(self):
        size = self.get_size()
        x1 = int(size[0] * 0.2)
        y = int(size[1] * 0.5)
        x2 = int(size[0] * 0.9)
        self.driver.swipe(x1, y, x2, y, 1000)

    # 上滑
    def swipeUp(self):
        size = self.get_size()
        x = int(size[0] * 0.5)
        y1 = int(size[1] * 0.9)
        y2 = int(size[1] * 0.2)
        self.driver.swipe(x, y1, x, y2, 1000)

    # 下滑
    def swipeDown(self):
        size = self.get_size()
        x = int(size[0] * 0.5)
        y1 = int(size[1] * 0.2)
        y2 = int(size[1] * 0.9)
        self.driver.swipe(x, y1, x, y2, 1000)

    # 按压 默认按压一秒
    def press_ele(self, eleTuple, s=1000):
        try:
            ele = self.eleIsPresence(eleTuple)
            self.touchAction.press(el=ele).wait(s).release().perform()
        except:
            self.logger.error('未找到元素:%s 无法按压' % eleTuple)
    def press_coordinate(self, x, y, s=1000):
        try:
            self.touchAction.press(x=x, y=y).wait(s).release().perform()
        except:
            self.logger.error('按压失败')

    # 长按
    def long_press_ele(self, eleTuple, duration=1000):
        try:
            ele = self.eleIsPresence(eleTuple)
            self.touchAction.long_press(el=ele,duration=duration).release().perform()
        except:
            self.logger.error('未找到元素:%s 长按失败' % eleTuple)
    def long_press_coordinate(self, x, y, duration=1000):
        try:
            self.touchAction.long_press(x=x, y=y, duration=duration).release().perform()
        except:
            self.logger.error('长按失败')

    def getScreenShot(self, text):
        dateTime = self.getTime.getCurrentDateTime()
        image_path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (text, dateTime)
        try:
            self.driver.get_screenshot_as_file(image_path)
        except:
            self.logger.error('截图失败')

if __name__ == '__main__':
    driver, logger = appium_desired()
    a = CommonMethod(driver, logger)
    driver.find_element_by_xpath('//android.widget.TextView[@text="未登录"]').click()
    sleep(2)
    a.swipeDown()
