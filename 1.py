x = int(input())
s = 1
n = 1
print(s)
for k in range(2, x + 1):
    s += k
    n += 1
    if s % n == 0:
        print(s)
