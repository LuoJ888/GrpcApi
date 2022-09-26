import re

phoneNum = input("电话号码：")
while not re.findall('^[0-9]+$', phoneNum):
    phoneNum = input("电话号码：")
