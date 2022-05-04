# input
n, m = [int(i) for i in input().split()]
a, b = [], []
for _ in range(m):
    x, y = [int(i) for i in input().split()]
    a.append(x); b.append(y)

dict = {}
cnt = 0
for i in range(m):
    if a not in dict:
        dict[a] = [b]
    elif b not in dict[a]:
        dict[a].append(b)
    if b in dict and a in dict[b]:
        cnt += 1

print(cnt)


