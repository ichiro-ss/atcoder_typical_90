h, w = [int(i) for i in input().split()]
a, b = [], []
for _ in range(h):
    a.append([int(i) for i in input().split()])
for _ in range(h):
    b.append([int(i) for i in input().split()])

ope_cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        dif = b[i][j] - a[i][j]
        ope_cnt += abs(dif)
        a[i][j] += dif; a[i+1][j] += dif; a[i][j+1] += dif; a[i+1][j+1] += dif
if a == b:
    print("Yes")
    print(ope_cnt)
else:
    print("No")