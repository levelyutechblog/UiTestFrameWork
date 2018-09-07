# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import time, os

def send_mail(file_new):

        smtpserver = ''
        user = ''
        password = ''
        sender = ''
        receiver = ''
        subject = ''
        msg = MIMEText('<html><h4>Python自动化测试报告</h4></html>', 'html', 'utf-8')

        sendfile = open(file_new, 'rb').read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename="TestReport.html"'

        masRoot = MIMEMultipart('related')
        masRoot['Subject'] = subject
        masRoot['To'] = Header("", 'utf-8')
        masRoot['From'] = Header("", 'utf-8')
        masRoot.attach(msg)
        masRoot.attach(att)

        State = True
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, masRoot.as_string())
            smtp.quit()
        except Exception as masg:
            print(masg)
            State = False

        if State:
            print('Email send out successfully!')
        else:
            print('Email send out failed')

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

