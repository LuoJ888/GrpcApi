import random


# creat_phone()
# 生成电话号
def creat_phone():
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


# 调用
# print(creat_phone())
num = input('请输入生成的数量')
for index in range(0, int(num)):
    print(creat_phone())