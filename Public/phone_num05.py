import random


# creat_phone()
# 生成电话号
def creat_phoneNum():
    # 第二位
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位的值根据第二位来确定
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9)
    }[second]
    # 后8位随机抽取
    suffix = ''
    for x in range(8):
        suffix = suffix + str(random.randint(0, 9))
    # 拼接
    return "1{}{}{}".format(second, third, suffix)
#
#
# # 调用
# # print(creat_phone())
# num = input('请输入生成的数量')
# for index in range(0, int(num)):
#     print(creat_phoneNum())

# 生成座机电话号
def creat_landlineNum():
    # 第二位
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位的值根据第二位来确定
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9)
    }[second]
    forth = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 后8位随机抽取
    suffix = ''
    for x in range(7):
        suffix = suffix + str(random.randint(0, 9))
    # 拼接
    return "(0{}{}{})-{}".format(second, third, forth, suffix)


# 调用
# print(creat_phone())
# num = input('请输入生成的数量')
# for index in range(0, int(num)):
#     print(creat_phone())

def creat_areaphoneNum():
    areaNum = ''
    for x in range(2):
        areaNum = areaNum + str(random.randint(0, 9))
    # 第二位
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位的值根据第二位来确定
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9)
    }[second]
    # 前4位随机抽取
    prefix_fs = ''
    for x in range(4):
        prefix_fs = prefix_fs + str(random.randint(0, 9))
    # 后4位随机抽取
    suffix_fs = ''
    for x in range(4):
        suffix_fs = suffix_fs + str(random.randint(0, 9))
    # 拼接
    return "(+{})-1{}{}-{}-{}".format(areaNum, second, third, prefix_fs, suffix_fs)


# 调用
# print(creat_phone())
num = input('请输入生成的数量：')
print("电话号码:")
for index in range(0, int(num)):
    print(creat_phoneNum())
print("\n")
print("座机号码:")
for index in range(0, int(num)):
    print(creat_landlineNum())
print("\n")
print("区号+电话号码:")
for index in range(0, int(num)):
    print(creat_areaphoneNum())

