# input
n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
b = []
for _ in range(q):
    b.append(int(input()))

a.sort
l, r = 0, n - 1
for i in range(q):
    while l < r + 1:
        mid = l + (r - l) // 2
        if a[mid] == b[i]:
            break
        elif a[mid] < b[i]:
            l = mid
        else:
            r = mid - 1
    print(min(abs(a[mid] - b[i]), abs(a[mid-1] - b[i])))
