n, m = [int(i) for i in input().split()]
a = [0]*m; b = [0]*m
for i in range(m):
    a[i], b[i] = [int(j) for j in input().split()]

# solution 1
# nodes = set()
# removed = set()
# for i in range(m):
#     bigger = max(a[i], b[i])
#     if bigger not in nodes and bigger not in removed:
#         nodes.add(bigger)
#     elif bigger in nodes and bigger not in removed:
#         nodes.remove(bigger)
#         removed.add(bigger)
# print(len(nodes))

# solution 2
cnt = 0
nodes = [0] * n
for i in range(m):
    bigger = max(a[i], b[i])
    nodes[bigger - 1] += 1
for i in range(n):
    if nodes[i] == 1:
        cnt += 1
print(cnt)