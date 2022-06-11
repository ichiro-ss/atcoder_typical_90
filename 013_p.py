from heapq import heappush, heappop
# input
n, m = [int(_) for _ in input().split()]
G = [[] for _ in range(n)]
for i in range(m):
    a, b, c = [int(_) for _ in input().split()]
    G[a-1].append([b-1, c])
    G[b-1].append([a-1, c])

INF = 10 ** 9 + 10
def dijkstra(G, s):
    dist = [INF] * len(G)
    dist[s] = 0
    hq = [[0, s]]
    passed = [False] * n
    while hq:
        v = heappop(hq)[1]
        passed[v] = True
        for to, cost in G[v]:
            if not passed[to] and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, [dist[to], to])
    return dist

from_1 = dijkstra(G, 0)
from_n = dijkstra(G, n-1)
for i in range(n):
    print(from_1[i] + from_n[i])