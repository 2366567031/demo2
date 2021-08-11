from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"C:\Users\车志阳\PycharmProjects\pythonProject\jiekou\day01\任务\练习的html\跳转页面\pop.html")
driver.maximize_window()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(1)
data = driver.window_handles[-1]
driver.switch_to.window(data)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='kw']").send_keys("周杰伦")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(3)
driver.quit()







