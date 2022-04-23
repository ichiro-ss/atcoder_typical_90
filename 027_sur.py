#input
n = int(input())
exist = set()
users = []

for i in range(n):
    s = str(input())
    if s not in exist:
        exist.add(s)
        users.append(i+1)

# this will be deleted with using map
for num in users:
    print(num)