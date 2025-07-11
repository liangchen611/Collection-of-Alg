import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

# a以i为结尾，b为j结尾时最长公共子串的长度
DP = [[0]*(len(b)+1) for _ in range(len(a)+1)]
max_len = 0

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
            if DP[i][j]>max_len:
                max_len = DP[i][j]

print(max_len)

# DP[i][j]：串a以i-1为结尾，串b以j-1结尾时，最长公共子串的长度  
# 如果结尾相等，那么DP中的数值+1，同时更新数值

# 子序列和子串的区别
# 序列可以不连续，而子串则必须连续，一旦二者出现 不相同的数位，直接夹断