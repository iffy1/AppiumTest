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
from appium.webdriver.common.touch_action import TouchAction

def set_pattern_psw():
    print('画正方形')
    TouchAction(driver).press(x=100, y=100)\
        .move_to(x=100, y=200)\
        .move_to(x=200, y=200)\
        .move_to(x=200, y=100)\
        .move_to(x=100, y=100)\
        .perform()

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = '0.0.0.0:4723'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 找到wlan按钮
wlan_btn = driver.find_element_by_xpath("//*[@text ='Network & internet']")
# 创建touch action对象
ta = TouchAction(driver)
# 想要执行的动作
ta = ta.tap(wlan_btn)
# 执行
ta.perform()

# 简写
# TouchAction(driver).tap(wlan_btn).perform()

TouchAction(driver).tap(x=100, y=100).perform()

# count 多次点击
TouchAction(driver).tap(x=100, y=100, count=10).perform()

# 按下 抬起
TouchAction(driver).press(x=100, y=100).perform()
TouchAction(driver).press(x=100, y=100).release().perform()

# 按下后等待
TouchAction(driver).press(x=500, y=600).press().wait(100).release().perform()

# 长按
TouchAction(driver).long_press(x=500, y=600, duration=2000).release().perform()

set_pattern_psw()