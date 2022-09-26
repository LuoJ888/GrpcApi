import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# 测试固件分离思想，导入Init类
from Demo_test002 import Init
import time as t


# 在测试类中继承Init类
class TestBaidu(Init):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_title(self):
        '''百度首页：验证百度的title是否正确'''
        # assert self.driver.title=="百度一下，你就知道"
        self.assertEqual(self.driver.title, "百度一下，你就知道")

    def test_baidu_url(self):
        '''百度首页：验证百度的网址是否正确'''
        # 浏览器输入网址必须为https，域名后边必须有斜杠
        # assert self.driver.current_url=="https://www.baidu.com/"
        self.assertEqual(self.driver.current_url, "https://www.baidu.com/")

    def test_baidu_lent(self):
        '''百度首页：验证百度输入框输入上限'''
        # 浏览器输入网址必须为https，域名后边必须有斜杠
        # assert self.driver.current_url=="https://www.baidu.com/"
        self.assertEqual(len(self.driver.find_element('kw', 'su').send_keys()), 11)


if __name__ == '__main__':
    unittest.main()
