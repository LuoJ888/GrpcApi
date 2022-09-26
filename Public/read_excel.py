import openpyxl
from Demo_req import req
import pytest

data = openpyxl.load_workbook(r'C:\Users\v_wenjieluo\PycharmProjects\ApiTest\test_case_data\case.xlsx')
sheets = data.sheetnames
req().setUp()
for name in sheets:
    sheet = data[name]
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
req().tearDown()