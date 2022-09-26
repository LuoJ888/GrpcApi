import unittest
# 测试固件分离思想，导入Init类
from LoginUI import MainUI
import time as t


# 在测试类中继承Init类
class TestBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.key = MainUI().get_value()

    def tearDown(self) -> None:
        pass

    def test_baidu_title(self):
        '''百度首页：验证百度的title是否正确'''
        # assert self.driver.title=="百度一下，你就知道"
        self.assertEqual(len(self.key.user('12')), 2)


    def test_baidu_url(self):
        '''百度首页：验证百度的网址是否正确'''
        # 浏览器输入网址必须为https，域名后边必须有斜杠
        # assert self.driver.current_url=="https://www.baidu.com/"
        self.assertEqual(len(self.key.pwd('111')), 5)


if __name__ == '__main__':
    unittest.main()
