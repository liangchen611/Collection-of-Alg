import sys
from math import ceil

m = int(input().strip())

metrix = sys.stdin.readline().strip().split(" ")
metrix = [int(me) for me in metrix]

n = int(input().strip())

if n == 0 or m==1:
    print("true")
    sys.exit() 

if m==2 and n>0:
    print("false")
    sys.exit()

else:
    index = []
    tolerance=0
    # 检测所有1的位置
    for i in range(0,m):
        if metrix[i]==1:index.append(i)

    if len(index)!=0:
        for j in range(0,len(index)-1):
            diff = index[j+1]-index[j]-1
            tolerance += ceil((diff-2)/2)
    
        # 最后一位不是1，假装加入定位
        if index[-1]<m-1:
            diff = m-index[-1]-1
            tolerance += diff//2

        if tolerance>=n:print("true")
        elif tolerance<n:print("false")
        sys.exit()
    
    # 没有0的情况
    if len(index)==0:
        tolerance += ceil((m-2)/2)+1
        if tolerance>=n:print("true")
        elif tolerance<n:print("false") 

'''
提取数组中所有1的位置，计算这些位置之间0的数量，两个1之间相邻的0，最多可以承受[(n-2)/2]个不相邻的1，例如3和4个0可承受1,5可承受2

如果数组结尾不是1，那么最后一个1后面跟着若干个0，这些0最多承受不相邻1的数量是n//2个，2或3个0可以有1个不相邻1,4或5则可有2个

再考虑数组全为0的情况，类似第一种情况，不过还可以再多加1个

再将最大承受量和变更数量相比较可得TF
'''