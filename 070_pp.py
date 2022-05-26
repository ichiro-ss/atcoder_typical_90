# input
n = int(input())
x, y = [0] * n, [9] * n
for i in range(n):
    x[i], y[i] = [int(_) for _ in input().split()]

def med_v(a):
    a.sort()
    length = len(a)
    if length % 2:
        return a[length // 2]
    else:
        return (a[length // 2 - 1] + a[length // 2]) / 2

med_x = med_v(x)
ans_x = 0
for i in range(n):
    ans_x += abs(x[i] - med_x)

med_y = med_v(y)
ans_y = 0
for i in range(n):
    ans_y += abs(y[i] - med_y)

print(int(ans_x + ans_y))
