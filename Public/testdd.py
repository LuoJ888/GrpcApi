# import unittest
#
# from Public.demoLog import demo_Log
#
#
# class api(unittest.TestCase):
#     def setUp(self):
#         demo_Log().log().info('测试用例开始执行')
#
#     def tearDown(self):
#         demo_Log().log().info('测试用例执行完毕')
#
#     def test_post(self):
#         print("test 1")
#
#     def test_get(self):
#         a = 1
#         self.assertEqual(1, a)
#         print("test 2")
#
#     def test_dell(self):
#         print("test 3")
#
#
# if __name__ == '__main__':
#     unittest.main()
a = input()
b = input()
if a=1 or b=2:
    add=a+b
    print(add)
else:
    aa=a-b
    print(aa)
# import pytest
#
# from Public.demoLog import demo_Log
#
#
# class TestApi:
#     def setUp(self):
#         demo_Log().log().info('测试用例开始执行')
#
#     def tearDown(self):
#         demo_Log().log().info('测试用例执行完毕')
#
#     def test_post(self):
#         add = 5
#         print("test 1")
#         assert add == 1
#
#     def test_get(self):
#         print("test 2")
#
#     def test_dell(self):
#         print("test 3")
#
#
# if __name__ == '__main__':
#     pytest.main()

# import os
# import unittest
#
#
# class EcshopLogin(unittest.TestCase):
#
#     def setUp(self):
#         demo_Log().log().info('测试用例开始执行')
#
#     def tearDown(self):
#         demo_Log().log().info('测试用例执行完毕')
#
#     # 测试用例
#     def test01_xiaoming(self):
#         print("测试小明")
#
#     # 测试用例
#     def test02_weiwei(self):
#         print("测试微微")
#
#     # 测试用例
#     def test10_xiaohongi(self):
#         print("测试小红")
#
#
# if __name__ == '__main__':
#     unittest.main()
# suite = unittest.TestSuite()
# testcase = unittest.defaultTestLoader.discover(start_dir=os.getcwd(), pattern='*.py')
# suite.addTests(testcase)
# unittest.main(defaultTest='suite')
