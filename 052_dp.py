# input
n = int(input())
a = []
for _ in range(n):
    a.append([int(_) for _ in input().split()])

num = 10 ** 9 + 7
ans = 1
for i in range(n):
    ans *= sum(a[i])
    ans %= num
print(ans % num)