# input
n, s = [int(i) for i in input().split()]
a, b = [], []
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    a.append(x); b.append(y)

# create a dp
dp = [[0 for _ in range(s)] for _ in range(n)]
if a[0] <= s:
    dp[0][a[0]-1] = 1
if b[0] <= s:
    dp[0][b[0]-1] = 1
for i in range(n - 1):
    for j in range(s):
        if dp[i][j] == 1:
            if j + a[i+1] < s:
                dp[i + 1][j + a[i+1]] = 1
            if j + b[i+1] < s:
                dp[i + 1][j + b[i+1]] = 1
# print(dp)

# search the dp
ans = ""
if dp[n - 1][s - 1]:
    j = s - 1
    for i in range(n - 1, 0, -1):
        if j-a[i] >= 0 and dp[i-1][j-a[i]]:
            ans = "A" + ans
            j -= a[i]
        elif j-b[i] >= 0 and dp[i-1][j-b[i]]:
            ans = "B" + ans
            j -= b[i]
    # first shopping
    if j == a[0] - 1:
        ans = "A" + ans
    else:
        ans = "B" + ans
    print(ans)
else:
    print("Impossible")
