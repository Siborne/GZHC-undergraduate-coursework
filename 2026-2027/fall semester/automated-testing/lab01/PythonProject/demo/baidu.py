"""
=======================
Author：Siborne
Time:2026/9/2 9:2
Project:demo
========================
"""
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置驱动
driver_path = r"D:\Siborne\automated-testing\lab01\PythonProject\resource\chromedriver.exe"
service = Service(executable_path=driver_path)
# 启动浏览器
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    driver.get("https://www.baidu.com/")
    print("正在打开百度首页...")

    time.sleep(3)

    print("正在定位收索框...")
    input_box = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"chat-textarea"))
    )

    input_box.clear()
    input_box.send_keys("selenium")
    print("已输入关键词:selenium")

    print("正在定位搜索按钮...")
    search_button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"chat-submit-button"))
    )

    search_button.click()
    print("已点击搜索按钮，正在等待搜索结果...")
    sleep(20)

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'result')]"))
    )

    current_title = driver.title
    print(f"搜索完成，当前页面标题：{current_title}")

    time.sleep(3)

    print("测试执行成功！")

except Exception as e:
    print(f"测试执行出错：{str(e)}")

finally:
    print("正在关闭浏览器")
    driver.quit()
    print("浏览器已关闭")
