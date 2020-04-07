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
desired_caps['appPackage'] = 'com.google.android.apps.messaging'
desired_caps['appActivity'] = '.ui.ConversationListActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(1)

# 点击新建
driver.find_element_by_id('start_new_conversation_button').click()
time.sleep(1)
# 默认打开msg app
# 打开设置APP
driver.start_activity('com.android.settings', '.Settings')

time.sleep(1)
print('当前的界面为' + driver.current_activity)
print('当前的包名为' + driver.current_package)

# 返回 msg app
driver.back()

time.sleep(1)

# 关闭msg app
driver.close_app()

# 判断应用是否安装 安装就卸载 没安装就安装
if driver.is_app_installed("com.iffy.activitytime"):
    print('remove app')
    driver.remove_app("com.iffy.activitytime")
else:
    print('install app from:' + os.path.abspath('.') + '\\apk\com.iffy.activitytime.apk')
    driver.install_app(os.path.abspath('.') + '\\apk\com.iffy.activitytime.apk')

# 启动msg
driver.start_activity('com.google.android.apps.messaging', '.ui.ConversationListActivity')

# msg app放置到后台3s后返回前台
driver.background_app(3)

if driver.wait_activity('.ui.ConversationListActivity', 1, 1):
    print("1秒内打开了activity")
else:
    print("打开页面超时 失败")

driver.quit()
