"""
=======================
Author：张梦娟
Time:2026/2/20 10:23
Project:test
========================
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestForAssert(unittest.TestCase):
    def setUp(self):
        """每个测试方法执行前启动浏览器，并注册清理"""
        self.driver = webdriver.Chrome()          # 确保 chromedriver 在 PATH 中
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.addCleanup(self.driver.quit)         # 测试结束后自动关闭浏览器
    def testSina(self):
        driver = webdriver.Chrome()
        # r"D:\Python36\chromedriver.exe"
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(r"file:///D:/注册A.html")
        # 打开测试网站
        # driver.maximize_window()
        element = driver.find_element(by=By.ID, value="userA").send_keys("admin")
        driver.find_element(by=By.ID, value="passwordA").send_keys("123456")
        # driver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys("123456")
        driver.find_element(by=By.NAME, value="telA").send_keys("13316170917")
        driver.find_element(by=By.CLASS_NAME, value="emailA").send_keys("1193259912@qq.com")
        driver.find_element(by=By.NAME, value="telA").clear()
        driver.find_element(by=By.NAME, value="telA").send_keys("18810517011")
        driver.find_element(by=By.XPATH, value="//button").click()
        # driver.find_element_by_link_text("新浪").click()
        driver.find_element(by=By.LINK_TEXT, value="访问 新浪 网站").click()
        # 获取所有打开的窗口 列表
        list_windows = driver.window_handles
        # 切换到列表的最后一个
        driver.switch_to.window(list_windows[-1]);
        msg = driver.find_element(by=By.XPATH, value="//*[@id='SI_Top_Wrap']/div/div/div/div[1]/div[3]/a/i").text
        print("msg==", msg)
        self.assertIn("新浪", msg)
        time.sleep(3)
        driver.quit()
    # def testSina(self):
    #     """访问新浪首页，断言标题包含‘新浪’"""
    #     driver = self.driver
    #     driver.get("https://www.sina.com.cn/")
    #     # 等待标题出现‘新浪’字样
    #     WebDriverWait(driver, 10).until(EC.title_contains("新浪"))
    #     title = driver.title
    #     print("新浪页面标题:", title)
    #     self.assertIn("新浪", title)
    #     time.sleep(3)  # 便于观察结果，可删除
    def testBaidu(self):
        """访问百度首页，点击‘新闻’链接，断言新页面标题包含‘新闻’"""
        driver = self.driver
        driver.get("https://www.baidu.com/")
        # 等待‘新闻’链接可点击并点击
        news_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "新闻"))
        )
        news_link.click()

        # 获取所有窗口句柄，如果打开了新窗口则切换过去
        handles = driver.window_handles
        if len(handles) > 1:
            driver.switch_to.window(handles[-1])

        # 等待新页面标题包含‘新闻’
        WebDriverWait(driver, 10).until(EC.title_contains("新闻"))
        print("百度新闻页面标题:", driver.title)
        self.assertIn("新闻", driver.title)
        time.sleep(3)  # 便于观察结果，可删除
