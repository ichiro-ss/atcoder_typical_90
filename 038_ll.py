import math
# input
a, b = [int(i) for i in input().split()]

ans = int(a * b / math.gcd(a, b))
if ans > pow(10, 18):
    ans = "Large"
print(ans)
# ans = a * b // math.gcd(a, b)
# print("Large" if 10 ** 18 < ans else ans)

# python は多倍長だからオーバーフローおきない