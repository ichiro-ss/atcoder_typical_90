# input
n = int(input())
s = str(input())
target = "atcoder"
mod = 10 ** 9 + 7

# dp[i][j]: The number of ways that use up to the i-th letter of s
# to create up to the j-th letter of target.
dp = [[0 for _ in range(len(target)+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, len(target)+1):
        if s[i-1] == target[j-1]:
            dp[i][j] = int((dp[i-1][j-1] + dp[i-1][j]) % mod)
        else:
            dp[i][j] = dp[i-1][j]
print(int(dp[n][len(target)] % mod))