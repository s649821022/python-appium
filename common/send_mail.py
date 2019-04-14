# -*- coding:utf-8 -*-
# @Author   ：kobe
# @time     ：13/4/2019 下午 7:09
# @File     ：send_mail.py
# @Software : PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time

def sendMail(report_file):
    # 发送纯文本格式的邮件
    # msg = MIMEText('hello, send by python_test....', 'plain', 'utf-8')
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    file = open(report_file, 'rb').read()
    att1 = MIMEText(file, _charset='utf-8')
    att1['Content-Type'] = 'application/octet-stream'  # 二进制流数据
    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名
    att1["Content-Disposition"] = 'attachment; filename="test_report.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)

    # 发送邮箱地址
    sender = '13341775681@163.com'
    # 邮箱授权码，非登陆密码
    password = '147174as'
    # 收件箱地址
    receiver = ['1044500650@qq.com']
    # smtp服务器
    smtp_server = 'smtp.163.com'
    # 发送邮箱地址
    msg['From'] = sender
    # 收件箱地址
    msg['To'] = '.'.join(receiver)
    # 主题
    msg['Subject'] = '今日头条自动化测试结果-' + time.strftime("%Y-%m-%d %H_%M_%S")
    server = smtplib.SMTP(smtp_server, 25)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

