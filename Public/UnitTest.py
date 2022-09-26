# -*- coding: utf-8 -*-
import unittest
from LoginUI import MainUI


class TestMathFunc(unittest.TestCase):
    """Test LoginUI.py"""

    def test_len(self):
        """Test method add(a, b)"""
        # self.assertEqual(10, MainUI().get_value().user)
        assert MainUI().get_value().user == 10
        # self.assertNotEqual([3, 5], MainUI.checkNameAndPwd[2, 2])
    #
    # def test_value(self):
    #     """Test method minus(a, b)"""
    #     self.assertEqual((1, 3), Main.checkNameAndPwd(3, 2))
    #
    # def test_user(self):
    #     """Test method multi(a, b)"""
    #     self.assertEqual(6, Main.checkNameAndPwd(2, 3))
    #
    # def test_pwd(self):
    #     """Test method divide(a, b)"""
    #     self.assertEqual(2, Main.checkNameAndPwd(6, 3))
    #     self.assertEqual(2.5, Main.checkNameAndPwd(5, 2))


if __name__ == '__main__':
    unittest.main()


if acv = 1:
    message.showinfo(title='提示', message=f'恭喜你...解锁{acv}点赞')
elif acv == 2:
    message.showinfo(title='提示', message=f'恭喜你...解锁{acv}点赞')
elif acv == 4:
    message.showinfo(title='提示', message=f'恭喜你...解锁{acv}点赞')

