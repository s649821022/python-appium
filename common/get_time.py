# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 上午 9:41
# @File     ：get_time.py
# @Software : PyCharm

import time

class GetTime(object):

    def getCurrentDate(self):
        date = time.strftime('%Y-%m-%d')  # 当前日期格式为：2019-4-13
        return date

    def getCurrentTime(self):
        now = time.strftime('%H_%M_%S')  # 当前时间格式为：09_45_23
        return now

    def getCurrentDateTime(self):
        dateTime = time.strftime('%Y-%m-%d %H_%M_%S')  # 当前完整时间格式为：2019-4-13 09_45_23
        return dateTime

    def getTimeStamp(self):
        timeStamp = int(time.time() * 1000)  # 获取时间戳
        return timeStamp

if __name__ == '__main__':

    times = GetTime()
    print(times.getTimeStamp())
