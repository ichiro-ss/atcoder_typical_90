# input
h, w = [int(i) for i in input().split()]
q_num = int(input())
Q = []
for _ in range(q_num):
    a = [int(i) - 1 for i in input().split()]
    Q.append(a)

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
# red: reds[i][j]==True, white reds[i][j]==False
reds = [[False for _ in range(w)] for _ in range(h)]

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def are_same(x, y):
    return root(x) == root(y)

# UnionFind without rank
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

# UnionFind with rank
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