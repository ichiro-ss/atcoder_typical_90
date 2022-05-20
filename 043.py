from collections import deque
# input
h, w = [int(_) for _ in input().split()]
st_y, st_x = [int(_) - 1 for _ in input().split()]
gl_y, gl_x = [int(_) - 1 for _ in input().split()]
s = [[str(_) for _ in list(input())] for _ in range(h)]

INF = 10 ** 7
min_turn = [[INF for _ in range(w)] for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
deq = deque()
min_turn[st_y][st_x] = -1
deq.append((st_y, st_x))

while deq:
    y, x = deq.popleft()
    min_v = min_turn[y][x]
    for dir in range(4):
        nx_y, nx_x = y + dy[dir], x + dx[dir]
        while 0 <= nx_y < h and 0 <= nx_x < w and s[nx_y][nx_x] == "." and min_v + 1 <= min_turn[nx_y][nx_x]:
            if min_turn[nx_y][nx_x] == INF:
                deq.append((nx_y, nx_x))
            min_turn[nx_y][nx_x] = min_v + 1
            nx_y += dy[dir]
            nx_x += dx[dir]

print(min_turn[gl_y][gl_x])
