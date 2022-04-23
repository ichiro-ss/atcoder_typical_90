h, w = [int(i) for i in input().split()]
a = [list(map(int, input().split())) for _ in range(h)]
sum_column = [0]*h
sum_row = [0]*w

# memorize sum of column/row values
for i in range(h):
    sum_column[i] = sum(a[i])
for i in range(w):
    for j in range(h):
        sum_row[i] += a[j][i]

# calulate the answer
for i in range(h):
    for j in range(w):
        # this means B[i][j]
        print(sum_column[i] + sum_row[j] - a[i][j], end=" ")
    print()

