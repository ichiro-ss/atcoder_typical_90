h, w = [int(i) for i in input().split()]

# consider in the case of 1
# print((h//2+h%2) * (w//2+w%2))

if h == 1 or w == 1:
    print(h * w)
else:
    print((h//2+h%2) * (w//2+w%2))