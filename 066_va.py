# input
n = int(input())
l, r = [0]*n, [0]*n
for i in range(n):
    l[i], r[i] = [int(_) for _ in input().split()]

exp = 0
for i in range(n):
    for j in range(i + 1, n):
        cnt, fig = 0, 0
        for k in range(l[i], r[i] + 1):
            for m in range(l[j], r[j] + 1):
                if k > m:
                    cnt += 1
                fig += 1
        exp += cnt / fig
print(exp)