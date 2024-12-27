import sys
import numpy as np

N = input()
S = [""]*int(N)
sign = [0]*501
for i in range(0,int(N)):
    S[i] = input()
    value = int(S[i])
    if sign[value]!=1:
        sign[value]=1

for i in range(1, len(sign)):
    if sign[i]==1:
        print(i)

# 建立空的数字型数组：[0]*大小
# 字符型：["0"]*大小
