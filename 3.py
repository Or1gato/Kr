x = int(input())
a = 0
b = 0
n = 0
while a < x:
    a += 1
    b = 0
    while b < x:
        b += 1
        if (a ** 2) + (b ** 2) == x:
            n += 1
            if n - 1 > 0:
                print(n - 1)
