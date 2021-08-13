from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from Initpage import Initpage # 页面的数据
from LoginPage import LoginPage # 页面的操作逻辑
import  time
@ddt
class TestLogin(TestCase):
    # 在每个操作之前先做预备工作
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(2)

    # 在每个用例执行后，将浏览器关闭
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    #登陆成功用例
    @data(*Initpage.login1_teacher_data)
    def testlogin1Teacher(self, testdata):
        loginname = testdata["loginname"]
        password = testdata["password"]
        expect = testdata["expect"]

        login1 = LoginPage(self.driver)
        login1.login1(loginname, password)

        result = login1.get_teacher_data()

        self.assertEqual(expect, result)

    @data(*Initpage.login1_teacher_x_data)
    def testlogin1Teacher_x(self, testdata):
        loginname = testdata["loginname"]
        password = testdata["password"]
        expect = testdata["expect"]

        login1 = LoginPage(self.driver)
        login1.login1(loginname, password)

        resule = login1.get_teacher_x_data()

        self.assertEqual(expect, resule)


    @data(*Initpage.login_success_data)
    def testLoginsuccess(self,testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginPage(self.driver)
        login.login(username,password)

        #  获取实际结果
        result = login.get_succes_data()

        # 断言
        self.assertEqual(expect,result)


    @data(*Initpage.login_pwd_error_data)
    def testLoginerror(self, testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginPage(self.driver)
        login.login(username, password)

        #  获取实际结果
        result = login.get_error_data()
        # 断言
        self.assertEqual(expect, result)

    # @data(*Initpage.login1_teacher_data)
    # def TestLogin1Teacher(self,testdata):
    #     loginname = testdata["loginname"]
    #     password = testdata["password"]
    #     expect = testdata["expect"]
    #
    #     login1 = LoginPage(self.driver)
    #     login1.login1(loginname,password)
    #
    #     result = login1.get_teacher_data()
    #
    #     self.assertEqual(expect,result)
    #
    # @data(*Initpage.login1_teacher_x_data)
    # def TestLogin1Teacher_x(self,testdata):
    #     loginname = testdata["loginname"]
    #     password = testdata["password"]
    #     expect = testdata["expect"]
    #
    #     login1 = LoginPage(self.driver)
    #     login1.login1(loginname,password)
    #
    #     resule = login1.get_teacher_x_data()
    #
    #     self.assertEqual(expect,resule)












