"""
=======================
Author：Siborne
Time:2026/9/2 9:2
Project:demo
========================
"""
# 导包
from selenium import webdriver
from time import sleep

# 创建浏览器驱动对象
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com/")

# 浏览器窗口最大化
driver.maximize_window()

# 休眠2s
sleep(2)

# 关闭窗口
driver.quit()
