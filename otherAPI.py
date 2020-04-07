import os
import time

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = '0.0.0.0:4723'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 获取分辨率 {'width': 1080, 'height': 1794}
print(driver.get_window_size())

# 420
print(driver.get_display_density())

# 截图
driver.get_screenshot_as_file(os.path.abspath("a.png"))

# 获取网络模式
"""
Possible
values:
Value(Alias) | Data | Wifi | Airplane
0(None)           | 0 | 0 | 0
1(AirplaneMode)   | 0 | 0 | 1
2(Wifionly)       | 0 | 1 | 0
4(Dataonly)       | 1 | 0 | 0
6(All network on) | 1 | 1 | 0
"""
print(driver.network_connection)
# 设置飞行模式
# driver.set_network_connection(4)
# driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
try:
    driver.set_network_connection(1)
except Exception as e:
    print("截获异常"+e.args[0])

print(driver.network_connection)

# 模拟按键
# 音量+
driver.press_keycode(keycode=24)
# 音量-
driver.press_keycode(keycode=24)
# home
driver.press_keycode(keycode=3)

# 操作通知栏
driver.open_notifications()
time.sleep(2)
# 返回键
driver.press_keycode(keycode=4)

