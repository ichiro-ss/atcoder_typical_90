import itertools

# input
n = int(input())
a = [[0]*n]*n
for i in range(n):
    a[i] = [int(j) for j in input().split()]
m = int(input())
# input 1
# x = [0]*m; y = [0]*m
# for i in range(m):
#     x[i], y[i] = [int(j) - 1 for j in input().split()]

#input 2
bad = [[False for i in range(n)]for j in range(n)]
# bad = [[False]*n]*nだと同じリストを３つ定義しているだけなので，要素の値を変更すると他の要素まで変わってしまう．
for i in range(m):
    x, y = [int(j) - 1 for j in input().split()]
    bad[x][y] = True
    bad[y][x] = True

# solution1 permutations (O(n * n! * m)) 1254(ms)
# permutations_l = itertools.permutations([int(i) for i in range(n)])

# ans = -1
# for runners_list in permutations_l:
#     ok = True   # relationship is good
#     sum_t = 0   # sum of times which takes start to finish
#     for leg in range(n - 1):
#         for i in range(m):
#             # remove the case of the bad adjacent
#             if (runners_list[leg] == x[i] and runners_list[leg + 1] == y[i]) or \
#                 (runners_list[leg + 1] == x[i] and runners_list[leg] == y[i]):
#                 ok = False
#                 break
#         if ok:
#             sum_t += a[runners_list[leg]][leg]
#         else:
#             break
#     if ok:
#         sum_t += a[runners_list[n - 1]][n - 1]
#         if ans < 0 or sum_t < ans:
#             ans = sum_t

# print(ans)

# solution2 permutations (O(n * n!)) 478(ms)
# permutations_l = itertools.permutations([int(i) for i in range(n)])

# ans = -1
# for runners_list in permutations_l:
#     ok = True
#     sum_t = 0
#     for leg in range(n - 1):
#         if bad[runners_list[leg]][runners_list[leg + 1]]:
#             ok = False
#             break
#         sum_t += a[runners_list[leg]][leg]
#     if ok:
#         sum_t += a[runners_list[n - 1]][n - 1]
#         if ans < 0 or sum_t < ans:
#             ans = sum_t
# print(ans)


# solution2 recursion
