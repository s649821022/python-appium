# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 4:39
# @File     ：baseView.py
# @Software : PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class BaseView(object):
    def __init__(self, driver, logger):
        # 初始化driver和logger
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 10)

    # 判断元素是否存在，不代表该元素一定可见，返回对象
    def eleIsPresence(self, eleTuple):
        try:
            element = self.wait.until(EC.presence_of_element_located(eleTuple))
            return element
        except:
            self.logger.error('未找到元素：%s' % eleTuple)

    # 判断是否至少有一个元素被定位到，如果有则返回列表
    def elesIsPresence(self, eleTuple):
        try:
            elementList = self.wait.until(EC.presence_of_all_elements_located(eleTuple))
            return elementList
        except:
            self.logger.error('未找到元素：%s' % eleTuple)

    # 判断文本内容text是否出现在某个元素中（判断的是元素的text值）,返回布尔值
    def text_in_element_text(self, eleTuple, text):
        try:
            result = self.wait.until(EC.text_to_be_present_in_element(eleTuple, text))
            return result
        except:
            self.logger.error(u'未找到元素：%s' % eleTuple)

    # 判断text是否出现在元素的value属性值中，返回布尔值
    def text_in_element_value(self, eleTuple, text):
        try:
            result = self.wait.until(EC.text_to_be_present_in_element_value(eleTuple, text))
            return result
        except:
            self.logger.error(u'未找到元素：%s' % eleTuple)

    # 判断页面title标签内容是否包含partial_title,返回布尔值
    def partial_title_in_title(self, partial_title):
        try:
            result = self.wait.until(EC.title_contains(partial_title))
            return result
        except:
            self.logger.error(u'title中不包含 %s' % partial_title)

    # 判断title内容与传参是否完全匹配
    def title_text_is_driver_title(self, title_text):
        try:
            result = self.wait.until(EC.title_is(title_text))
            return result
        except:
            self.logger.error(u'title与 %s 不匹配' % title_text)

    # 判断单个元素是否可见（存在且可见）
    def element_is_visibility(self, eleTuple):
        try:
            element = self.wait.until(EC.visibility_of_element_located(eleTuple))
            return element
        except:
            self.logger.error(u'未找到元素：%s' % eleTuple)

    # 判断是否至少有一个元素可见，如果定位到就返回列表
    def elements_is_visibility(self, eleTuple):
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(eleTuple))
            return elements
        except:
            self.logger.error(u'%s元素不可见' % eleTuple)

    # 元素不可见
    def element_isnot_visibility(self, eleTuple):
        try:
            elements = self.wait.until(EC.invisibility_of_element_located(eleTuple))
            return elements
        except:
            self.logger.error(u'%s元素依然可见' % eleTuple)

    """
        判断frame是否可用，如果可用返回True，并切入到frame中，如果返回false，则不可用
        参数parm可以是：
        1)xpath定位元组（by, xpath）
        2)也可以是id,name,index(By.ID, 'xxx')或1
        3)WebElement对象 driver.find_element_by_id('xxx')
    """
    def switch_to_frame(self, parm):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(parm))
        except:
            self.src.screenshot()
            self.logger.error(u'%s元素依然可见' % parm)

    # 切换到默认窗体
    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    # 判断某个元素是否可见且是enable的，代表可点击
    def click(self, eleTuple):
        try:
            self.element_is_visibility(eleTuple).click()
        except:
            self.logger.error(u'%s元素不可见或不能点击' % eleTuple)

    # 判断某个元素是否可见切是enable的，代表可发送文本
    def send_keys(self, eleTuple, text):
        try:
            element = self.element_is_visibility(eleTuple)
            # element.clear()
            element.send_keys(text)
        except AttributeError:
            self.logger.error(u'未找到元素：%s 或元素不可输入文本' % eleTuple)

    # 判断某个元素是否被园中了，一般用在下拉列表
    def element_is_selected(self, element):
        try:
            self.wait.until(EC.element_located_to_be_selected(element))
        except:
            self.logger.error(u'%s未选中' % element)

    # 判断页面上是否存在alert，如果有就切换到alert并返回alert的内容
    def element_is_alert(self):
        try:
            instance = self.wait.until(EC.alert_is_present())
            print(instance.text)
            instance.accept()
        except:
            self.logger.error(u'未存在alert')

    # 选择下拉列表的下标
    def select_index(self, eleTuple, number):
        try:
            options = self.element_is_visibility(eleTuple)
            self.select = Select(options)
            self.select.select_by_index(number)
        except:
            self.logger.error('没有找到这个选项')

if __name__ == '__main__':
    driver, logger = appium_desired()
    BaseView(driver, logger).eleIsPresence((By.ID, 'com.ss.android.article.lite:id/yk')).click()

