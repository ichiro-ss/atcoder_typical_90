# input
n, k = [int(_) for _ in input().split()]

def digit_sum(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

num = 10 ** 5
nx = [0] * num
appeard_in = [-1 for _ in range(num)]

for i in range(num):
    nx[i] = (i + digit_sum(i)) % num
x = n
cnt = 0
while appeard_in[x] < 0:
    appeard_in[x] = cnt
    x = nx[x]
    cnt += 1
cycle = cnt - appeard_in[x]
if k >= appeard_in[x]:
    k = (k - appeard_in[x]) % cycle + appeard_in[x]
ans = -1
for i in range(num):
    if appeard_in[i] == k:
        ans = i
print(ans)