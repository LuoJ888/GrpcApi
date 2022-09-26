import openpyxl
from Demo_req import req
import unittest, time, os
from Public import BSTestRunner


BASH_DIR = "report"
if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'report')
    # file_reslut = os.path.join(file_dir, r'C:\Users\v_wenjieluo\PycharmProjects\ApiTest\test_case_data\case.xlsx')
    file_reslut = openpyxl.load_workbook(r'C:\Users\v_wenjieluo\PycharmProjects\ApiTest\test_case_data\case.xlsx')
    sheets = file_reslut.sheetnames
    req().setUp()
    for name in sheets:
        sheet = file_reslut[name]
        for values in sheet.values:
            if type(values[0]) is int:
                data2 = {
                    "url": values[4], "params": values[3]
                }
                for key in list(data2.keys()):
                    # print(data2[key])
                    if data2[key] is None:
                        del data2[key]
                # print(data2)
                # del key
                # print(key)
                print(f'正在执行： id->{values[0]} {values[5]} {values[4]}')

                # key2 = req(**data2)
                # # print(key2)
                getattr(req(), values[5])(**data2)
    try:
        os.remove(file_reslut)
    except:
        pass
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(req))
    now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    file = os.path.join(file_dir, (now + '.html'))
    re_open = open(file, 'wb')
    print(re_open)
    besautiful = BSTestRunner.BSTestRunner(title="报告",
                                           description="测试报告",
                                           stream=re_open,
                                           trynum=3,
                                           filepath=BASH_DIR,
                                           is_show=True)
    besautiful.run(suite)
