'''
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
'''
from HTMLTestRunner import HTMLTestRunner  # 运行器
from email.mime.multipart import MIMEMultipart
import unittest
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\车志阳\PycharmProjects\pythonProject\czy\day15",pattern="Test*.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份工商银行测试报告",
    description="",
    verbosity=1,
    stream= open("ICBCBank.html", mode="w+", encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)


# 4.实现邮件发送
# from_addr = "2366567031@qq.com"  # 邮件发送账号
# to_addr = "2366567031@qq.com"
# qqCode = "ttnugyzuaeyndibe"  # qq邮箱的授权码 POP3/SMTP
# smtp_server = "smtp.qq.com"  # 固定写死
# smtp_port = 465  # 端口号 固定写死
#
# # ===配置服务器
# smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
# smtp.login(from_addr, qqCode)
#
# # ====组装发送内容
# msg = MIMEMultipart()
# message = MIMEText("我是一条邮件信息", 'plain', 'utf-8')
# message['From'] = Header("Python邮件系统", 'utf-8')
# message['To'] = Header("管理员", 'utf-8')
# subject = "Python SMTP 邮件测试"
# message['Subject'] = Header(subject, 'utf-8')
#
# # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
# att = MIMEText(open(r"C:\Users\车志阳\PycharmProjects\pythonProject\czy\day13\计算器.html", "rb").read(), "base64", "utf-8")
# att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = "attachment; filename=case.html"  # filename为文件名字
# msg.attach(att)
#
# try:
#  smtp.sendmail(from_addr, to_addr, message.as_string())
# except Exception as e:
#  print("邮件发送失败" + str(e))
# else:
#  print("邮件发送成功")
# finally:
#  pass



# 4.实现邮件发送
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

sender = '2366567031@qq.com'  # 发件人邮箱账号
my_pass = 'ttnugyzuaeyndibe'  # 发件人邮箱授权码
user = '2431320433@qq.com'  # 收件人邮箱账号


msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["车志阳", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["贾经理", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题
# 发件人邮箱中的SMTP服务器，SMTP端口是465
server = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 括号中对应的是发件人邮箱账号、邮箱密码
server.login(sender, my_pass)
# 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att = MIMEText(open(r'C:\Users\车志阳\PycharmProjects\pythonProject\czy\day15\ICBCBank.txt', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=icbc.html"  # filename为文件名字
msg.attach(att)

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")

