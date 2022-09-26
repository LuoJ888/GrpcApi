import unittest
from selenium import webdriver


class Init(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def tearDown(self) -> None:
        self.driver.quit()
