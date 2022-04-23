from math import sqrt, log2
n = int(input())

cnt = 0
for i in range(2, int(sqrt(n)) + 1):
    while not n % i:
        n //= i
        cnt += 1
if not n == 1:
    cnt += 1

# if log2(cnt) == 2: print 2
# if log2(cnt) == 2.3: print3
print(int(log2(cnt - 1)) + 1 if cnt != 1 else 0)
