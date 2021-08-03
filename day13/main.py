'''
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
'''
from HTMLTestRunner import HTMLTestRunner  # 运行器
import unittest
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\车志阳\PycharmProjects\pythonProject\czy\day13",pattern="test*.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份计算器的测试报告",
    description="这只是加减乘除运算的测试报告",
    verbosity=1,
    stream= open("计算器.html",mode="w+",encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)


# 4.实现邮件发送
from_addr = "2366567031@qq.com"  # 邮件发送账号
to_addr = "2366567031@qq.com"
qqCode = "ttnugyzuaeyndibe"  # qq邮箱的授权码 POP3/SMTP
smtp_server = "smtp.qq.com"  # 固定写死
smtp_port = 465  # 端口号 固定写死

# ===配置服务器
smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
smtp.login(from_addr, qqCode)

# ====组装发送内容
message = MIMEText("我是一条邮件信息", 'plain', 'utf-8')
message['From'] = Header("Python邮件系统", 'utf-8')
message['To'] = Header("管理员", 'utf-8')
subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
 smtp.sendmail(from_addr, to_addr, message.as_string())
except Exception as e:
 print("邮件发送失败" + str(e))
else:
 print("邮件发送成功")
finally:
 pass





