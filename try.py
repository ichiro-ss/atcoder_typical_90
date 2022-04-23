# input
n, w_nap = [int(i) for i in input().split()]
v, w = [], []
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    v.append(a); w.append(b)

# create a dp
dp = [[0 for _ in range(w_nap + 1)] for _ in range(n)]
for i in range(n):
    for j in range(w_nap + 1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][w_nap])
