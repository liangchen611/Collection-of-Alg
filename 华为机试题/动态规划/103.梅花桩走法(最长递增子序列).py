import sys

n = int(input())
H = input().strip().split(" ")
H = [int(h) for h in H]

def LCS(arr):
    tails = []
    for num in arr:
        if not tails:
            tails.append(num)
            continue
        elif tails:
            sign = 0
            for j in range(len(tails)):
                t = tails[j]
                if num<=t:
                    tails[j]=num
                    sign=1
                    break
            if sign==0:
                tails.append(num)
    return tails

R = LCS(H)
print(len(R))