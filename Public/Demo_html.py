import unittest
import os
import HTMLTestRunner
import datetime


def allTests():
    # 获取要执行的测试模块
    suite = unittest.TestLoader().discover(
        # start_dir指的是测试模块的路径
        start_dir=os.path.dirname(__file__),
        # pattern通过正则方式加载所有测试模块
        pattern="test_*.py")
    return suite


def run():
    filename = os.path.join(os.path.dirname(__file__), 'report', 'index{}.html'.format(datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S'), encoding='UTF-8'))
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试',
        description='ui test'
    )
    runner.run(allTests())


if __name__ == '__main__':
    run()
