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

network = driver.find_element_by_xpath("//*[@text ='Network & internet']")
print('clickable:' + network.get_attribute('clickable'))
