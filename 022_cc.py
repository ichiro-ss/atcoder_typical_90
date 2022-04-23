import math

def cut(g, x):
    return x // g - 1

a, b, c = [int(i) for i in input().split()]

G = math.gcd(math.gcd(a, b), c)
print(cut(G, a) + cut(G, b) + cut(G, c))