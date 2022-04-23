# input
n, l = [int(i) for i in input().split()]
k = int(input())
a = [int(i) for i in input().split()]

a.append(l)
l, r = 1, l
# l, mid, r: length of cutted yokan
while l < r - 1:
    mid = l + (r - l) // 2
    cut_len = 0
    y_cnt = 0
    prev_cut = 0
    for i in range(n + 1):
        if mid <= a[i] - prev_cut:
            prev_cut = a[i]
            y_cnt += 1
            cut_len = 0
    # print("y_cnt:", y_cnt)
    if y_cnt < k + 1:
        r = mid
    else:
        l = mid
    # print(l, r)
print(l)
