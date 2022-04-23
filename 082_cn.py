# input
l, r = [int(i) for i in input().split()]

sigma = ((r + 1) * r - l * (l - 1)) / 2
print(int(sigma))