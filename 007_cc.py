from bisect import bisect_left

# input
n = int(input())
a = [int(_) for _ in input().split()]
q = int(input())
b = []
for _ in range(q):
    b.append(int(input()))

a.sort()
for i in range(q):
    idx = bisect_left(a, b[i])
    if idx == 0:
        print(abs(a[idx]-b[i]))
    elif idx == n:
        print(abs(a[idx-1]-b[i]))
    else:
        print(min(abs(a[idx-1]-b[i]), abs(a[idx]-b[i])))
