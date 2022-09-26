a = "bbcbaacccccb"
list_b = list(a)
# list_c = list(set(list_b))
# print(len(sorted(list_c)))

list_c = []
list_v = []
for i in list_b:
    if i not in list_c:
        list_c.append(i)
list_d = sorted(list_c)
len_d = len(list_d)

for j in range(len_d):
    list_v.append(list_d[len_d-1])
    len_d = len_d-1
print(list_v)

# print(list(reversed(list_d)))
