# input
n = int(input()); s = str(input())

# lからr (l != r)でo or xどちらかを含まない．
# 全部の場合（n(n-1)/2）から上を引けば良い．(順序関係なくｎからl, r２つを選ぶ)
# l == rの場合はどうせox両方含まないため，数えなくて良い

opp = 0
c = s[0]
cnt = 1
for i in range(1, n):
    if s[i] == c:
        cnt += 1
    else:
        opp += (cnt*(cnt-1)/2)
        cnt = 1
        c = s[i]
"""
5
ooooo
5
oxoxo
"""
opp += (cnt*(cnt-1)/2)
print(int(n * (n - 1) / 2 - opp))

