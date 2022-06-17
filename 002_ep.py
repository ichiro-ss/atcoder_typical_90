# input
n = int(input())

for i in range(2 ** n):
    brac = 0
    ans = ""
    flag = False
    for j in range(n):
        if (i >> j) & 1:
            brac += 1
            ans = ')' + ans
        else:
            brac -= 1
            ans = '(' + ans
        
        if brac < 0:
            flag = True
            break
    
    if not (flag or brac):
        print(ans)

