k = int(input())
m = int(input())
n = int(input())

if n <= k:
    print(2 * m)
else:
    t = 2 * n
    print((t + k - 1) // k * m)
