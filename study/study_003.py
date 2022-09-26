def fib(n):
    a = 0
    b = 1
    numlist = [0, 1]
    for i in range(1, n):
        a, b = b, a + b
        print(a, b)
        numlist.append(a)
    print(numlist[n - 1])


fib(10)
