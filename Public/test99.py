count = 0
for i in range(1, 6):
    for j in range(6):
        for k in range(6):
            if i != j and i != k and j != k:
                print(i, j, k)
                count = count + 1
print(count)
