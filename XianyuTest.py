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
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = '0.0.0.0:4723'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage'] = 'com.taobao.idlefish'
# desired_caps['appActivity'] = 'com.taobao.fleamarket.home.activity.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.start_activity('com.taobao.idlefish', 'com.taobao.fleamarket.home.activity.MainActivity')

# 点击我的
driver.find_element_by_xpath("//*[@content-desc='我的，未选中状态']").click()

time.sleep(1)

# 点击我发布的 模糊查找
driver.find_element_by_xpath("//*[contains(@text,'我发布的')]").click()

# 查找擦亮按钮
for i in range(1, 50):
    # 查找所有擦亮按钮
    caliang_btns = driver.find_elements_by_xpath("//*[@content-desc='擦亮']")
    for btn in caliang_btns:
        btn.click()

    # 拖到一键转卖说明到底了
    zhuanmai_btn = 0
    try:
        zhuanmai_btn = driver.find_element_by_xpath("//*[@content-desc='一键转卖']")
    except:
        print('没找到一键转卖')

    if zhuanmai_btn:
        print('发现转卖，结束下滑')
        break

    # 滑动 单位是像素
    driver.swipe(10, 600, 10, 20, 500)
