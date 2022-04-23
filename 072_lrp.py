from collections import deque
# input
h, w = [int(i) for i in input().split()]
c = []
for _ in range(h):
    c.append([str(i) for i in list(input())])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
used = [[False for _ in range(20)] for _ in range(20)]

def dfs(sx, sy, px, py):
    if sx == px and sy == py and used[px][py]:
        return 0
        exit()
    used[px][py] = True

    ret = -10000
    for i in range(4):
        nx = px + dx[i]; ny = py + dy[i]
        if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1 or c[nx][ny] == '#':
            continue
        if (sx != nx or sy != ny) and used[nx][ny]:
            continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v + 1)
    used[px][py] = False
    return ret

ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans, dfs(i, j, i, j))
if ans <= 2:
    ans = -1
print(ans)