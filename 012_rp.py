import sys
sys.setrecursionlimit(10**6)
# input
h, w = [int(i) for i in input().split()]
q_num = int(input())
Q = []
for _ in range(q_num):
    a = [int(i) - 1 for i in input().split()]
    Q.append(a)

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
passed = [[False for _ in range(w)] for _ in range(h)]
ans = "No"
# red: reds[i][j]==True, white reds[i][j]==False
reds = [[False for _ in range(w)] for _ in range(h)]

# solution 1 DFS (redursion) TLE
# def dfs(a_h, a_w, cor_h, cor_w, b_h, b_w):
#     global ans
#     if cor_h == b_h and cor_w == b_w:
#         ans = "Yes"
#         return

#     passed[cor_h][cor_w] = True
#     for i in range(4):
#         next_h, next_w = cor_h + dh[i], cor_w + dw[i]
#         if next_h < 0 or next_w < 0 or next_h >= h or next_w >= w\
#              or passed[next_h][next_w] or not reds[next_h][next_w]:
#             continue
#         dfs(a_h, a_w, next_h, next_w, b_h, b_w)
#     passed[cor_h][cor_w] = False
#     return

# for q in Q:
#     ans = "No"
#     if q[0] == 0:
#         reds[q[1]][q[2]] = True
#     elif q[0] == 1 and reds[q[1]][q[2]] and reds[q[3]][q[4]]:
#             dfs(q[1], q[2], q[1], q[2], q[3], q[4])
#         print(ans)

# solution 2 DFS (stack)
# for q in Q:
#     ans = "No"
#     if q[0] == 0:
#         reds[q[1]][q[2]] = True
#     elif q[0] == 1:
#         if reds[q[1]][q[2]] and reds[q[3]][q[4]]:
#             # dfs using stacks
#             stack = [[q[1], q[2]]]
#             visited = [[False for _ in range(w)] for _ in range(h)]
#             visited[q[1]][q[2]] = True

#             while stack:
#                 high, wid = stack.pop()
#                 for i in range(4):
#                     next_h, next_w = high + dh[i], wid + dw[i]
#                     if 0 <= next_h < h and 0 <= next_w < w and \
#                         not visited[next_h][next_w] and reds[next_h][next_w]:
#                         visited[next_h][next_w] = True
#                         stack.append([next_h, next_w])
#                 if visited[q[3]][q[4]]:
#                     ans = "Yes"
#                     break
#         print(ans)

# solution 3 UnionFind without rank
# def root(x):
#     if par[x] == x:
#         return x
#     else:
#         par[x] = root(par[x])
#         return par[x]

# def are_same(x, y):
#     return root(x) == root(y)

# def unite(x, y):
#     x, y = root(x), root(y)
#     if x == y:
#         return
#     par[x] = y

# par = [0] * (h * w)
# for i in range(len(par)):
#     par[i] = i

# for q in Q:
#     ans = "No"
#     if q[0] == 0:
#         reds[q[1]][q[2]] = True
#         for i in range(4):
#             next_h, next_w = q[1] + dh[i], q[2] + dw[i]
#             if 0 <= next_h < h and 0 <= next_w < w and reds[next_h][next_w]:
#                 unite(w * q[1] + q[2], w * next_h + next_w)
#     elif q[0] == 1:
#         if reds[q[1]][q[2]] and reds[q[3]][q[4]] and \
#             are_same(w * q[1] + q[2], w * q[3] + q[4]):
#             ans = "Yes"
#         print(ans)

# solution 3 UnionFind without rank
def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def are_same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return
    
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

par, rank = [0] * (h * w), [0] * (h * w)
for i in range(len(par)):
    par[i] = i

for q in Q:
    ans = "No"
    if q[0] == 0:
        reds[q[1]][q[2]] = True
        for i in range(4):
            next_h, next_w = q[1] + dh[i], q[2] + dw[i]
            if 0 <= next_h < h and 0 <= next_w < w and reds[next_h][next_w]:
                unite(w * q[1] + q[2], w * next_h + next_w)
    elif q[0] == 1:
        if reds[q[1]][q[2]] and reds[q[3]][q[4]] and \
            are_same(w * q[1] + q[2], w * q[3] + q[4]):
            ans = "Yes"
        print(ans)