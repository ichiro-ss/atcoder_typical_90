# input
n = int(input())
a = [int(i) for i in input().split()]
a.sort()

# modified brute force
for i in range(n // a[0]):
    for j in range(n // a[1]):
        res = n - (a[0]*i + a[1]*j)
        if res >= 0 and not res % a[2]:
            print(i + j + res//a[2])
            exit()
        if res < 0:
            break
