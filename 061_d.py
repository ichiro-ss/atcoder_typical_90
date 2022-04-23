#input
q = int(input())
t = [0]*q; x =[0]*q
for i in range(q):
    t[i], x[i] = [int(j) for j in input().split()]

# simple solution
# cards = []
# for i in range(q):
#     if t[i] == 1:
#         cards.insert(0, x[i])
#     elif t[i] == 2:
#         cards.append(x[i])
#     elif t[i] == 3:
#         print(cards[x[i]-1])
#     else:
#         print("error")

