# returns an approximate int value
def app_int(x):
    if 1 - x % 1 < 1e-7:    # is it better to calculate integers?
        return int(x + 1)
    else:
        return int(x)

# input
k = int(input())

# brute force of divisor O(d(k)^2)
divs = []
# memorize divisors
for i in range(1, app_int(pow(k, 1/2)) + 1):
    if not k % i:
        divs.append(i)
# div by div by div
cnt = 0
for a in range(len(divs)):
    for b in range(a, len(divs)):
        if not k % (divs[a] * divs[b]) and divs[b] <= (k // (divs[a] * divs[b])):
            cnt += 1
print(cnt)

# brute force O(k^(5/6))
# n = app_int(pow(k, 1/3))
# cnt = 0
# for a in range(1, n + 1):
#     for b in range(a, int(pow(k / a, 1/2)) + 1):
#         if not k % (a * b) and b <= (k // (a * b)):
#             cnt += 1
# print(cnt)
