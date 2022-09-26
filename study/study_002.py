# 冒泡排序

list_a = [5, 8, 9, 3, 2, 33, 7, 1]
# print()
len_a = len(list_a)
# print(type(list_a[1]))
# print(len_a)
for j in range(1, len_a):
    for i in range(1, len_a):
        # print(i)
        if list_a[i - 1] > list_a[i]:
            # print(list_a[i-1])
            list_a[i - 1], list_a[i] = list_a[i], list_a[i - 1]
            print(list_a[i - 1], list_a[i])
            print(list_a)

print(list_a)


