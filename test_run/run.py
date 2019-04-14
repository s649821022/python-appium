# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 7:08
# @File     ：run.py
# @Software : PyCharm

import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from common.common_method import CommonMethod
import time
from common.send_mail import sendMail
import os

now = time.strftime("%Y-%m-%d %H_%M_%S")

path = os.path.dirname(os.path.dirname(__file__))
case_path = path+'/test_case'
report_path = path+'/reports/'

# discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
report_file = report_path+now+' test_report.html'

if __name__=="__main__":
	# unittest.TextTestRunner().run(discover)
	with open(report_file,'wb') as f:
		runner = HTMLTestRunner(stream=f, title="测试报告", description='测试用例执行结果')
		runner.run(discover)

	sendMail(report_file)

