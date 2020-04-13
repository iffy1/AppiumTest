import os
import time
from appium import webdriver

# 定位方式 	By
# id 	By.ID
# name 	By.NAME
# class_name 	By.CLASS_NAME
# tag_name 	By.TAG_NAME
# link_text 	By.LINK_TEXT
# partial_link_text 	By.PARTIAL_LINK_TEXT
# css_selector 	By.CSS_SELECTOR
# xpath 	By.XPATH
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = '0.0.0.0:4723'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 隐式等待
# 10秒只能找到aa就会直接执行，不会等到10秒
# 10秒还没知道会抛异常
# 会影响后续所有find_element方法
driver.implicitly_wait(10)

driver.find_element_by_name('aa')
driver.find_element_by_name('bb')


# 隐式等待
print("开始显式查找")
# 显式等待，超时时间 5秒
# 默认每0.5秒调用一次 找到马上返回，不会等到5秒
wait = WebDriverWait(driver, 5)
btn_cc = wait.until(lambda x: x.find_element_by_xpath("//*[@text ='iffy']"), '没找到')
print(btn_cc.text)

# 25秒超时 每5秒找1次
WebDriverWait(driver, 25, 5).until(lambda x: x.find_element_by_xpath("//*[@text ='iffy']"), '没找到').click()

# 显式等待
