import math
# input
l, r = [int(i) for i in input().split()]

mod = 10 ** 9 + 7

def sigma(l, r, digits):
    global mod
    return ((r - l + 1) * (l + r)) // 2 % mod * digits % mod

digits = len(str(l))
# digits = int(math.log10(l)) + 1 # python 3.8.2 で大きい数を入れるとアウト

tens = 10 ** digits
ans = 0
while tens <= r:
    ans += sigma(l, tens - 1, digits)
    ans %= mod
    l = tens; tens *= 10; digits += 1

ans += sigma(l, r, digits)

# sigma += (((r + 1) * r - l * (l - 1)) / 2) * digits　で後にintだと異なる答えに
print(ans % mod)