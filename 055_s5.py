n, p, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    a[i] = a[i] % p

for i in range(n-4):
    for j in range(i+1, n-3):
        for k in range(j+1, n-2):
            for l in range(k+1, n-1):
                for m in range(l+1, n):
                    # can't use a[i]*a[j]*a[k]*a[l]*a[m]%p == q:
                    if a[i]*a[j]%p * a[k]%p * a[l]%p * a[m]%p == q:
                        cnt += 1
print(cnt)