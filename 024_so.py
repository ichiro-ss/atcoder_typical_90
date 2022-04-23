# input
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
ans = "Yes"

dif = 0
for i in range(n):
    dif += abs(a[i] - b[i])

# consider a parity
if k < dif:
    ans = "No"
elif (k - dif) % 2:
    ans = "No"

print(ans)