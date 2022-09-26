import re

inp = input()
inp = str(inp)
number = ['18820202021', '130-4567-8900', '156 5555 6666', '0755-88886666', '010-89965331']
for no in number:
    right = re.findall("^1\d{10}$", no)
    error = re.findall("^1[\d]{2}-\d{4}-\d{4}$|^1[\d]{2} \d{4} \d{4}$", no)
    # print(no)

    def le():
        if len(no) == len(inp):
            print('手机长度正确')
        # else:
        #     print(f'{no}手机长度错误')


    le()
    try:
        if right[0] in no:
            def rig():
                if right[0] == inp:
                    print('号码正确')
                else:
                    print(f'{right[0]}号码错误')
            rig()

    except:
        pass
        # print(error)
    # if type(right[0]) is None:
    #     del right[0]
    #     print(right[0])
    # print(no)1

    # print(len(no))
    # if len(no) == 8:
    #     print('手机长度正确')
    # else:
    #     print('手机长度错误')
    # print(type(no))
    # def le():
    #     if len(right[0]) == len(inp):
    #         print('手机长度正确')
    #     else:
    #         print('手机长度错误')
    #
    #
    # le()
    #
    #
    # def rig():
    #     if right[0] == inp:
    #         print('手机号码正确')
    #     else:
    #         print('手机号码错误')
    #
    #
    # rig()
# print(no)
