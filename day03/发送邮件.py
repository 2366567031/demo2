# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
#
#
#
#
#
#
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
# message = MIMEText("我是一条邮件信息", 'plain', 'utf-8')
# message['From'] = Header("Python邮件系统", 'utf-8')
# message['To'] = Header("管理员", 'utf-8')
# subject = "Python SMTP 邮件测试"
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtp.sendmail(from_addr, to_addr, message.as_string())
# except Exception as e:
#     print("邮件发送失败" + str(e))
# else:
#     print("邮件发送成功")
# finally:
#     pass



# 4.实现邮件发送
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

sender = '2366567031@qq.com'  # 发件人邮箱账号
my_pass = 'ttnugyzuaeyndibe'  # 发件人邮箱授权码
user = '2431320433@qq.com'  # 收件人邮箱账号


msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["良辰i", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题
# 发件人邮箱中的SMTP服务器，SMTP端口是465
server = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 括号中对应的是发件人邮箱账号、邮箱密码
server.login(sender, my_pass)
# 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att = MIMEText(open(r'C:\Users\车志阳\PycharmProjects\pythonProject\jiekou\day03\登陆测试报告.html', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=登陆测试报告.html"  # filename为文件名字
msg.attach(att)

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")



































