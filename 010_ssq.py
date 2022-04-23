# input
n = int(input())
c = [0]*n; p = [0]*n
for i in range(n):
    c[i], p[i] = [int(j) for j in input().split()]

q = int(input())
l = [0]*q; r = [0]*q
for i in range(q):
    l[i], r[i] = [int(j) for j in input().split()]

# solution 1 O(NQ)
# # calculate ans for each query
# for i in range(q):
#     sum1 = 0; sum2 = 0
#     for j in range(l[i] - 1, r[i]):
#         if c[j] == 1:
#             sum1 += p[j]
#         else:
#             sum2 += p[j]
#     print(sum1, sum2)

# solution 2 using a cumulative sum O(N+Q)
# create cumulative sum arrays
sum1 = [0]; sum2 = [0]
for i in range(n):
    if c[i] == 1:
        sum1.append(sum1[i] + p[i])
        sum2.append(sum2[i])
    else:
        sum1.append(sum1[i])
        sum2.append(sum2[i] + p[i])

for i in range(q):
    print(sum1[r[i]] - sum1[l[i]-1], sum2[r[i]] - sum2[l[i]-1])

# result
"""
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7

sum1 [0, 72, 72, 72, 95, 95, 135, 210]
sum2 [0, 0, 78, 172, 172, 261, 261, 261]

72 172
23 172
23 183
63 89
115 89
95 261
63 261
138 183
135 261
138 261
"""