# input
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# sort and then greedy
ans = 0
a.sort(); b.sort()
for i in range(n):
    ans += abs(a[i] - b[i])
print(ans)