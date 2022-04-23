# input
n, l = [int(i) for i in input().split()]

step = [1]
for i in range(1, n+1):
    if i - l >= 0:
        step.append((step[i-1] + step[i-l]) % (1e9 + 7))
    else:
        step.append(step[i-1] % (1e9 + 7))
print(int(step.pop() % (1e9 + 7)))
