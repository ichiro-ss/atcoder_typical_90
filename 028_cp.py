# input
n = int(input())
lx, ly, rx, ry = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    lx[i], ly[i], rx[i], ry[i] = [int(_) for _ in input().split()]

num = 1000
cnt_papers = [[0 for _ in range(num+1)] for _ in range(num+1)]

for i in range(n):
    cnt_papers[ly[i]][lx[i]] += 1
    cnt_papers[ry[i]][rx[i]] += 1
    cnt_papers[ly[i]][rx[i]] -= 1
    cnt_papers[ry[i]][lx[i]] -= 1

for i in range(num):
    for j in range(1, num):
        cnt_papers[i][j] += cnt_papers[i][j-1]
for i in range(num):
    for j in range(1, num):
        cnt_papers[j][i] += cnt_papers[j-1][i]

cnts = [0] * (n+1)
for i in range(num):
    for j in range(num):
        if cnt_papers[i][j] > 0:
            cnts[cnt_papers[i][j]] += 1

for i in range(n):
    print(cnts[i+1])