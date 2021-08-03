import smtplib
from email.header import Header
from email.mime.text import MIMEText






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