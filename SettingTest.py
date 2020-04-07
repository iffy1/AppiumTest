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


desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = '0.0.0.0:4723'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Case 打开设置 输入搜索"hello" 点击返回

# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search_action_bar_title").click()
time.sleep(1)

# 搜索框输入hello
driver.find_element_by_class_name('android.widget.EditText').send_keys('hello')
time.sleep(1)

# 点击返回按钮
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(1)

# 点击wifi列 使用xpath
driver.find_element_by_xpath("//*[@text ='Network & internet']").click()

time.sleep(2)
