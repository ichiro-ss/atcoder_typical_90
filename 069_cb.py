# input
n, k = [int(i) for i in input().split()]

# painted = [k, k - 1, k - 2]
# for i in range(2, n):
if n == 1:
    print(k); exit()
else:
    ans = int(k * (k - 1)) % (1e9 + 7)
    ans *= pow(k - 2, n - 2, int(1e9 + 7))
    ans %= (1e9 + 7)
print(int(ans))

"""
26276514 421031430
answer: 780646908
my ans: 929499467
"""