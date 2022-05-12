# input
h, w = [int(i) for i in input().split()]
Q = int(input())
q = []
for _ in range(Q):
    a = [int(i) - 1 for i in input().split()]
    q.append(a)

# Union Find
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
# red: reds[i][j]==True, white: reds[i][j]==False
reds = [[False for _ in range(w)] for _ in range(h)]

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
for a_q in q:
    ans = "No"
    if a_q[0] == 0:
        reds[a_q[1]][a_q[2]] = True
        for i in range(4):
            next_h, next_w = a_q[1] + dh[i], a_q[2] + dw[i]
            if 0 <= next_h < h and 0 <= next_w < w and reds[next_h][next_w]:
                unite(w * a_q[1] + a_q[2], w * next_h + next_w)
    elif a_q[0] == 1:
        if reds[a_q[1]][a_q[2]] and reds[a_q[3]][a_q[4]] and \
            are_same(w * a_q[1] + a_q[2], w * a_q[3] + a_q[4]):
            ans = "Yes"
        print(ans)