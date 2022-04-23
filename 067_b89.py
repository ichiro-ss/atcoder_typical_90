def eight_nine(x8):
    # 8 to 10
    x10 = 0
    i = 1
    while x8 > 0:
        x10 += (x8 % 10) * i
        i *= 8
        x8 //= 10

    # 10 to 9
    x9 = 0
    i = 1
    while x10 > 0:
        x9 += 5 * i if x10 % 9 == 8 else (x10 % 9) * i  # if fig 8, change it to 5
        i *= 10
        x10 //= 9

    return x9
    
n, k = [int(i) for i in input().split()]
for i in range(k):
    n = eight_nine(n)
print(n)