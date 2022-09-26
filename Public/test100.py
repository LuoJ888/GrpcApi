count = 0
for i in range(1, 6):
    for j in range(6):
        for k in range(6):
            for a in range(6):
                for b in range(6):
                    for c in range(6):
                        if i != j and i != k and i != a and i != b and i != c and j != k and j != a and j != b and j \
                                != c and k != a and k != b and k != c and a != b and a != c and b != c:
                            # print(i, j, k, a, b, c)
                            sn = i * 100000 + j * 10000 + k * 1000 + a * 100 + b * 10 + c
                            if sn % 25 == 0:
                                print(sn)
                                count = count + 1
print(count)
