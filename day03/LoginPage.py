'''
    就写登陆的页面的操作逻辑：


'''
import time
class LoginPage:
    def __init__(self,drive):
        self.driver = drive  # 将driver生命为全局变量



    def login1(self,loginname,password):
        #点击教师登录
        self.driver.find_element_by_link_text("教师登录").click()
        #输入用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(loginname)
        time.sleep(1)
        #输入密码
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(1)
        #点击登录
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    def get_teacher_data(self):
        return self.driver.title

    def get_teacher_x_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text



    def login(self,username,password):
        # 输入用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        # 点击登陆
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    def get_succes_data(self):
        return self.driver.title

    def get_error_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text




