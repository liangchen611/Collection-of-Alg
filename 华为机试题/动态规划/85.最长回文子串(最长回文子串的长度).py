import sys

string = input().strip()

L = len(string)
max_L = 0
sign = 0
# DP[i][j]：i为开头，j为结尾时是否构成回文
DP = [[False]*L for _ in range(L)]
for i in range(L):
    DP[i][i] = True

for l in range(2,L+1):
    # 长度为1显然为回文子串
    if L == 1:
        print(1)
        break
    for i in range(0,L-l+1):
        j = i+l-1
        if string[i] == string[j]:
            if l == 2 or DP[i+1][j-1]==True:
                DP[i][j]=True
                if l > max_L:
                    max_L = l
print(max_L)