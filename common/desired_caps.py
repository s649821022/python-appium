# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 1:21
# @File     ：desired_caps.py
# @Software : PyCharm

from appium import webdriver
from time import sleep
import logging
import logging.config
import os
import yaml

def appium_desired():
    configPath = os.path.dirname(os.path.dirname(__file__)) + '/config/logger.ini'
    yamlFile = os.path.dirname(os.path.dirname(__file__)) + '/config/desired_caps.yaml'
    configFile = open(configPath, encoding='utf-8')
    logging.config.fileConfig(configFile)
    logger = logging.getLogger('infoLogger')
    with open(yamlFile, 'r', encoding='utf-8') as path:
        data = yaml.load(path)

    caps = {}
    caps['platformName'] = data['platformName']
    caps['platformVersion'] = data['platformVersion']
    caps['deviceName'] = data['deviceName']
    caps['appPackage'] = data['appPackage']
    caps['appActivity'] = data['appActivity']
    caps['unicodeKeyboard'] = data['unicodeKeyboard']
    caps['resetKeyboard'] = data['resetKeyboard']
    caps['noReset'] = data['noReset']

    driver = webdriver.Remote('http://'+str(data["ip"])+":"+str(data["port"])+"/wd/hub", caps)
    logger.info('初始化设置')
    return driver, logger

if __name__ == '__main__':
    driver, logger = appium_desired()
    logger.info('123')
