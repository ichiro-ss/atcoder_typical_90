# input
n, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
l = [0]*q; r = [0]*q; v = [0]*q
for i in range(q):
    l[i], r[i], v[i] = [int(j) for j in input().split()]

