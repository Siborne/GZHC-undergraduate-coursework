"""
=======================
Author：张梦娟
Time:2026/2/20 10:23
Project:test
========================
"""
# 导包
import unittest
from htmltestreport import HTMLTestReport
# 封装测试套件
from test_01_demo import TestForAssert
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestForAssert))
# 实例化 HTMLTestReport 对象
file_path = './report.html'
report = HTMLTestReport(file_path, title="Web 自动化测试报告", description="Win11.....")
# 执行测试套件
report.run(suite)


