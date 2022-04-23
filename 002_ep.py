n = int(input())
if not n % 2:
    cnt = 0
    for i in range(1 << n):
        