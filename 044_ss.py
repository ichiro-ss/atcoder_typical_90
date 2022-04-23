# input
n, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
t, x, y = [], [], []
for _ in range(q):
    i, j, k = [int(i) for i in input().split()]
    t.append(i); x.append(j); y.append(k)

shift_cnt = 0
for i in range(q):
    if t[i] == 1:
        real_x = x[i] - 1 - (shift_cnt % n)
        real_y = y[i] - 1 - (shift_cnt % n)
        a[real_x], a[real_y] = a[real_y], a[real_x]
    if t[i] == 2:
        shift_cnt += 1
    if t[i] == 3:
        print(a[x[i] - 1 - (shift_cnt % n)])
