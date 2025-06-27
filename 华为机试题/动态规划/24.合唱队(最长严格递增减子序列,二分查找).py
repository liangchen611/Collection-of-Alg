import sys
from bisect import bisect_left

def lis_len_count(arr):
    tails = [arr[0]]
    inc = [1]*len(arr)
    for i in range(1, len(arr)):
        h = arr[i]
        if h > tails[-1]:
            tails.append(h)
            inc[i] = len(tails)
        else:
            pos = bisect_left(tails,h)
            tails[pos]=h
            inc[i] = pos+1
    return inc

while True:
    try:
        N = int(sys.stdin.readline())
        H = list(map(int, sys.stdin.readline().split()))
        L = lis_len_count(H)
        R = lis_len_count(H[::-1])[::-1]
        best = 0
        for i in range(1,N-1):
            if L[i] >=2 and R[i] >=2:
                best = max(best, L[i]+R[i]-1)
        print(N - best)
    except:
        break
    
#对原数组的每个位置，求出它的LIS和LDS长度，由于LIS和LDS都包含此位置，所以要-1，LIS[i]+LDS[i]-1
#这样得到的就是以该位置为峰值中心，队伍中所剩余学生的最大个数
#将学生总人数与剩余学生最大个数的最大值相减，可以求得最小出列人数