from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一个HKR的测试报告",
    description="这是一个详细登陆的测试报告",
    verbosity=1,
    stream = open(file="登陆测试报告.html",mode="w+",encoding="utf-8")
)


runner.run(tests)


# 邮件发送代码
# 报告发送
# 截图当成附件发送过去












