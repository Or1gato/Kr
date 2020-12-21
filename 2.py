n = 0
for i in reversed(range(2,10)):
    n = n * 10 + i
    eq = n * 9 + i - 2
    print('{0} * {1} + {2} = {3}'.format(n, 9, i-2, eq))